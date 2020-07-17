from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'HTo2LongLivedTo4q_MH_125_MFF_1_CTau_5000mm_TuneCP5_14TeV_pythia'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'ppTohToSSTo4b_DIGI_L1.py'

config.Data.inputDataset = '/HTo2LongLivedTo4q_MH_125_MFF_1_CTau_5000mm_TuneCP5_14TeV_pythia/dildick-HTo2LongLivedTo4q_110X_mcRun3_2021_realistic_v6_GEN_SIM_FEVTDEBUGoutput-0048970b41a006c59df023fb34aa563a/USER'
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.publication = True
config.Data.outputDatasetTag = 'HTo2LongLivedTo4q_MH_125_MFF_1_CTau_5000mm_TuneCP5_14TeV_pythia'

config.Site.storageSite = 'T3_US_FNALLPC'
