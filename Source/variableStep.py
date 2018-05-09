
##########################################################################
# Imports (from openmm library)
##########################################################################
from __future__ import print_function
from simtk.openmm.app import *
from simtk.openmm import *
from simtk import unit
import sys
import volumeEditor as ve

def sim(temp, newDensity, type, run, chkpt_file, pdb_file, cudaIndex, saveFolder):
    ##########################################################################
    # Variables
    ##########################################################################
    Temp = temp * unit.kelvin                                       # Temperature for the simulation
    output_steps = 50                                               # How often to output information
    LI_fric_coef = 1.0 / unit.picoseconds                           # the langevin integrator friction coeficient
    time_of_step = 0.5 * unit.femtoseconds                          # the time length of each simulation step
    tot_time = 0.5 * unit.nanoseconds                               # the total time of the simulation
    num_steps = tot_time / time_of_step                             # the number of steps for the simulation
    sim_steps = math.ceil(num_steps)                                # 1 nanoseconds long at 1/2 femtosecond timestep
                                                                    # (number of steps rounded up)
    screen_output = math.ceil(sim_steps / 10)                       # print output to the screen in 10% intervals
    save_baseName = saveFolder + '/' + type + '_trial' + str(run)   # a string that designates the base save name

    print('Starting Simulation: ', save_baseName)
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
    integrator = VariableLangevinIntegrator(Temp, LI_fric_coef, 0.001) # 0.001 is the suggested error tolerance

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
    # Loading Checkpoint file and opening reporters
    ##########################################################################
    with open(chkpt_file, 'rb') as f:
        simulation.context.loadCheckpoint(f.read())

    # add a dcd reporter
    simulation.reporters.append(app.DCDReporter(save_baseName + '.dcd',
                                                output_steps))

    # add a reporter for the simulation
    simulation.reporters.append(app.StateDataReporter(save_baseName + '.log',
                                                      output_steps, step=True,
                                                      time=True,
                                                      potentialEnergy=True,
                                                      kineticEnergy=True,
                                                      totalEnergy=True,
                                                      temperature=True,
                                                      remainingTime=True,
                                                      speed=True,
                                                      totalSteps=sim_steps,
                                                      separator='\t'))

    simulation.reporters.append(app.StateDataReporter(sys.stdout,
                                                      screen_output,
                                                      progress=True,
                                                      remainingTime=True,
                                                      totalSteps=sim_steps))

    ##########################################################################
    # Run the Simulation
    ##########################################################################
    print('Running...')

    if run is 1:
        simulation.context.setTime(0)
        simulation.currentStep = 0

    simulation.step(sim_steps)

    ##########################################################################
    # Create a checkpoint file at the end of the simulation
    ##########################################################################
    print('Saving Checkpoint...')
    with open(save_baseName + '.chk', 'wb') as f:
        f.write(simulation.context.createCheckpoint())

    print('Done!')