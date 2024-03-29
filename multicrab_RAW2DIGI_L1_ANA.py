from CRABClient.UserUtilities import config
from samples import *
from samples_v2 import *
from optparse import OptionParser
import getpass

## expert options
parser = OptionParser()
parser.add_option("--sampleChoice", dest="sampleChoice",  type=int, default=0, help='0:central signal; 1: private signal; 2: data')
parser.add_option("--jobLabel", dest="jobLabel",  type=str, default="_L1_ANA", help='A relevant label for this project')
parser.add_option("--test", dest="test", default=False, action='store_true', help='just produce the crab configuration')
(options,args) = parser.parse_args()

## current user
USER = getpass.getuser()

## samples to run on
chosenSample = chosenListWithSamples(options.sampleChoice)

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
    for sample in chosenSample:
        cconfig = config()
        cconfig.General.workArea = 'crab_projects' + options.jobLabel
        cconfig.General.transferLogs = True
        cconfig.General.requestName = sample[0] + options.jobLabel
        cconfig.JobType.pluginName = 'Analysis'
        cconfig.JobType.psetName = sample[3]
        cconfig.JobType.pyCfgParams = sample[4]
	cconfig.JobType.maxMemoryMB = 5000
        cconfig.Site.storageSite = 'T3_US_FNALLPC'
        cconfig.Data.splitting = 'Automatic'
        #cconfig.Data.unitsPerJob = 5
        cconfig.Data.outLFNDirBase = '/store/user/nimenend/Eff_Rate/'
        cconfig.Data.inputDataset = sample[1]
        cconfig.Data.inputDBS = sample[2]
        print cconfig
        if not options.test:
            print("Submit Jobs...")
            crabCommand('submit', config = cconfig)
