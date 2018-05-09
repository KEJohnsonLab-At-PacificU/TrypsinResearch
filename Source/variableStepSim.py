import variableStep as vs

vs.sim(500, .01943, 'trypsinSucVarStep', 1, '../Output/trypsinSucCompHeatUp/thermEq500.chk', '../Resources/trypSucComp.pdb', '0',
         '../Output/variableStepTrial')
vs.sim(500, .01943, 'trypsinSucVarStep', 2, '../Output/variableStepTrial/trypsinSucVarStep1.chk', '../Resources/trypsinSucComp.pdb', '0',
         '../Output/variableStepTrial')
