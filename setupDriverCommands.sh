 cmsDriver.py LLPToHadronicShowers/Generator/python/ppTohToSSTo4b.py \
--fileout file:step1.root --mc \
--eventcontent FEVTDEBUG,LHE --datatier GEN-SIM,LHE --conditions auto:phase1_2021_realistic \
--beamspot Run3RoundOptics25ns13TeVLowSigmaZ --step LHE,GEN,SIM --geometry DB:Extended \
--era Run3 --python_filename ppTohToSSTo4b_GEN_SIM.py --no_exec   -n 10

cmsDriver.py step2.py \
--filein file:step1.root \
--fileout file:step2.root --mc \
--eventcontent FEVTDEBUG --datatier GEN-SIM-DIGI-L1 --conditions auto:phase1_2021_realistic \
--step DIGI:pdigi_valid,L1 --geometry DB:Extended \
--era Run3 --python_filename ppTohToSSTo4b_DIGI_L1.py --no_exec   -n 10



### new samples with 1 GeV LLPs
cmsDriver.py LLPToHadronicShowers/Generator/python/HTo2LongLivedTo4q_MH_125_MFF_1_CTau_1000mm_TuneCP5_14TeV_pythia8.py \
--fileout file:step1.root --mc \
--eventcontent FEVTDEBUG,LHE --datatier GEN-SIM,LHE --conditions auto:phase1_2021_realistic \
--beamspot Run3RoundOptics25ns13TeVLowSigmaZ --step LHE,GEN,SIM --geometry DB:Extended \
--era Run3 --python_filename HTo2LongLivedTo4q_MH_125_MFF_1_CTau_1000mm_TuneCP5_14TeV_pythia_GEN_SIM.py --no_exec   -n 10


cmsDriver.py LLPToHadronicShowers/Generator/python/HTo2LongLivedTo4q_MH_125_MFF_1_CTau_5000mm_TuneCP5_14TeV_pythia8.py \
--fileout file:step1.root --mc \
--eventcontent FEVTDEBUG,LHE --datatier GEN-SIM,LHE --conditions auto:phase1_2021_realistic \
--beamspot Run3RoundOptics25ns13TeVLowSigmaZ --step LHE,GEN,SIM --geometry DB:Extended \
--era Run3 --python_filename HTo2LongLivedTo4q_MH_125_MFF_1_CTau_5000mm_TuneCP5_14TeV_pythia_GEN_SIM.py --no_exec   -n 10


cmsDriver.py LLPToHadronicShowers/Generator/python/HTo2LongLivedTo4q_MH_125_MFF_1_CTau_10000mm_TuneCP5_14TeV_pythia8.py \
--fileout file:step1.root --mc \
--eventcontent FEVTDEBUG,LHE --datatier GEN-SIM,LHE --conditions auto:phase1_2021_realistic \
--beamspot Run3RoundOptics25ns13TeVLowSigmaZ --step LHE,GEN,SIM --geometry DB:Extended \
--era Run3 --python_filename HTo2LongLivedTo4q_MH_125_MFF_1_CTau_10000mm_TuneCP5_14TeV_pythia_GEN_SIM.py --no_exec   -n 10



cmsDriver.py LLPToHadronicShowers/Generator/python/HTo2LongLivedTo4q_MH_125_MFF_1_CTau_10000mm_TuneCP5_14TeV_pythia8.py \
--fileout file:step1.root --mc \
--eventcontent FEVTDEBUG,LHE --datatier GEN-SIM,LHE,DIGI --conditions auto:phase1_2021_realistic \
--beamspot Run3RoundOptics25ns13TeVLowSigmaZ --step LHE,GEN,SIM,DIGI --geometry DB:Extended \
--era Run3 --python_filename HTo2LongLivedTo4q_MH_125_MFF_1_CTau_10000mm_TuneCP5_14TeV_pythia_GEN_SIM_DIGI.py --no_exec   -n 10






cmsDriver.py Configuration/GenProduction/python/TSG-Run3Winter20GS-00040-fragment.py --python_filename TSG-Run3Winter20GS-00040_1_L1_cfg.py --eventcontent FEVTDEBUG --customise Configuration/DataProcessing/Utils.addMonitoring --datatier GEN-SIM-DIGI --fileout file:TSG-Run3Winter20GS-00040.root --conditions 110X_mcRun3_2021_realistic_v6 --beamspot Run3RoundOptics25ns13TeVLowSigmaZ --step GEN,SIM,DIGI:pdigi_valid,L1 --geometry DB:Extended --era Run3 --no_exec --mc -n 10 || exit $? ;

## TSG numbers
00040
00064
00065
00066
00067
00068
