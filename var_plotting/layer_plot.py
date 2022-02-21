from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as mplcm
import matplotlib.colors as colors
from tqdm import tqdm
import pickle


in_dir = "/eos/uscms/store/user/nimenend/Eff_Rate/Final"
samples = [
"MH_1000_MFF_450_CTau_100000mm",
"MH_125_MFF_12_CTau_9000mm",
"MH_125_MFF_12_CTau_900mm",
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

NUM_COLORS = len(samples)
sectors = [11,12,13,21,22,31,32,41,42]
#sectors = [42]

for me in tqdm(sectors):

	cm = plt.get_cmap('gist_rainbow')
	cNorm  = colors.Normalize(vmin=0, vmax=NUM_COLORS-1)
	scalarMap = mplcm.ScalarMappable(norm=cNorm, cmap=cm)	
	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.set_prop_cycle(color=[scalarMap.to_rgba(i) for i in range(NUM_COLORS)])
	for s in tqdm(samples,leave=False):
		with open ('Plots/pickle/layer/%s_ME%i_comp.p'%(s,me),'rb') as handle:
			times_comp = pickle.load(handle)
		if s == "ZeroBias_Data":
			(n,bins,patches) = ax.hist(times_comp[s]["ME%i"%(me)],bins=14,range=[1,15],density=True,histtype='step',label=s,color='black')
		else:
			(n,bins,patches) = ax.hist(times_comp[s]["ME%i"%(me)],bins=14,range=[1,15],density=True,histtype='step',label=s)
	plt.xlabel("Number of Layers Hit")
	plt.ylabel("Number of Chambers")
	plt.title("Number of Layers Hit in Each Chamber for Comparator in ME%i"%(me))
	plt.yscale('log')
	plt.legend(loc='center right',fontsize='x-small')
	fig.savefig("Plots/layer/Layer_comp_ME%i.png"%(me))
	fig.clf()

	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.set_prop_cycle(color=[scalarMap.to_rgba(i) for i in range(NUM_COLORS)])
	for s in tqdm(samples,leave=False):
		with open ('Plots/pickle/layer/%s_ME%i_wire.p'%(s,me),'rb') as handle:
			times_wire = pickle.load(handle)
		if s == "ZeroBias_Data":
			(n,bins,patches) = ax.hist(times_wire[s]["ME%i"%(me)],bins=14,range=[1,15],density=True,histtype='step',label=s,color='black')
		else:
			(n,bins,patches) = ax.hist(times_wire[s]["ME%i"%(me)],bins=14,range=[1,15],density=True,histtype='step',label=s)
	plt.xlabel("Number of Layers Hit")
	plt.ylabel("Number of Chambers")
	plt.title("Number of Layers Hit in Each Chamber for Wire in ME%i"%(me))
	plt.yscale('log')
	plt.legend(loc='center right',fontsize='x-small')
	fig.savefig("Plots/layer/Layer_wire_ME%i.png"%(me))
	fig.clf()
