import confEq as ce
import thermEq as te
import heatedTrial as trial
import thermEqHeatUp as tehu

'''print('ThermEq')
te.thermEq(300, 1, 0.01607, '../Resources/trypSuc5M.pdb', '0', '../Output/trypsin300K_5M/thermEq')

print('ConfEq')
ce.confEq(300, 0.01607, 1, '../Output/trypsin300K_5M/thermEq/thermEq1.chk', '../Resources/trypSuc5M.pdb', '0', '../Output/trypsin300K_5M/confEq')
ce.confEq(300, 0.01607, 2, '../Output/trypsin300K_5M/confEq/confEq1.chk', '../Resources/trypSuc5M.pdb', '0', '../Output/trypsin300K_5M/confEq')


trial.sim(300, 'trypsin300K_5M', 1, '../Output/trypsin300K_5M/confEq/confEq2.chk', '../Resources/trypSuc5M.pdb', '0',
             '../Output/trypsin300K_5M/potentialEnergyData')

for num in range(2, 11):
    chk_num = num - 1
    chkpt_file = '../Output/trypsin300K_5M/potentialEnergyData/trypsin300K_5M_trial' + str(chk_num) + '.chk'
    trial.sim(300, 'trypsin300K_5M', num, chkpt_file, '../Resources/trypSuc5M.pdb', '0', '../Output/trypsin300K_5M/potentialEnergyData')'''

# def thermEq(temp, run, newDensity, pdb_file, cudaIndex, saveFolder, chkpt_file):

'''tehu.thermEq(325, 325, .01625, '../Resources/trypSuc5M.pdb', '1', '../Output/trypsin500K_5M/heatUp', '../Output/trypsin300K_5M/thermEq/thermEq1.chk')
tehu.thermEq(350, 350, .01645, '../Resources/trypSuc5M.pdb', '1', '../Output/trypsin500K_5M/heatUp', '../Output/trypsin500K_5M/heatUp/thermEq325.chk')
tehu.thermEq(375, 375, .01672, '../Resources/trypSuc5M.pdb', '1', '../Output/trypsin500K_5M/heatUp', '../Output/trypsin500K_5M/heatUp/thermEq350.chk')
tehu.thermEq(400, 400, .01709, '../Resources/trypSuc5M.pdb', '1', '../Output/trypsin500K_5M/heatUp', '../Output/trypsin500K_5M/heatUp/thermEq375.chk')
tehu.thermEq(425, 425, .01745, '../Resources/trypSuc5M.pdb', '1', '../Output/trypsin500K_5M/heatUp', '../Output/trypsin500K_5M/heatUp/thermEq400.chk')
tehu.thermEq(450, 450, .01799, '../Resources/trypSuc5M.pdb', '1', '../Output/trypsin500K_5M/heatUp', '../Output/trypsin500K_5M/heatUp/thermEq425.chk')
tehu.thermEq(475, 475, .01864, '../Resources/trypSuc5M.pdb', '1', '../Output/trypsin500K_5M/heatUp', '../Output/trypsin500K_5M/heatUp/thermEq450.chk')
tehu.thermEq(500, 500, .01943, '../Resources/trypSuc5M.pdb', '1', '../Output/trypsin500K_5M/heatUp', '../Output/trypsin500K_5M/heatUp/thermEq475.chk')'''

temp = 500
density = .01943
baseFile_name = 'trypsin500K_5M'
pdb_file = '../Resources/trypSuc5M.pdb'
cudaIndex = '0'

'''trial.sim(temp, density, baseFile_name, 1, '../Output/trypsin500K_5M/heatUp/thermEq500.chk', pdb_file,
          cudaIndex, '../Output/' + baseFile_name + '/potentialEnergyData')

for num in range(2, 11):
    chk_num = num - 1
    chkpt_file = '../Output/' + baseFile_name + '/potentialEnergyData/' + baseFile_name + '_trial'+ str(chk_num) + '.chk'
    trial.sim(temp, density, baseFile_name, num, chkpt_file, pdb_file, cudaIndex,
              '../Output/' + baseFile_name + '/potentialEnergyData')'''

chkpt_file = '../Output/' + baseFile_name + '/potentialEnergyData/' + baseFile_name + '_trial10' + '.chk'
trial.sim(temp, density, baseFile_name, 11, chkpt_file, pdb_file, cudaIndex,
              '../Output/' + baseFile_name + '/potentialEnergyData')