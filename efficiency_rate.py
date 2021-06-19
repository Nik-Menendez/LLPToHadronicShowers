from __future__ import division
import uproot4
import awkward1 as ak
import numpy as np
import sys
from collections import Counter

in_file = str(sys.argv[1])
find_rate = False
if "Data" in in_file: find_rate = True

#print("Getting Efficiency for file "+in_file)
#print("")
if not find_rate:
	sample = in_file.split('_')
	HM = (sample[2])
	LLPM = (sample[4])
	CTau = (sample[6][0:-7])
else:
	HM = "Zero"
	LLPM = "Bias"
	CTau = "Data"

def get_eff(llp_accept,csc_accept,csc_accept_loose,csc_accept_tight,emtf_accept,emtf_accept_loose,gmt_accept,csc_sector,emtf_sector):

	# Create a mask for events in acceptance
	llp_pass = np.array(ak.sum(llp_accept, axis=-1)>0)
	#n_acc    = np.count_nonzero(llp_pass)
	#if n_acc==0: return [0,0,0,0]

	# Apppply mask to the csc, emtf, and gmt
	csc_pass  = csc_accept[llp_pass]
	emtf_pass = emtf_accept[llp_pass]
	gmt_pass  = gmt_accept[llp_pass]
	csc_pass_loose = csc_accept_loose[llp_pass]
	csc_pass_tight = csc_accept_tight[llp_pass]
	emtf_pass_loose = emtf_accept_loose[llp_pass]	
	n_acc = len(csc_pass)

	# Calculate efficiency for each
	csc_eff  = np.count_nonzero(ak.sum(csc_pass,axis=1))/n_acc
	emtf_eff = np.count_nonzero(ak.sum(emtf_pass,axis=1))/n_acc
	gmt_eff  = np.count_nonzero((gmt_pass))/n_acc
	csc_eff_loose  = np.count_nonzero(ak.sum(csc_pass_loose,axis=1))/n_acc
	csc_eff_tight  = np.count_nonzero(ak.sum(csc_pass_tight,axis=1))/n_acc
	emtf_eff_loose = np.count_nonzero(ak.sum(emtf_pass_loose,axis=1))/n_acc
	#csc_eff_2loose = np.count_nonzero(np.array(ak.sum(csc_pass_loose,axis=1)>1))/n_acc
	csc_avail = (csc_sector[llp_pass][ak.sum(csc_pass_loose,axis=1)>1])
	csc_2loose = np.zeros(len(csc_avail))
	i=0
	for x in csc_avail:
		a = np.array(x[np.array(csc_pass_loose[ak.sum(csc_pass_loose,axis=1)>1][i]>0)])
		u, c = np.unique(a, return_counts=True)
		if np.count_nonzero(c)>0: csc_2loose[i]=np.max(c)
		else: csc_2loose[i]=0
		i+=1
	csc_eff_2loose = np.count_nonzero(csc_2loose>1)/n_acc
	#if np.count_nonzero(csc_2loose>1) != np.count_nonzero(ak.sum(emtf_pass_loose,axis=1)): 
	#	print("Mismatch")
	#	#print(np.array((csc_2loose>1)))
	#	#print(np.array((ak.sum(emtf_pass_loose[ak.sum(csc_pass_loose,axis=1)>1],axis=1)))>0)
	#	index = np.where(np.equal(np.array((csc_2loose>1)),np.array((ak.sum(emtf_pass_loose[ak.sum(csc_pass_loose,axis=1)>1],axis=1)))>0)==False)[0]
	#	print(index[0])
	#	print("CSC Sectors with shower:")
	#	print(csc_avail[index[0]])
	#	print("CSC 1nom for the event:")
	#	print(csc_pass[ak.sum(csc_pass_loose,axis=1)>1][index[0]])
	#	print("CSC loose for the event:")
	#	print(csc_pass_loose[ak.sum(csc_pass_loose,axis=1)>1][index[0]])
	#	print("EMTF Sectors with shower:")
	#	print(emtf_sector[llp_pass][ak.sum(csc_pass_loose,axis=1)>1][index[0]])
	#	print("EMTF 2loose for the event:")
	#	print(emtf_pass_loose[ak.sum(csc_pass_loose,axis=1)>1][index[0]])
	#	print("EMTF 1nom for the event:")
	#	print(emtf_pass[ak.sum(csc_pass_loose,axis=1)>1][index[0]])

	emtf_one = np.array(ak.sum(emtf_pass,axis=1)>0)
	emtf_two = np.array(ak.sum(emtf_pass_loose,axis=1)>0)
	emtf_or = emtf_one | emtf_two
	emtf_eff_or = np.count_nonzero(emtf_or)/n_acc

	return [n_acc,csc_eff_loose,csc_eff,csc_eff_tight,csc_eff_2loose,emtf_eff,emtf_eff_loose,emtf_eff_or,gmt_eff]

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

# Open file and tree
tree = uproot4.open(in_file)["MuonNtuplizer"]["FlatTree"]

# Save relevant branches into awkward arrays
if not find_rate: llp_accept  = (tree["gen_llp_in_acceptance"].array())
else: llp_accept = True
csc_accept  = (tree["csc_shower_isNominalInTime"].array())
emtf_accept = (tree["emtfshower_isOneNominalInTime"].array())
gmt_accept  = (tree["l1mushower_isOneNominalInTime"].array())
csc_accept_loose = (tree["csc_shower_isLooseInTime"].array())
csc_accept_tight = (tree["csc_shower_isTightInTime"].array())
emtf_accept_loose = (tree["emtfshower_isTwoLooseInTime"].array())
csc_sector = (tree["csc_shower_sector"].array())
emtf_sector = tree["emtfshower_sector"].array()

effs = get_eff(llp_accept,csc_accept,csc_accept_loose,csc_accept_tight,emtf_accept,emtf_accept_loose,gmt_accept,csc_sector,emtf_sector)

csc_chamber  = tree["csc_shower_chamber"].array()
lct_chamber  = tree["csc_lct_chamber"].array()
clct_chamber = tree["csc_clct_chamber"].array()
alct_chamber = tree["csc_alct_chamber"].array()

chams = lct_check(csc_accept,csc_chamber,lct_chamber,clct_chamber,alct_chamber)

if not find_rate: print("%s,%s,%s,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%"%(HM,LLPM,CTau,effs[1]*100,effs[2]*100,effs[3]*100,effs[4]*100,effs[5]*100,effs[6]*100,effs[7]*100,effs[8]*100,chams[1],chams[2],chams[3]))
else: print("%s,%s,%s,%.2f kHz,%.2f kHZ,%.2f kHZ,%.2f kHZ,%.2f kHZ,%.2f kHZ,%.2f kHZ,%.2f kHz,%.2f%%,%.2f%%,%.2f%%"%(HM,LLPM,CTau,effs[1]*30000,effs[2]*30000,effs[3]*30000,effs[4]*30000,effs[5]*30000,effs[6]*30000,effs[7]*30000,effs[8]*30000,chams[1],chams[2],chams[3]))
