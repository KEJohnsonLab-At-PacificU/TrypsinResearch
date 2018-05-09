import heatedTrial as trial
import confEq as ce

#  print('ConfEq')
'''ce.confEq(500, .01645, 1, '../Output/trypsinHeatUp/thermEq350.chk', '../Resources/trypsinAlone.pdb', '1',
          '../Output/trypsin350/confEq')

trial.sim(500, .01943, 'trypsin350', 1, '../Output/trypsin350/confEq/confEq1.chk', '../Resources/trypsinAlone.pdb', '1',
         '../Output/trypsin350/potentialEnergyData')'''

for num in range(6, 11):
    chk_num = num - 1
    chkpt_file = '../Output/trypsin500/potentialEnergyData/trypsin500_trial' + str(chk_num) + '.chk'
    trial.sim(500, .01943,  'trypsin500', num, chkpt_file, '../Resources/trypsinAlone.pdb', '1',
              '../Output/trypsin500/potentialEnergyData')
