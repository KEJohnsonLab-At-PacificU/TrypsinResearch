import variableStep as vs

temp = 500
density = .01943
baseFile_name = 'trypsin500K'
pdb_file = '../Resources/trypsinAlone.pdb'
cudaIndex = '1'

vs.sim(temp, density, baseFile_name, 11, '../Output/trypsin500K/trypsin500_trial10.chk', pdb_file,
         cudaIndex, '../Output/' + baseFile_name)

for num in range(12, 21):
    chk_num = num - 1
    chkpt_file = '../Output/' + baseFile_name + '/potentialEnergyData/' + baseFile_name + '_trial'+ str(chk_num) + '.chk'
    vs.sim(temp, density, baseFile_name, num, chkpt_file, pdb_file, cudaIndex,
              '../Output/' + baseFile_name)