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
