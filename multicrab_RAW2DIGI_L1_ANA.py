from CRABClient.UserUtilities import config

cconfig = config()
cconfig.General.workArea = 'crab_projects'
cconfig.General.transferLogs = True
cconfig.JobType.pluginName = 'Analysis'
cconfig.Data.inputDBS = 'phys03'
cconfig.Data.splitting = 'FileBased'
cconfig.Data.unitsPerJob = 1
cconfig.Data.outLFNDirBase = '/store/group/XXX/'
cconfig.Site.storageSite = 'T3_US_FNALLPC'

samples = {
    '/HTo2LongLivedTo4b_MH-350_MFF-80_CTau-500mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    '/HTo2LongLivedTo4b_MH-350_MFF-80_CTau-1000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    '/HTo2LongLivedTo4b_MH-350_MFF-80_CTau-10000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    '/HTo2LongLivedTo4b_MH-350_MFF-160_CTau-500mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    '/HTo2LongLivedTo4b_MH-350_MFF-160_CTau-1000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    '/HTo2LongLivedTo4b_MH-350_MFF-160_CTau-10000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    '/HTo2LongLivedTo4b_MH-250_MFF-60_CTau-500mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    '/HTo2LongLivedTo4b_MH-250_MFF-60_CTau-1000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    '/HTo2LongLivedTo4b_MH-250_MFF-60_CTau-10000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    '/HTo2LongLivedTo4b_MH-250_MFF-120_CTau-500mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    '/HTo2LongLivedTo4b_MH-250_MFF-120_CTau-1000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    '/HTo2LongLivedTo4b_MH-250_MFF-120_CTau-10000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    '/HTo2LongLivedTo4b_MH-125_MFF-50_CTau-3000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    '/HTo2LongLivedTo4b_MH-125_MFF-50_CTau-30000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    '/HTo2LongLivedTo4b_MH-125_MFF-25_CTau-1500mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    '/HTo2LongLivedTo4b_MH-125_MFF-25_CTau-15000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    '/HTo2LongLivedTo4b_MH-125_MFF-12_CTau-900mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    '/HTo2LongLivedTo4b_MH-125_MFF-12_CTau-9000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    '/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-10000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    '/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-100000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    '/Nu_E10-pythia8-gun/Run3Winter20DRPremixMiniAOD-SNB_110X_mcRun3_2021_realistic_v6-v1/GEN-SIM-RAW',
    '/Neutrino_Pt-2to20_gun/Run3Winter20DRPremixMiniAOD-SNB_110X_mcRun3_2021_realistic_v6-v1/GEN-SIM-RAW',
}

directory = '/uscms/home/dildick/nobackup/work/LLPStudiesWithSergoEtAL/CMSSW_11_1_0_pre6/src/'

if __name__ == '__main__':
    from CRABAPI.RawCommand import crabCommand
    for s in samples:
        cconfig.Data.inputDataset = s
        cconfig.JobType.psetName = directory + 'L1Trigger/CSCTriggerPrimitives/test/CSCTPEmulator_cfg.py'
        cconfig.General.requestName = cconfig.Data.inputDataset.split('/')[1] + '_RAW2DIGI_L1_ANA_20200515'
        print cconfig
        #crabCommand('submit', config = cconfig)
