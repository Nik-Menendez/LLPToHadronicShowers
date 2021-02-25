from CRABClient.UserUtilities import config
from samples import *

cconfig = config()
cconfig.General.workArea = 'crab_projects'
cconfig.General.transferLogs = True
cconfig.JobType.pluginName = 'Analysis'
cconfig.Data.inputDBS = 'phys03'
cconfig.Data.splitting = 'FileBased'
cconfig.Data.unitsPerJob = 5
cconfig.Data.outLFNDirBase = '/store/user/dildick/'
cconfig.Site.storageSite = 'T3_US_FNALLPC'


samples = [
    HTo2LongLivedTo4b_MH_1000_MFF_450_CTau_100000mm,
    HTo2LongLivedTo4b_MH_1000_MFF_450_CTau_10000mm,
    HTo2LongLivedTo4b_MH_125_MFF_12_CTau_9000mm,
    HTo2LongLivedTo4b_MH_125_MFF_12_CTau_900mm,
    HTo2LongLivedTo4b_MH_125_MFF_25_CTau_15000mm,
    HTo2LongLivedTo4b_MH_125_MFF_25_CTau_1500mm,
    HTo2LongLivedTo4b_MH_125_MFF_50_CTau_30000mm,
    HTo2LongLivedTo4b_MH_125_MFF_50_CTau_3000mm,
    HTo2LongLivedTo4b_MH_250_MFF_120_CTau_10000mm,
    HTo2LongLivedTo4b_MH_250_MFF_120_CTau_1000mm,
    HTo2LongLivedTo4b_MH_250_MFF_120_CTau_500mm,
    HTo2LongLivedTo4b_MH_250_MFF_60_CTau_10000mm,
    HTo2LongLivedTo4b_MH_250_MFF_60_CTau_1000mm,
    HTo2LongLivedTo4b_MH_250_MFF_60_CTau_500mm,
    HTo2LongLivedTo4b_MH_350_MFF_160_CTau_10000mm,
    HTo2LongLivedTo4b_MH_350_MFF_160_CTau_1000mm,
    HTo2LongLivedTo4b_MH_350_MFF_160_CTau_5000mm,
    HTo2LongLivedTo4b_MH_350_MFF_80_CTau_10000mm,
    HTo2LongLivedTo4b_MH_350_MFF_80_CTau_1000mm,
    HTo2LongLivedTo4b_MH_350_MFF_80_CTau_500mm,
    HTo2LongLivedTo4q_MH_125_MFF_1_CTau_10000mm,
    HTo2LongLivedTo4q_MH_125_MFF_1_CTau_1000mm,
    HTo2LongLivedTo4q_MH_125_MFF_1_CTau_5000mm
]

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
    for sample in samples:
        cconfig.Data.inputDataset = sample[1]
        cconfig.General.requestName = sample[0] + '_ANA_20210225'
        cconfig.Data.inputDBS = sample[2]
        cconfig.JobType.psetName = sample[3]
        print cconfig
        #crabCommand('submit', config = cconfig)
