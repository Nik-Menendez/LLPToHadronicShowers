from __future__ import division
import numpy as np
import uproot
import matplotlib.pyplot as plt
from tqdm import tqdm
import pickle

in_dir = "/eos/uscms/store/user/nimenend/Eff_Rate/Final"
samples = [
#"MH_1000_MFF_450_CTau_100000mm",
"MH_125_MFF_12_CTau_9000mm",
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
]

vars_in = ["csc_comp_time","csc_comp_station","csc_comp_ring","csc_wire_time","csc_wire_station","csc_wire_ring","gen_llp_in_acceptance","csc_comp_layer","csc_wire_layer"]
sectors = [11,12,13,21,22,31,32,41,42]
#sectors = [41,42]
nCham = {"ME11":72,"ME12":72,"ME13":72,"ME21":36,"ME22":72,"ME31":36,"ME32":72,"ME41":36,"ME42":72}

for me in tqdm(sectors):
	layer_comp, layer_wire = {}, {}
	for s in tqdm(samples,leave=False):
		layer_comp[s] = {'ME11':[],'ME12':[],'ME13':[],'ME21':[],'ME22':[],'ME31':[],'ME32':[],'ME41':[],'ME42':[]}
		layer_wire[s] = {'ME11':[],'ME12':[],'ME13':[],'ME21':[],'ME22':[],'ME31':[],'ME32':[],'ME41':[],'ME42':[]}
		tree = uproot.open("%s/%s.root"%(in_dir,s))["MuonNtuplizer"]["FlatTree"]
	
		data = tree.arrays(vars_in)
	
		sector_comp = data["csc_comp_station"]*10 + data["csc_comp_ring"]
		sector_wire = data["csc_wire_station"]*10 + data["csc_wire_ring"]
	
		for ev in tqdm(range(len(data["csc_comp_time"])),leave=False):
			if not (np.count_nonzero(data["gen_llp_in_acceptance"][ev])>=1): continue

			layer = (np.take(data["csc_comp_time"][ev],np.argwhere(sector_comp[ev]==me).flatten())).flatten().tolist()
			layer_comp[s]["ME%i"%(me)].extend(layer)
			layer = (np.take(data["csc_wire_time"][ev],np.argwhere(sector_wire[ev]==me).flatten())).flatten().tolist()
			layer_wire[s]["ME%i"%(me)].extend(layer)

			

	for s in samples:
		weights = np.ones(len(layer_comp[s]["ME%i"%(me)]))*(1/nCham["ME%i"%(me)])
		layer_comp[s]["weights"] = weights
		(n,bins,patches) = plt.hist(layer_comp[s]["ME%i"%(me)],bins=25,range=[0,25],weights=weights,density=False,histtype='step',label=s)
		with open('Plots/pickle/%s_ME%i_comp.p'%(s,me),'wb') as handle:
			pickle.dump(layer_comp,handle)
		for x in n:
			file_comp.write("%.5f, "%(x))
	plt.xlabel("BX")
	plt.ylabel("Number of Hits")
	plt.title("BX of Hits for Comparator in ME%i"%(me))
	#plt.legend(loc='best')
	plt.savefig("Plots/BX_comp_ME%i.png"%(me))
	plt.clf()

	for s in samples:
		weights = np.ones(len(layer_wire[s]["ME%i"%(me)]))*(1/nCham["ME%i"%(me)])
		layer_wire[s]["weights"] = weights
		(n,bins,patches) = plt.hist(layer_wire[s]["ME%i"%(me)],bins=25,range=[0,25],weights=weights,density=False,histtype='step',label=s)
		with open('Plots/pickle/%s_ME%i_wire.p'%(s,me),'wb') as handle:
			pickle.dump(layer_wire,handle)
		for x in n:
			file_wire.write("%.5f, "%(x))
	plt.xlabel("BX")
	plt.ylabel("Number of Hits")
	plt.title("BX of Hits for Wire in ME%i"%(me))
	#plt.legend(loc='best')
	plt.savefig("Plots/BX_wire_ME%i.png"%(me))
	plt.clf()
