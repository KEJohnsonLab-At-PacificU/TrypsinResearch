import confEq as ce
import thermEq as te
import heatedTrial as trial
import thermEqHeatUp as tehu


temp = 400
density = .01709
baseFile_name = 'trypsin400'
pdb_file = '../Resources/trypsinAlone.pdb'
cudaIndex = '1'

# trial.sim(temp, density, baseFile_name, 1, '../Output/trypsinHeatUp/thermEq400.chk', pdb_file,
#          cudaIndex, '../Output/' + baseFile_name + '/potentialEnergyData')

for num in range(10, 11):
    chk_num = num - 1
    chkpt_file = '../Output/' + baseFile_name + '/potentialEnergyData/' + baseFile_name + '_trial'+ str(chk_num) + '.chk'
    trial.sim(temp, density, baseFile_name, num, chkpt_file, pdb_file, cudaIndex,
              '../Output/' + baseFile_name + '/potentialEnergyData')