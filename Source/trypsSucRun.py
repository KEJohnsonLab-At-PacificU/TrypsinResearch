import confEq as ce
import thermEq as te
import trial


def trypSucRun(pdb_file, temp, cudaIndex, baseFile_name):
    '''print('ThermEq')
    te.thermEq(temp, 1, 0.01607, pdb_file, cudaIndex, '../Output/' + baseFile_name + '/thermEq')

    print('ConfEq')
    ce.confEq(temp, 0.01607, 1, '../Output/' + baseFile_name + '/thermEq/thermEq1.chk', pdb_file, cudaIndex,
              '../Output/' + baseFile_name + '/confEq')
    ce.confEq(temp, 0.01607, 2, '../Output/' + baseFile_name + '/confEq/confEq1.chk', pdb_file, cudaIndex,
              '../Output/' + baseFile_name + '/confEq')

    trial.sim(temp, baseFile_name, 1, '../Output/' + baseFile_name + '/confEq/confEq2.chk', pdb_file,
              cudaIndex, '../Output/' + baseFile_name + '/potentialEnergyData')'''

    for num in range(2, 11):
        chk_num = num - 1
        chkpt_file = '../Output/' + baseFile_name + '/potentialEnergyData/' + baseFile_name + '_trial'+ str(chk_num) + '.chk'
        trial.sim(temp, baseFile_name, num, chkpt_file, pdb_file, cudaIndex,
                  '../Output/' + baseFile_name + '/potentialEnergyData')
