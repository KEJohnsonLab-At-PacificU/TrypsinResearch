import confEq as ce
import trypSucCompTrial as trial

print('ConfEq')
'''ce.confEq(315, .01613, 1, '../Output/trypsinSucCompHeatUp/thermEq315.chk', '../Resources/trypSucComp.pdb', '0',
        '../Output/trypsinSucComp315/confEq')'''

trial.sim(315, .01613, 'trypsinSucComp315', 1, '../Output/trypsinSucComp315/confEq/confEq1.chk', '../Resources/trypSucComp.pdb', '0',
          '../Output/trypsinSucComp315/potentialEnergyData')

for num in range(2, 21):
    chk_num = num - 1
    chkpt_file = '../Output/trypsinSucComp315/potentialEnergyData/trypsinSucComp315_trial' + str(chk_num) + '.chk'
    trial.sim(315, .01613,  'trypsinSucComp315', num, chkpt_file, '../Resources/trypSucComp.pdb', '0',
              '../Output/trypsinSucComp315/potentialEnergyData')
