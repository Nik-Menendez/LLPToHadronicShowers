from __future__ import division
import uproot4
import awkward1 as ak
import numpy as np
import sys

in_file = str(sys.argv[1])
debug = False

#print("Getting Efficiency for file "+in_file)
#print("")
sample = in_file.split('_')
HM = (sample[2])
LLPM = (sample[4])
CTau = (sample[6][0:-7])

def get_eff(llp_accept,csc_accept,csc_accept_loose,csc_accept_tight,emtf_accept,emtf_accept_loose,gmt_accept):

	# Create a mask for events in acceptance
	llp_pass = np.array(ak.sum(llp_accept, axis=-1)>0)
	n_acc    = np.count_nonzero(llp_pass)
	if n_acc==0: return [0,0,0,0]

	# Apppply mask to the csc, emtf, and gmt
	csc_pass  = csc_accept[llp_pass]
	emtf_pass = emtf_accept[llp_pass]
	gmt_pass  = gmt_accept[llp_pass]
	csc_pass_loose = csc_accept_loose[llp_pass]
	csc_pass_tight = csc_accept_tight[llp_pass]
	emtf_pass_loose = emtf_accept_loose[llp_pass]	

	# Calculate efficiency for each
	csc_eff  = np.count_nonzero(ak.sum(csc_pass,axis=1))/n_acc*100
	emtf_eff = np.count_nonzero(ak.sum(emtf_pass,axis=1))/n_acc*100
	gmt_eff  = np.count_nonzero((gmt_pass))/n_acc*100
	csc_eff_loose  = np.count_nonzero(ak.sum(csc_pass_loose,axis=1))/n_acc*100
	csc_eff_tight  = np.count_nonzero(ak.sum(csc_pass_tight,axis=1))/n_acc*100
	emtf_eff_loose = np.count_nonzero(ak.sum(emtf_pass_loose,axis=1))/n_acc*100
	csc_eff_2loose = np.count_nonzero(np.array(ak.sum(csc_pass_loose,axis=1)>1))/n_acc*100

	emtf_one = np.array(ak.sum(emtf_pass,axis=1)>0)
	emtf_two = np.array(ak.sum(emtf_pass_loose,axis=1)>0)
	emtf_or = emtf_one | emtf_two
	emtf_eff_or = np.count_nonzero(emtf_or)/n_acc*100

	return [n_acc,csc_eff_loose,csc_eff,csc_eff_tight,csc_eff_2loose,emtf_eff,emtf_eff_loose,emtf_eff_or,gmt_eff]

def get_rate(csc_accept,emtf_accept,gmt_accept):

	# Calculate rate for reach
	n_acc = len(csc_accept)
	csc_rate  = np.count_nonzero(ak.num(csc_accept,axis=1))/n_acc*30*1000
	emtf_rate = np.count_nonzero(ak.num(emtf_accept,axis=1))/n_acc*30*1000
	gmt_rate  = np.count_nonzero(gmt_accept)/n_acc*30*1000

	return [n_acc,csc_rate,emtf_rate,gmt_rate]

def debug_eff(llp_accept,csc_accept,emtf_accept,gmt_accept,csc_endcap,csc_station,csc_ring,csc_chamber,emtf_endcap,emtf_station):
	
	# Create a mask for events in acceptance
	llp_pass = np.array(ak.sum(llp_accept, axis=-1)>0)
	
	# Apppply mask to the csc, emtf, and gmt
	csc_pass  = csc_accept[llp_pass]
	emtf_pass = emtf_accept[llp_pass]
	gmt_pass  = gmt_accept[llp_pass]

	mismatch = ak.num(emtf_pass) > ak.flatten(gmt_pass)*5
	print("Mismatch:")
	print(mismatch)
	print('')

	csc_pass_endcap   = csc_endcap[llp_pass]
	csc_pass_station = csc_station[llp_pass]
	csc_pass_ring    = csc_ring[llp_pass]
	csc_pass_chamber = csc_chamber[llp_pass]

	print("CSC Masked Array:")
	print(csc_pass[mismatch])
	print("CSC endcap:")
	print(csc_pass_endcap[mismatch])
	print("CSC station:")
	print(csc_pass_station[mismatch])
	print("CSC ring:")
	print(csc_pass_ring[mismatch])
	print("CSC chamber:")
	print(csc_pass_chamber[mismatch])
	print("")
	
	emtf_pass_endcap = emtf_endcap[llp_pass]
	emtf_pass_station = emtf_station[llp_pass]

	print("EMTF Masked Array:")
	print(emtf_pass[mismatch])
	print("EMTF endcap:")
	print(emtf_pass_endcap[mismatch])
	print("EMTF sector:")
	print(emtf_pass_station[mismatch])
	print("")

	print("GMT Masked Array:")
	print(gmt_pass[mismatch])
	print("")

	# Calculate efficiency for each
	n_acc    = np.count_nonzero(llp_pass)
	csc_eff  = np.count_nonzero(ak.num(csc_pass,axis=1))/n_acc*100
	emtf_eff = np.count_nonzero(ak.num(emtf_pass,axis=1))/n_acc*100
	gmt_eff  = np.count_nonzero(gmt_pass)/n_acc*100

	return [n_acc,csc_eff,emtf_eff,gmt_eff]

def lct_check(csc_accept,csc_chamber,lct_chamber,alct_chamber,clct_chamber):

	csc_pass = np.array(ak.num(csc_accept,axis=1)>0)
	if np.count_nonzero(csc_pass)==0: return [0,0,0,0]

	csc_cham_pass  = csc_chamber[csc_pass]
	lct_cham_pass  = lct_chamber[csc_pass]
	alct_cham_pass = alct_chamber[csc_pass]
	clct_cham_pass = clct_chamber[csc_pass]

	#print(csc_cham_pass)
	#print(lct_cham_pass)
	#print(alct_cham_pass)
	#print(clct_cham_pass)

	lct_corr=0
	alct_corr=0
	clct_corr=0
	for i in range(len(csc_cham_pass)):
		for j in range(len(csc_cham_pass[i])):
			if csc_cham_pass[i][j] in lct_cham_pass[i]:  lct_corr+=1
			if csc_cham_pass[i][j] in alct_cham_pass[i]: alct_corr+=1
			if csc_cham_pass[i][j] in clct_cham_pass[i]: clct_corr+=1

	total_cham = ak.sum(ak.num(csc_cham_pass))
	lct_eff = lct_corr/total_cham*100
	alct_eff = alct_corr/total_cham*100
	clct_eff = clct_corr/total_cham*100

	return [total_cham,lct_eff,alct_eff,clct_eff]

rate_arg = "eff"#str(sys.argv[1])
find_rate = rate_arg == "rate"
# Open file and tree
tree = uproot4.open(in_file)["MuonNtuplizer"]["FlatTree"]

# Save relevant branches into awkward arrays
if not find_rate: llp_accept  = (tree["gen_llp_in_acceptance"].array())
csc_accept  = (tree["csc_shower_isNominalInTime"].array())
emtf_accept = (tree["emtfshower_isOneNominalInTime"].array())
gmt_accept  = (tree["l1mushower_isOneNominalInTime"].array())
csc_accept_loose = (tree["csc_shower_isLooseInTime"].array())
csc_accept_tight = (tree["csc_shower_isTightInTime"].array())
emtf_accept_loose = (tree["emtfshower_isTwoLooseInTime"].array())
if debug:
	csc_endcap  = tree["csc_shower_region"].array()
	csc_station = tree["csc_shower_station"].array()
	csc_ring    = tree["csc_shower_ring"].array()
	csc_chamber = tree["csc_shower_chamber"].array()
	emtf_endcap = tree["emtfshower_region"].array()
	emtf_station= tree["emtfshower_sector"].array()

if debug: 
	print("LLP_Acceptance array:")
	print(llp_accept)
	print("CSC_Acceptance array:")
	print(csc_accept)
	print("EMTF_Acceptance array:")
	print(emtf_accept)
	print("GMT_Acceptance array:")
	print(gmt_accept)
	print("")

if not debug:
	if find_rate: rates = get_rate(csc_accept,emtf_accept,gmt_accept)
	else: effs = get_eff(llp_accept,csc_accept,csc_accept_loose,csc_accept_tight,emtf_accept,emtf_accept_loose,gmt_accept)
else:
	effs = debug_eff(llp_accept,csc_accept,emtf_accept,gmt_accept,csc_endcap,csc_station,csc_ring,csc_chamber,emtf_endcap,emtf_station)

"""
if find_rate:
	# Print out results
	print("Number of Events: %i"%(rates[0]))
	print("CSC Trigger Rate: %.2f kHz"%(rates[1]))
	print("EMTF Rate: %.2f kHz"%(rates[2]))
	print("GMT Rate: %.2f kHz"%(rates[3]))
else:
	# Print out results
	print("Number of Events with LLP in Acceptance: %i"%(effs[0]))
	print("CSC Trigger Efficiency: %.2f%%" %(effs[1]))
	print("EMTF Efficiency: %.2f%%" %(effs[2]))
	print("GMT Efficiency: %.2f%%" %(effs[3]))
#print("")
"""

csc_chamber  = tree["csc_shower_chamber"].array()
lct_chamber  = tree["csc_lct_chamber"].array()
clct_chamber = tree["csc_clct_chamber"].array()
alct_chamber = tree["csc_alct_chamber"].array()

chams = lct_check(csc_accept,csc_chamber,lct_chamber,clct_chamber,alct_chamber)

#print("Out of %i chambers with CSC showers:"%(chams[0]))
#print("There are LCTs in %.2f%% of chambers"%(chams[1]))
#print("There are ALCTs in %.2f%% of chambers"%(chams[2]))
#print("There are CLCTs in %.2f%% of chambers"%(chams[3]))
#
#print("*************************************************************************")

print("%s,%s,%s,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%"%(HM,LLPM,CTau,effs[1],effs[2],effs[3],effs[4],effs[5],effs[6],effs[7],effs[8],chams[1],chams[2],chams[3]))
