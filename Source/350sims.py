import confEq as ce
import thermEq as te
import heatedTrial as trial
import thermEqHeatUp as tehu

temp = 350
density = .01645
baseFile_name = 'trypsin350K_5M'
pdb_file = '../Resources/trypsinPDBs/trypSuc5M.pdb'
cudaIndex = '1'

trial.sim(temp, density, baseFile_name, 1, '../Resources/trypsinSuc5M_Checkpoints/thermEq350.chk', pdb_file,
       cudaIndex, '../Output/' + baseFile_name + '/potentialEnergyData')

for num in range(2, 11):
    chk_num = num - 1
    chkpt_file = '../Output/' + baseFile_name + '/potentialEnergyData/' + baseFile_name + '_trial'+ str(chk_num) + '.chk'
    trial.sim(temp, density, baseFile_name, num, chkpt_file, pdb_file, cudaIndex,
              '../Output/'      + baseFile_name + '/potentialEnergyData')