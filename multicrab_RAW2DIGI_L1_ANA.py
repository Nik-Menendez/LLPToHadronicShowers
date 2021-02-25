from CRABClient.UserUtilities import config
from samples import *
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-s", dest="sampleChoice",  type=int, default=0, help='0:central signal; 1: private signal; 2: data')
(options,args) = parser.parse_args()

central_signal = [
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
    HTo2LongLivedTo4b_MH_350_MFF_80_CTau_500mm
]

private_signal = [
    HTo2LongLivedTo4q_MH_125_MFF_1_CTau_10000mm,
    HTo2LongLivedTo4q_MH_125_MFF_1_CTau_1000mm,
    HTo2LongLivedTo4q_MH_125_MFF_1_CTau_5000mm
]

data = [
    ZeroBias_Run2018D
]

chosenSample = []

## make a choice
if options.sampleChoice == 0:
    chosenSample = central_signal

if options.sampleChoice == 1:
    chosenSample = private_signal

if options.sampleChoice == 2:
    chosenSample = data

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
    for sample in chosenSample:
        cconfig = config()
        cconfig.General.workArea = 'crab_projects'
        cconfig.General.transferLogs = True
        cconfig.General.requestName = sample[0] + '_ANA_20210225_v3'
        cconfig.JobType.pluginName = 'Analysis'
        cconfig.JobType.psetName = sample[3]
        cconfig.Site.storageSite = 'T3_US_FNALLPC'
        cconfig.Data.splitting = 'FileBased'
        cconfig.Data.unitsPerJob = 5
        cconfig.Data.outLFNDirBase = '/store/user/dildick/'
        cconfig.Data.inputDataset = sample[1]
        cconfig.Data.inputDBS = sample[2]
        print cconfig
        #crabCommand('submit', config = cconfig)
