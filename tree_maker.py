from __future__ import division

from ROOT import TFile, TTree
from tqdm import tqdm
from collections import Counter
import pickle

in_dir = "/eos/uscms/store/user/nimenend/Eff_Rate/Final/"
bkg_files = ["ZeroBias_Data"]
sig_files = [
"MH_1000_MFF_450_CTau_100000mm",
"MH_125_MFF_12_CTau_9000mm",
"MH_125_MFF_12_CTau_900mm",
"MH_125_MFF_1_CTau_10000mm",
"MH_125_MFF_1_CTau_1000mm",
"MH_125_MFF_1_CTau_5000mm",
"MH_125_MFF_25_CTau_15000mm",
"MH_125_MFF_25_CTau_1500mm",
"MH_125_MFF_50_CTau_30000mm",
"MH_125_MFF_50_CTau_3000mm",
"MH_250_MFF_120_CTau_10000mm",
#"MH_250_MFF_120_CTau_1000mm",
"MH_250_MFF_120_CTau_500mm",
"MH_250_MFF_60_CTau_10000mm",
"MH_250_MFF_60_CTau_1000mm",
"MH_250_MFF_60_CTau_500mm",
"MH_350_MFF_160_CTau_10000mm",
"MH_350_MFF_160_CTau_1000mm",
"MH_350_MFF_160_CTau_500mm",
"MH_350_MFF_80_CTau_10000mm",
"MH_350_MFF_80_CTau_1000mm",
"MH_350_MFF_80_CTau_500mm",
"ZeroBias_Data",
]

bx_comp_min, bx_comp_max = 6, 8
bx_wire_min, bx_wire_max = 7, 9
bx_target_comp, bx_target_wire = 7, 8
MEs = [11, 12, 13, 21, 22, 31, 32, 41, 42]

#maxes = {"comp": {11:[],12:[],13:[],21:[],22:[],31:[],32:[],41:[],42:[]}, "wire": {11:[],12:[],13:[],21:[],22:[],31:[],32:[],41:[],42:[]}}
for s in tqdm(sig_files):
	maxes = {"comp": {11:[],12:[],13:[],21:[],22:[],31:[],32:[],41:[],42:[]}, "wire": {11:[],12:[],13:[],21:[],22:[],31:[],32:[],41:[],42:[]}}
	File = TFile("%s/%s.root"%(in_dir,s))
	t = File.Get("MuonNtuplizer/FlatTree")
	nEntries = t.GetEntries()

	for ev in tqdm(range(nEntries),leave=False):
		t.GetEntry(ev)

		if s!="ZeroBias_Data":
			if not t.gen_llp_in_acceptance: continue
			if len(t.gen_llp_in_acceptance) < 2:
				if t.gen_llp_in_acceptance[0]==0: continue
			else:
				if t.gen_llp_in_acceptance[0]==0 and t.gen_llp_in_acceptance[1]==0: continue
	
		chamber = {"comp": {11:[],12:[],13:[],21:[],22:[],31:[],32:[],41:[],42:[]}, "wire": {11:[],12:[],13:[],21:[],22:[],31:[],32:[],41:[],42:[]}}
		for i in range(len(t.csc_comp_station)):
			if t.csc_comp_time[i]<bx_comp_min or t.csc_comp_time[i]>bx_comp_max: continue

			sector = (t.csc_comp_station[i]*10 + t.csc_comp_ring[i])
			if sector not in MEs: continue
			chamber["comp"][sector].append(t.csc_comp_region[i]*(t.csc_comp_station[i]*1000 + t.csc_comp_ring[i]*100 + t.csc_comp_chamber[i]))

		for i in range(len(t.csc_wire_station)):
			if t.csc_wire_time[i]<bx_wire_min or t.csc_wire_time[i]>bx_wire_max: continue

			sector = (t.csc_wire_station[i]*10 + t.csc_wire_ring[i])
			if sector not in MEs: continue
			chamber["wire"][sector].append(t.csc_wire_region[i]*(t.csc_wire_station[i]*1000 + t.csc_wire_ring[i]*100 + t.csc_wire_chamber[i]))

		for me in MEs:
			counts = Counter(chamber["comp"][me])
			if counts.most_common():
				maxes["comp"][me].append(counts.most_common()[0][1])	
			else:
				maxes["comp"][me].append(0)
			
			counts = Counter(chamber["wire"][me])
			if counts.most_common():
				maxes["wire"][me].append(counts.most_common()[0][1])
			else:
				maxes["wire"][me].append(0)

	with open('output/comp%i%i_wire%i%i/maxHits_%s.p'%(bx_comp_min,bx_comp_max,bx_wire_min,bx_wire_max,s), 'wb') as handle:
		pickle.dump(maxes, handle, protocol=pickle.HIGHEST_PROTOCOL)

		
