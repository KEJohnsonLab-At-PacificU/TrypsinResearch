import confEq as ce
import thermEq as te
import trial

print('ThermEq')
te.thermEq(300, 1, '../Resources/trypsinAlone.pdb', '0', '../Output/trypsin300/thermEq')

print('ConfEq')
ce.confEq(300, 1, '../Output/trypsin300/thermEq/thermEq1.chk', '../Resources/trypsinAlone.pdb', '0', '../Output/trypsin300/confEq')
ce.confEq(300, 2, '../Output/trypsin300/confEq/confEq1.chk', '../Resources/trypsinAlone.pdb', '0', '../Output/trypsin300/confEq')


trial.sim(300, 'trial', 1, '../Output/trypsin300/confEq/confEq2.chk', '../Resources/trypsinAlone.pdb', '0',
         '../Output/trypsin300/potentialEnergyData')

for num in range(2, 11):
    chk_num = num - 1
    chkpt_file = '../Output/trypsin300/potentialEnergyData/trypsin300_trial' + str(chk_num) + '.chk'
    trial.sim(300, 'trypsin300', num, chkpt_file, '../Resources/trypsinAlone.pdb', '0', '../Output/trypsin300/potentialEnergyData')
