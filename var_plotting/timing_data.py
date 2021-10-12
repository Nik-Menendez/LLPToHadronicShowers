from __future__ import division
import numpy as np
#import uproot4
from ROOT import TFile, TTree
import matplotlib.pyplot as plt
from tqdm import tqdm
import pickle

in_dir = "/eos/uscms/store/user/nimenend/Eff_Rate/Final"
samples = [
#"MH_1000_MFF_450_CTau_100000mm",
#"MH_125_MFF_12_CTau_9000mm",
#"MH_125_MFF_12_CTau_900mm",
#"MH_125_MFF_1_CTau_10000mm",
#"MH_125_MFF_1_CTau_1000mm",        
#"MH_125_MFF_1_CTau_5000mm",
#"MH_125_MFF_25_CTau_15000mm",
#"MH_125_MFF_25_CTau_1500mm",
#"MH_125_MFF_50_CTau_30000mm",
#"MH_125_MFF_50_CTau_3000mm",
#"MH_250_MFF_120_CTau_10000mm",
##"MH_250_MFF_120_CTau_1000mm",
#"MH_250_MFF_120_CTau_500mm",
#"MH_250_MFF_60_CTau_10000mm",
#"MH_250_MFF_60_CTau_1000mm",
#"MH_250_MFF_60_CTau_500mm",
#"MH_350_MFF_160_CTau_10000mm",
#"MH_350_MFF_160_CTau_1000mm",
#"MH_350_MFF_160_CTau_500mm",
#"MH_350_MFF_80_CTau_10000mm",
#"MH_350_MFF_80_CTau_1000mm",
#"MH_350_MFF_80_CTau_500mm",
"ZeroBias_Data",
]

vars_in = ["csc_comp_time","csc_comp_station","csc_comp_ring","csc_wire_time","csc_wire_station","csc_wire_ring"]
sectors = [11,12,13,21,22,31,32,41,42]
#sectors = [41,42]
nCham = {"ME11":72,"ME12":72,"ME13":72,"ME21":36,"ME22":72,"ME31":36,"ME32":72,"ME41":36,"ME42":72}

for me in tqdm(sectors):
	times_comp, times_wire = {}, {}
	for s in tqdm(samples,leave=False):
		times_comp[s] = {'ME11':[],'ME12':[],'ME13':[],'ME21':[],'ME22':[],'ME31':[],'ME32':[],'ME41':[],'ME42':[]}
		times_wire[s] = {'ME11':[],'ME12':[],'ME13':[],'ME21':[],'ME22':[],'ME31':[],'ME32':[],'ME41':[],'ME42':[]}
		File = TFile("%s/%s.root"%(in_dir,s))
		t = File.Get("MuonNtuplizer/FlatTree")
		nEntries = t.GetEntries()
	
		for ev in tqdm(range(10000),leave=False):
			t.GetEntry(ev)

			sector_comp, sector_wire = [], []
			for i in range(len(t.csc_comp_station)):
				sector_comp = (t.csc_comp_station[i]*10 + t.csc_comp_ring[i])
				if sector_comp==me:
					times_comp[s]["ME%i"%(me)].append(t.csc_comp_time[i])
			for i in range(len(t.csc_wire_station)):
				sector_wire = (t.csc_wire_station[i]*10 + t.csc_wire_ring[i])
				if sector_wire==me:
					times_wire[s]["ME%i"%(me)].append(t.csc_wire_time[i])

	for s in samples:
		weights = np.ones(len(times_comp[s]["ME%i"%(me)]))*(1/nCham["ME%i"%(me)])
		times_comp[s]["weights"] = weights
		(n,bins,patches) = plt.hist(times_comp[s]["ME%i"%(me)],bins=25,range=[0,25],weights=weights,density=True,histtype='step',label=s)
		with open ('Plots/pickle/%s_ME%i_comp.p'%(s,me),'wb') as handle:
			pickle.dump(times_comp,handle)
	plt.xlabel("BX")
	plt.ylabel("Number of Hits")
	plt.title("BX of Hits for Comparator in ME%i"%(me))
	plt.legend(loc='best')
	plt.savefig("Plots/BX_comp_data_ME%i.png"%(me))
	plt.clf()

	file_wire = open("wire_bins.txt","a")
	file_wire.write("\n")
	file_wire.write("ME%i"%(me))
	for s in samples:
		weights = np.ones(len(times_wire[s]["ME%i"%(me)]))*(1/nCham["ME%i"%(me)])
		times_wire[s]["weights"] = weights
		(n,bins,patches) = plt.hist(times_wire[s]["ME%i"%(me)],bins=25,range=[0,25],weights=weights,density=True,histtype='step',label=s)
		with open ('Plots/pickle/%s_ME%i_wire.p'%(s,me),'wb') as handle:
			pickle.dump(times_wire,handle)
	plt.xlabel("BX")
	plt.ylabel("Number of Hits")
	plt.title("BX of Hits for Wire in ME%i"%(me))
	plt.legend(loc='best')
	plt.savefig("Plots/BX_wire_data_ME%i.png"%(me))
	plt.clf()
