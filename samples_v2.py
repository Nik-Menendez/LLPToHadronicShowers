import os

crabInputDBSGlob = 'global'
crabInputDBSUser = 'phys03'
directory = os.path.expandvars("$CMSSW_BASE/src/")
package = "GEMCode/GEMValidation/test/"
cmsRun = directory + package + "step2_ReL1_Run3_MuonShower.py"
cmsRunOptionsRun2RAW = ["crab=True", "run3=False", "runOnRaw=True"]
cmsRunOptionsRun3RAW = ["crab=True", "run3=True", "runOnRaw=True"]
cmsRunOptionsRun3DIGI = ["crab=True", "run3=True", "runOnRaw=False"]

HTo2LongLivedTo4b_MH_1000_MFF_450_CTau_100000mm = [
    "HTo2LongLivedTo4b_MH_1000_MFF_450_CTau_100000mm",
    '/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-100000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    crabInputDBSGlob,
    cmsRun,
    cmsRunOptionsRun3RAW
]

HTo2LongLivedTo4b_MH_1000_MFF_450_CTau_10000mm = [
    "HTo2LongLivedTo4b_MH_1000_MFF_450_CTau_10000mm",
    '/HTo2LongLivedTo4b_MH-1000_MFF-450_CTau-10000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    crabInputDBSGlob,
    cmsRun,
    cmsRunOptionsRun3RAW
]

HTo2LongLivedTo4b_MH_125_MFF_12_CTau_9000mm = [
    "HTo2LongLivedTo4b_MH_125_MFF_12_CTau_9000mm",
    '/HTo2LongLivedTo4b_MH-125_MFF-12_CTau-9000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    crabInputDBSGlob,
    cmsRun,
    cmsRunOptionsRun3RAW
]

HTo2LongLivedTo4b_MH_125_MFF_12_CTau_900mm = [
    "HTo2LongLivedTo4b_MH_125_MFF_12_CTau_900mm",
    '/HTo2LongLivedTo4b_MH-125_MFF-12_CTau-900mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    crabInputDBSGlob,
    cmsRun,
    cmsRunOptionsRun3RAW
]

HTo2LongLivedTo4b_MH_125_MFF_25_CTau_15000mm = [
    "HTo2LongLivedTo4b_MH_125_MFF_25_CTau_15000mm",
    '/HTo2LongLivedTo4b_MH-125_MFF-25_CTau-15000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    crabInputDBSGlob,
    cmsRun,
    cmsRunOptionsRun3RAW
]

HTo2LongLivedTo4b_MH_125_MFF_25_CTau_1500mm = [
    "HTo2LongLivedTo4b_MH_125_MFF_25_CTau_1500mm",
    '/HTo2LongLivedTo4b_MH-125_MFF-25_CTau-1500mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    crabInputDBSGlob,
    cmsRun,
    cmsRunOptionsRun3RAW
]

HTo2LongLivedTo4b_MH_125_MFF_50_CTau_30000mm = [
    "HTo2LongLivedTo4b_MH_125_MFF_50_CTau_30000mm",
    '/HTo2LongLivedTo4b_MH-125_MFF-50_CTau-30000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    crabInputDBSGlob,
    cmsRun,
    cmsRunOptionsRun3RAW
]

HTo2LongLivedTo4b_MH_125_MFF_50_CTau_3000mm = [
    "HTo2LongLivedTo4b_MH_125_MFF_50_CTau_3000mm",
    '/HTo2LongLivedTo4b_MH-125_MFF-50_CTau-3000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    crabInputDBSGlob,
    cmsRun,
    cmsRunOptionsRun3RAW
]

HTo2LongLivedTo4b_MH_250_MFF_120_CTau_10000mm = [
    "HTo2LongLivedTo4b_MH_250_MFF_120_CTau_10000mm",
    '/HTo2LongLivedTo4b_MH-250_MFF-120_CTau-10000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    crabInputDBSGlob,
    cmsRun,
    cmsRunOptionsRun3RAW
]

HTo2LongLivedTo4b_MH_250_MFF_120_CTau_1000mm = [
    "HTo2LongLivedTo4b_MH_250_MFF_120_CTau_1000mm",
    '/HTo2LongLivedTo4b_MH-250_MFF-120_CTau-1000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    crabInputDBSGlob,
    cmsRun,
    cmsRunOptionsRun3RAW
]

HTo2LongLivedTo4b_MH_250_MFF_120_CTau_500mm = [
    "HTo2LongLivedTo4b_MH_250_MFF_120_CTau_500mm",
    '/HTo2LongLivedTo4b_MH-250_MFF-120_CTau-500mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    crabInputDBSGlob,
    cmsRun,
    cmsRunOptionsRun3RAW
]

HTo2LongLivedTo4b_MH_250_MFF_60_CTau_10000mm = [
    "HTo2LongLivedTo4b_MH_250_MFF_60_CTau_10000mm",
    '/HTo2LongLivedTo4b_MH-250_MFF-60_CTau-10000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    crabInputDBSGlob,
    cmsRun,
    cmsRunOptionsRun3RAW
]

HTo2LongLivedTo4b_MH_250_MFF_60_CTau_1000mm = [
    "HTo2LongLivedTo4b_MH_250_MFF_60_CTau_1000mm",
    '/HTo2LongLivedTo4b_MH-250_MFF-60_CTau-1000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    crabInputDBSGlob,
    cmsRun,
    cmsRunOptionsRun3RAW
]

HTo2LongLivedTo4b_MH_250_MFF_60_CTau_500mm = [
    "HTo2LongLivedTo4b_MH_250_MFF_60_CTau_500mm",
    '/HTo2LongLivedTo4b_MH-250_MFF-60_CTau-500mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    crabInputDBSGlob,
    cmsRun,
    cmsRunOptionsRun3RAW
]

HTo2LongLivedTo4b_MH_350_MFF_160_CTau_10000mm = [
    "HTo2LongLivedTo4b_MH_350_MFF_160_CTau_10000mm",
    '/HTo2LongLivedTo4b_MH-350_MFF-160_CTau-10000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    crabInputDBSGlob,
    cmsRun,
    cmsRunOptionsRun3RAW
]

HTo2LongLivedTo4b_MH_350_MFF_160_CTau_1000mm = [
    "HTo2LongLivedTo4b_MH_350_MFF_160_CTau_1000mm",
    '/HTo2LongLivedTo4b_MH-350_MFF-160_CTau-1000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    crabInputDBSGlob,
    cmsRun,
    cmsRunOptionsRun3RAW
]

HTo2LongLivedTo4b_MH_350_MFF_160_CTau_500mm = [
    "HTo2LongLivedTo4b_MH_350_MFF_160_CTau_500mm",
    '/HTo2LongLivedTo4b_MH-350_MFF-160_CTau-500mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    crabInputDBSGlob,
    cmsRun,
    cmsRunOptionsRun3RAW
]

HTo2LongLivedTo4b_MH_350_MFF_80_CTau_10000mm = [
    "HTo2LongLivedTo4b_MH_350_MFF_80_CTau_10000mm",
    '/HTo2LongLivedTo4b_MH-350_MFF-80_CTau-10000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    crabInputDBSGlob,
    cmsRun,
    cmsRunOptionsRun3RAW
]

HTo2LongLivedTo4b_MH_350_MFF_80_CTau_1000mm = [
    "HTo2LongLivedTo4b_MH_350_MFF_80_CTau_1000mm",
    '/HTo2LongLivedTo4b_MH-350_MFF-80_CTau-1000mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    crabInputDBSGlob,
    cmsRun,
    cmsRunOptionsRun3RAW
]

HTo2LongLivedTo4b_MH_350_MFF_80_CTau_500mm = [
    "HTo2LongLivedTo4b_MH_350_MFF_80_CTau_500mm",
    '/HTo2LongLivedTo4b_MH-350_MFF-80_CTau-500mm_TuneCP5_14TeV_pythia8/Run3Winter20DRPremixMiniAOD-110X_mcRun3_2021_realistic_v6-v2/GEN-SIM-RAW',
    crabInputDBSGlob,
    cmsRun,
    cmsRunOptionsRun3RAW
]

HTo2LongLivedTo4q_MH_125_MFF_1_CTau_10000mm = [
    "HTo2LongLivedTo4q_MH_125_MFF_1_CTau_10000mm",
    '/HTo2LongLivedTo4q_MH_125_MFF_1_CTau_10000mm_TuneCP5_14TeV_pythia/nimenend-HTo2LongLivedTo4q_MH_125_MFF_1_CTau_10000mm_TuneCP5_14TeV_pythia-adb3cd2089542b29cb06bec5451b8c0e/USER',
    crabInputDBSUser,
    cmsRun,
    cmsRunOptionsRun3DIGI
]

HTo2LongLivedTo4q_MH_125_MFF_1_CTau_1000mm = [
    "HTo2LongLivedTo4q_MH_125_MFF_1_CTau_1000mm",
    '/HTo2LongLivedTo4q_MH_125_MFF_1_CTau_1000mm_TuneCP5_14TeV_pythia/nimenend-HTo2LongLivedTo4q_MH_125_MFF_1_CTau_1000mm_TuneCP5_14TeV_pythia-adb3cd2089542b29cb06bec5451b8c0e/USER',
    crabInputDBSUser,
    cmsRun,
    cmsRunOptionsRun3DIGI
]

HTo2LongLivedTo4q_MH_125_MFF_1_CTau_5000mm = [
    "HTo2LongLivedTo4q_MH_125_MFF_1_CTau_5000mm",
    '/HTo2LongLivedTo4q_MH_125_MFF_1_CTau_5000mm_TuneCP5_14TeV_pythia/nimenend-HTo2LongLivedTo4q_MH_125_MFF_1_CTau_5000mm_TuneCP5_14TeV_pythia-adb3cd2089542b29cb06bec5451b8c0e/USER',
    crabInputDBSUser,
    cmsRun,
    cmsRunOptionsRun3DIGI
]

ZeroBias_Run2018D = [
    "ZeroBias_Run2018D",
    '/ZeroBias/Run2018D-v1/RAW',
    crabInputDBSGlob,
    cmsRun,
    cmsRunOptionsRun2RAW
]

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
    HTo2LongLivedTo4b_MH_350_MFF_160_CTau_500mm,

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

def chosenListWithSamples(choice):
    ## make a choice
    if choice == 0:
        return central_signal

    elif choice == 1:
        return private_signal

    elif choice == 2:
        return data

    else:
        return central_signal
