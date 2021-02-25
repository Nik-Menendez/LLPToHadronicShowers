from CRABClient.UserUtilities import config

cconfig = config()
cconfig.General.workArea = 'crab_projects'
cconfig.General.transferLogs = True
cconfig.JobType.pluginName = 'PrivateMC'
cconfig.Data.splitting = 'EventBased'
nJobs = 500
cconfig.Data.totalUnits = 100 * nJobs
cconfig.Data.unitsPerJob = nJobs
cconfig.Data.outLFNDirBase = '/store/user/dildick/'
cconfig.Site.storageSite = 'T3_US_FNALLPC'

samples = [
#    ['HTo2LongLivedTo4q_MH_125_MFF_1_CTau_10000mm_TuneCP5_14TeV_pythia_GEN_SIM.py',
#     'HTo2LongLivedTo4q_MH_125_MFF_1_CTau_10000mm_TuneCP5_14TeV_pythia',
#     'HTo2LongLivedTo4q_110X_mcRun3_2021_realistic_v6_GEN_SIM'],
    ['HTo2LongLivedTo4q_MH_125_MFF_1_CTau_1000mm_TuneCP5_14TeV_pythia_GEN_SIM.py',
     'HTo2LongLivedTo4q_MH_125_MFF_1_CTau_1000mm_TuneCP5_14TeV_pythia',
     'HTo2LongLivedTo4q_110X_mcRun3_2021_realistic_v6_GEN_SIM'],
#    ['HTo2LongLivedTo4q_MH_125_MFF_1_CTau_5000mm_TuneCP5_14TeV_pythia_GEN_SIM.py',
#     'HTo2LongLivedTo4q_MH_125_MFF_1_CTau_5000mm_TuneCP5_14TeV_pythia',
#     'HTo2LongLivedTo4q_110X_mcRun3_2021_realistic_v6_GEN_SIM']
]

directory = '/uscms/home/dildick/nobackup/work/LLPStudiesWithSergoEtAL/CMSSW_11_1_0_pre6/src/LLPToHadronicShowers/'

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
    for s in samples:
        cconfig.JobType.psetName = directory + s[0]
        cconfig.Data.outputPrimaryDataset = s[1]
        cconfig.Data.outputDatasetTag = s[2]
        cconfig.General.requestName = s[1]
        print cconfig
        crabCommand('submit', config = cconfig)
