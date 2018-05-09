##########################################################################
# Imports (from openmm library)
##########################################################################
from __future__ import print_function
from simtk.openmm.app import *
from simtk.openmm import *
from simtk import unit
from simtk.openmm.app.pdbfile import *
import volumeEditor as ve

##########################################################################
# Variables
##########################################################################
Temp = 300 * unit.kelvin                    # Temperature for the simulation
output_steps = 50                           # How often to output information
LI_fric_coef = 1.0 / unit.picoseconds       # the langevin integrator friction coeficient
time_of_step = 0.5 * unit.femtoseconds      # the time length of each simulation step
tot_time = 0.5 * unit.nanoseconds           # the total time of the simulation
num_steps = tot_time / time_of_step         # the number of steps for the simulation
pdb_file = "../Resources/trypsinPDBs/trypsinAlone.pdb"
cudaIndex = 1


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

print('Creating Langevin Integrator...')
integrator = LangevinIntegrator(Temp, LI_fric_coef, time_of_step)

print('Setting Platform...')
platform = Platform.getPlatformByName('CUDA')  # tell OpenMM to use the CUDA platform
properties = {'CudaDeviceIndex': cudaIndex,
              'CudaPrecision': 'mixed',
              'DisablePmeStream': 'True'}  # run using a CudaDevice - GPU[0] w/ mixed precision

print('Creating Simulation')
simulation = app.Simulation(pdb.topology, system, integrator)  # create the simulation object
simulation.context.setPositions(pdb.positions)  # set the positions for the simulations based on our pdb object and file

##########################################################################
# Minimize the system
##########################################################################
print('Minimizing...')
simulation.minimizeEnergy()
positions = simulation.context.getState(getPositions=True, enforcePeriodicBox=True).getPositions()

with open('../Resources/trypsinPDBs/trypsinMin.pdb', 'w') as f:
    app.PDBFile.writeFile (simulation.topology, positions, f)