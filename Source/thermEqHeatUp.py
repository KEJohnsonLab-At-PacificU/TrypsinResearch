
##########################################################################
# Imports (from openmm library)
##########################################################################
from __future__ import print_function
from simtk.openmm.app import *
from simtk.openmm import *
from simtk import unit
import volumeEditor as ve

def thermEq(temp, run, newDensity, pdb_file, cudaIndex, saveFolder, chkpt_file):
    ##########################################################################
    # Variables
    ##########################################################################
    Temp = temp * unit.kelvin                    # Temperature for the simulation
    output_steps = 50                           # How often to output information
    LI_fric_coef = 1.0 / unit.picoseconds       # the langevin integrator friction coeficient
    time_of_step = 0.5 * unit.femtoseconds      # the time length of each simulation step
    tot_time = 0.5 * unit.nanoseconds           # the total time of the simulation
    num_steps = tot_time / time_of_step         # the number of steps for the simulation
    sim_steps = math.ceil(num_steps)            # 1 nanoseconds long at 1/2 femtosecond timestep
                                                # (number of steps rounded up)
    save_baseName = saveFolder + '/thermEq' + str(run) # a string that designates the base save name
    KE_tolerance = 0.005                        # This will be used to ensure there is less
                                                # then a .5% change in Kinetic Energy
    KE_eq_steps = 50                            # the number of steps per cycle during equilibration

    ##########################################################################
    # System Setup
    ##########################################################################
    print('Loading Force Field and PDB file...')
    forcefield = app.ForceField('amoebaProtein.xml', 'amoebaSmall.xml', 'amoebaSmallOrg.xml')  # load our 3 force fields
    pdb = app.PDBFile(pdb_file)  # load to the pdb file

    # Creating the system
    print('Creating System...')
    system = forcefield.createSystem(pdb.topology,
                                     nonbondedMethod=app.PME,
                                     nonboundedCutoff=10 * unit.angstroms,
                                     constraints=HBonds,
                                     vdwCutoff=1.2 * unit.nanometer,
                                     rigidWater=None)
    ##########################################################################
    # Changing Box Size to account for Temperature Variation
    ##########################################################################
    vecs = system.getDefaultPeriodicBoxVectors()
    print("Original Box Parameters at 300 K:")
    print(vecs)
    newVecs = ve.editVolume(vecs, 0.01607, newDensity)
    print("New Box Parameters at ", temp, " K:")
    print(newVecs)
    system.setDefaultPeriodicBoxVectors(newVecs[0], newVecs[1], newVecs[2])

    print('Creating Langevin Integrator...')
    integrator = LangevinIntegrator(Temp, LI_fric_coef, time_of_step)

    print('Setting Platform...')
    platform = Platform.getPlatformByName('CUDA')  # tell OpenMM to use the CUDA platform
    properties = {'CudaDeviceIndex': cudaIndex,
                  'CudaPrecision': 'mixed',
                  'DisablePmeStream': 'True'}  # run using a CudaDevice - GPU[0] w/ mixed precision

    print('Creating Simulation')
    simulation = app.Simulation(pdb.topology, system, integrator, platform, properties)  # create the simulation object
    simulation.context.setPositions(pdb.positions)  # set the positions for the simulations based on our pdb object and file

    print('Using Platform', simulation.context.getPlatform().getName())

    ##########################################################################
    # Variables to calculate system temperature
    ##########################################################################
    BOLTZ = unit.MOLAR_GAS_CONSTANT_R
    particles = system.getNumParticles()
    constraints = system.getNumConstraints()
    DOF = 3 * particles - constraints

    ##########################################################################
    # Minimize the system
    ##########################################################################
    with open(chkpt_file, 'rb') as f:
        simulation.context.loadCheckpoint(f.read())

    ##########################################################################
    # Thermally Equilibrate the system to 300K
    ##########################################################################
    print('Equilibrating...')
    # Set the velocities in the simulation to the temperature of the simulation
    simulation.context.setVelocitiesToTemperature(Temp)

    KE_old = simulation.context.getState(getEnergy=True).getKineticEnergy()

    # add a reporter for the simulation
    simulation.reporters.append(app.StateDataReporter(save_baseName + '.log',
                                                      output_steps, step=True,
                                                      time=True,
                                                      potentialEnergy=True,
                                                      kineticEnergy=True,
                                                      totalEnergy=True,
                                                      temperature=True,
                                                      separator='\t'))

    simulation.step(KE_eq_steps)

    KE_new = simulation.context.getState(getEnergy=True).getKineticEnergy()
    current_temp = KE_new / (0.5 * DOF * BOLTZ)

    while (abs(KE_new - KE_old) / KE_old > KE_tolerance or current_temp < Temp):
        KE_old = KE_new
        simulation.step(KE_eq_steps)
        KE_new = simulation.context.getState(getEnergy=True).getKineticEnergy()
        current_temp = KE_new / (0.5 * DOF * BOLTZ)
        print('Kinetic Energy Temp = ', current_temp)

    print('Set Temp = ', integrator.getTemperature())
    print('Final Kinetic Energy Temp = ', current_temp)

    ##########################################################################
    # Create a checkpoint file at the end of the simulation
    ##########################################################################
    print('Saving Checkpoint...')
    with open(save_baseName + '.chk', 'wb') as f:
        f.write(simulation.context.createCheckpoint())

    print('Done!')