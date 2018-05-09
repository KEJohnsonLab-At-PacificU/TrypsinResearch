import confEq as ce
import thermEq as te
import heatedTrial as trial
import thermEqHeatUp as tehu

temp = 400
density = .01709
baseFile_name = 'trypsin400K_2M'
pdb_file = '../Resources/trypsinPDBs/trypSuc2M.pdb'
cudaIndex = '0'

#trial.sim(temp, density, baseFile_name, 1, '../Resources/trypsinSuc2M_Checkpoints/thermEq400.chk', pdb_file,
#          cudaIndex, '../Output/' + baseFile_name + '/potentialEnergyData')

for num in range(9, 11):
    chk_num = num - 1
    chkpt_file = '../Output/' + baseFile_name + '/potentialEnergyData/' + baseFile_name + '_trial'+ str(chk_num) + '.chk'
    trial.sim(temp, density, baseFile_name, num, chkpt_file, pdb_file, cudaIndex,
              '../Output/' + baseFile_name + '/potentialEnergyData')