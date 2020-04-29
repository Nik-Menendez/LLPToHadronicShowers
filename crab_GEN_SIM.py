from CRABClient.UserUtilities import config
config = config()
config.General.workArea = 'crab_projects'
config.General.transferLogs = True
config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'ppTohToSSTo4b_GEN_SIM.py'
config.General.transferOutputs = True
config.Data.splitting = 'EventBased'
nJobs = 1000
config.Data.totalUnits = 100 * nJobs
config.Data.unitsPerJob = nJobs
config.Data.outLFNDirBase = '/store/user/dildick/'
config.Data.publication = True
config.Site.storageSite = 'T3_US_FNALLPC'
config.Data.outputPrimaryDataset = 'ppTohToSSTo4b'
config.Data.outputDatasetTag = 'ppTohToSSTo4b_GEN_SIM'
config.General.requestName = config.Data.outputDatasetTag
