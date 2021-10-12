from __future__ import division
import numpy as np
#import uproot4
from ROOT import TFile, TTree
import matplotlib.pyplot as plt
from tqdm import tqdm
import pickle
from numba import njit
import time
from collections import Counter

in_dir = "/eos/uscms/store/user/nimenend/Eff_Rate/Final"
samples = [
#"MH_1000_MFF_450_CTau_100000mm",
#"MH_125_MFF_12_CTau_9000mm",
#"MH_125_MFF_12_CTau_900mm",
"MH_125_MFF_1_CTau_10000mm",
#"MH_125_MFF_1_CTau_1000mm",        
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

def get_nLayers2(sector, csc_layer, csc_time, BX):
	out_layers = {11:[],12:[],13:[],21:[],22:[],31:[],32:[],41:[],42:[]}
	test = [11,12,13,21,22,31,32,41,42]

	if len(BX)>1:
		sector = sector[(csc_time==BX[0])|(csc_time==BX[1])|(csc_time==BX[2])]
		layer = csc_layer[(csc_time==BX[0])|(csc_time==BX[1])|(csc_time==BX[2])]
		thresh = {11:100,12:55,13:20,21:35,22:29,31:35,32:25,41:40,42:30}
	else:
		sector = sector[csc_time==BX[0]]
		layer = csc_layer[csc_time==BX[0]]
		thresh = {11:140,12:56,13:22,21:55,22:34,31:74,32:27,41:86,42:67}

	ME = temp = np.abs(sector/100).astype(np.int_)
	shower = Counter(sector)
	shower_num = shower.most_common()
	with_shower = []
	for i in range(len(shower_num)):
		if abs(shower_num[i][0]/100).astype(int) not in test: continue
		if shower_num[i][1]>thresh[abs(shower_num[i][0]/100).astype(int)]:
			with_shower.append(shower_num[i][0])

	shower_mask = np.in1d(sector,with_shower)
	sector = sector[shower_mask]
	ME = ME[shower_mask]
	layer = layer[shower_mask]

	for me in out_layers:
		sec_check = ME==me
		sector_me = sector[sec_check]
		layer_me = layer[sec_check]

		temp, indexes, counts = (np.unique(sector_me,return_index=True,return_counts=True))
		for i in range(len(indexes)):
			out_layers[me].append(len(set(layer_me[indexes[i]:indexes[i]+counts[i]])))

	return out_layers
	

vars_in = ["csc_comp_time","csc_comp_station","csc_comp_ring","csc_comp_layer","csc_comp_region","csc_comp_chamber",
	   "csc_wire_time","csc_wire_station","csc_wire_ring","csc_wire_layer","csc_wire_region","csc_wire_chamber",]
sectors = [11,12,13,21,22,31,32,41,42]
#sectors = [41,42]
nCham = {"ME11":72,"ME12":72,"ME13":72,"ME21":36,"ME22":72,"ME31":36,"ME32":72,"ME41":36,"ME42":72}
comp_BX = [6,7,8]
wire_BX = [8]

for s in tqdm(samples):
	layer_comp, layer_wire = {}, {}
	layer_comp[s] = {'ME11':[],'ME12':[],'ME13':[],'ME21':[],'ME22':[],'ME31':[],'ME32':[],'ME41':[],'ME42':[]}
	layer_wire[s] = {'ME11':[],'ME12':[],'ME13':[],'ME21':[],'ME22':[],'ME31':[],'ME32':[],'ME41':[],'ME42':[]}
	File = TFile("%s/%s.root"%(in_dir,s))
	t = File.Get("MuonNtuplizer/FlatTree")
	nEntries = t.GetEntries()
	if "Data" in s:
		nEntries = 100000
	else:
		vars_in = vars_in + ["gen_llp_in_acceptance"]
	#nEntries = 1000

	t.SetBranchStatus("*",0)
	for var in vars_in:
		t.SetBranchStatus(var,1)
	
	for ev in tqdm(range(nEntries),leave=False):
		t.GetEntry(ev)

		if "Data" not in s:
			if not (np.count_nonzero(t.gen_llp_in_acceptance)>=1): continue

		csc_station, csc_ring, csc_chamber, csc_region = np.empty(len(t.csc_comp_station)), np.empty(len(t.csc_comp_ring)), np.empty(len(t.csc_comp_chamber)), np.empty(len(t.csc_comp_region))
		csc_time, csc_layer = np.empty(len(t.csc_comp_time)), np.empty(len(t.csc_comp_time))
		for i in range(len(t.csc_comp_time)):
			csc_station[i] = t.csc_comp_station[i]
			csc_ring[i] = t.csc_comp_ring[i]
			csc_chamber[i] = t.csc_comp_chamber[i]
			csc_region[i] = t.csc_comp_region[i]
			csc_time[i] = (t.csc_comp_time[i])
			csc_layer[i] = (t.csc_comp_layer[i])
		sector = (csc_station*1000 + csc_ring*100 + csc_chamber)*csc_region
		out_layer = get_nLayers2(sector,csc_layer,csc_time,comp_BX)
		for me in sectors:
			layer_comp[s]["ME%i"%(me)].extend(out_layer[me])

			
		csc_station, csc_ring, csc_chamber, csc_region = np.empty(len(t.csc_wire_station)), np.empty(len(t.csc_wire_ring)), np.empty(len(t.csc_wire_chamber)), np.empty(len(t.csc_wire_region))
		csc_time, csc_layer = np.empty(len(t.csc_wire_time)), np.empty(len(t.csc_wire_time))
		for i in range(len(t.csc_wire_time)):
			csc_station[i] = t.csc_wire_station[i]
			csc_ring[i] = t.csc_wire_ring[i]
			csc_chamber[i] = t.csc_wire_chamber[i]
			csc_region[i] = t.csc_wire_region[i]
			csc_time[i] = (t.csc_wire_time[i])
			csc_layer[i] = (t.csc_wire_layer[i])
		sector = (csc_station*1000 + csc_ring*100 + csc_chamber)*csc_region
		out_layer = get_nLayers2(sector,csc_layer,csc_time,wire_BX)
		for me in sectors:
			layer_wire[s]["ME%i"%(me)].extend(out_layer[me])

	File.Close()
	for me in tqdm(sectors,leave=False):
		with open ('Plots/pickle/layer/%s_ME%i_comp.p'%(s,me),'wb') as handle:
			pickle.dump(layer_comp,handle,protocol=pickle.HIGHEST_PROTOCOL)

		with open ('Plots/pickle/layer/%s_ME%i_wire.p'%(s,me),'wb') as handle:
                        pickle.dump(layer_wire,handle,protocol=pickle.HIGHEST_PROTOCOL)

