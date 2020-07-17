from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'HTo2LongLivedTo4q_MH_125_MFF_1_CTau_5000mm_TuneCP5_14TeV_pythia_ANA'
config.General.workArea = 'crab_mc'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../L1Trigger/CSCTriggerPrimitives/test/CSCTPEmulator_Run3_MC_cfg.py'

config.Data.inputDataset = '/HTo2LongLivedTo4q_MH_125_MFF_1_CTau_5000mm_TuneCP5_14TeV_pythia/nimenend-HTo2LongLivedTo4q_MH_125_MFF_1_CTau_5000mm_TuneCP5_14TeV_pythia-adb3cd2089542b29cb06bec5451b8c0e/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/nimenend/All_LCT/'
config.Data.publication = True
config.Data.outputDatasetTag = 'HTo2LongLivedTo4q_MH_125_MFF_1_CTau_5000mm_TuneCP5_14TeV_pythia_ALL_LCT_Analyzed'

config.Site.storageSite = 'T3_US_FNALLPC'
