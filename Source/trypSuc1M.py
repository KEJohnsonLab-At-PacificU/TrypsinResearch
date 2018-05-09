import trypsSucRun as run
import thermEqHeatUp as tehu
import heatedTrial as trial
# run.trypSucRun('../Resources/trypSuc2M.pdb', 300, '1', 'trypsinSuc300K_1M')

'''tehu.thermEq(325, 325, .01625, '../Resources/trypSuc2M.pdb', '0', '../Output/trypsin500K_2M/heatUp', '../Output/trypsinSuc300K_2M/thermEq/thermEq1.chk')
tehu.thermEq(350, 350, .01645, '../Resources/trypSuc2M.pdb', '0', '../Output/trypsin500K_2M/heatUp', '../Output/trypsin500K_2M/heatUp/thermEq325.chk')
tehu.thermEq(375, 375, .01672, '../Resources/trypSuc2M.pdb', '0', '../Output/trypsin500K_2M/heatUp', '../Output/trypsin500K_2M/heatUp/thermEq350.chk')
tehu.thermEq(400, 400, .01709, '../Resources/trypSuc2M.pdb', '0', '../Output/trypsin500K_2M/heatUp', '../Output/trypsin500K_2M/heatUp/thermEq375.chk')
tehu.thermEq(425, 425, .01745, '../Resources/trypSuc2M.pdb', '0', '../Output/trypsin500K_2M/heatUp', '../Output/trypsin500K_2M/heatUp/thermEq400.chk')
tehu.thermEq(450, 450, .01799, '../Resources/trypSuc2M.pdb', '0', '../Output/trypsin500K_2M/heatUp', '../Output/trypsin500K_2M/heatUp/thermEq425.chk')
tehu.thermEq(475, 475, .01864, '../Resources/trypSuc2M.pdb', '0', '../Output/trypsin500K_2M/heatUp', '../Output/trypsin500K_2M/heatUp/thermEq450.chk')
tehu.thermEq(500, 500, .01943, '../Resources/trypSuc2M.pdb', '0', '../Output/trypsin500K_2M/heatUp', '../Output/trypsin500K_2M/heatUp/thermEq475.chk')'''
# def sim(temp, newDensity, type, run, chkpt_file, pdb_file, cudaIndex, saveFolder):

temp = 500
density = .01709
baseFile_name = 'trypsin400K_2M'
pdb_file = '../Resources/trypSuc2M.pdb'
cudaIndex = '1'

trial.sim(temp, density, baseFile_name, 1, '../Output/trypsin500K_2M/heatUp/thermEq400.chk', pdb_file,
         cudaIndex, '../Output/' + baseFile_name + '/potentialEnergyData')

for num in range(2, 11):
    chk_num = num - 1
    chkpt_file = '../Output/' + baseFile_name + '/potentialEnergyData/' + baseFile_name + '_trial'+ str(chk_num) + '.chk'
    trial.sim(temp, density, baseFile_name, num, chkpt_file, pdb_file, cudaIndex,
              '../Output/' + baseFile_name + '/potentialEnergyData')