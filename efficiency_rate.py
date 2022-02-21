from __future__ import division
import uproot4
import awkward1 as ak
import numpy as np
import sys
from collections import Counter

in_file = str(sys.argv[1])
#in_file = "root://cmsxrootd.fnal.gov/%s"%(in_file[10:])
find_rate = False
if "Data" in in_file: find_rate = True

nllp1=1
nllp2=1

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
	if not find_rate: 
		llp_pass = np.array(ak.sum(llp_accept, axis=-1)>=nllp1)
		llp_pass2= np.array(ak.sum(llp_accept, axis=-1)>=nllp2)
	else: llp_pass = True
	#n_acc    = np.count_nonzero(llp_pass)
	#if n_acc==0: return [0,0,0,0]

	# Apppply mask to the csc, emtf, and gmt
	if not find_rate:
		csc_pass  = csc_accept[llp_pass]
		emtf_pass = emtf_accept[llp_pass]
		gmt_pass  = gmt_accept[llp_pass]
		csc_pass_loose = csc_accept_loose[llp_pass]
		csc_pass_loose2= csc_accept_loose[llp_pass2]
		csc_pass_tight = csc_accept_tight[llp_pass]
		emtf_pass_loose = emtf_accept_loose[llp_pass2]
		csc_avail = (csc_sector[llp_pass2][ak.sum(csc_pass_loose2,axis=1)>1])
	else:
		csc_pass  = csc_accept
		emtf_pass = emtf_accept
		gmt_pass  = gmt_accept
		csc_pass_loose = csc_accept_loose
		csc_pass_loose2= csc_accept_loose
		csc_pass_tight = csc_accept_tight
		emtf_pass_loose = emtf_accept_loose
		csc_avail = (csc_sector[ak.sum(csc_pass_loose2,axis=1)>1])
	n_acc = len(csc_pass)
	n_acc2= len(csc_pass_loose2)

	# Calculate efficiency for each
	csc_eff  = np.count_nonzero(ak.sum(csc_pass,axis=1))/n_acc
	emtf_eff = np.count_nonzero(ak.sum(emtf_pass,axis=1))/n_acc
	gmt_eff  = np.count_nonzero((gmt_pass))/n_acc
	csc_eff_loose  = np.count_nonzero(ak.sum(csc_pass_loose,axis=1))/n_acc
	csc_eff_tight  = np.count_nonzero(ak.sum(csc_pass_tight,axis=1))/n_acc
	emtf_eff_loose = np.count_nonzero(ak.sum(emtf_pass_loose,axis=1))/n_acc2
	csc_2loose = np.zeros(len(csc_avail))
	i=0
	for x in csc_avail:
		a = np.array(x[np.array(csc_pass_loose2[ak.sum(csc_pass_loose2,axis=1)>1][i]>0)])
		u, c = np.unique(a, return_counts=True)
		if np.count_nonzero(c)>0: csc_2loose[i]=np.max(c)
		else: csc_2loose[i]=0
		i+=1
	#csc_2loose = ak.sum(csc_pass_loose2,axis=1) #Allow 2 loose showers anywhere
	csc_eff_2loose = np.count_nonzero(csc_2loose>1)/n_acc2

	emtf_one = np.array(ak.sum(emtf_pass,axis=1)>0)
	emtf_two = np.array(ak.sum(emtf_pass_loose,axis=1)>0)
	emtf_or = emtf_one | emtf_two
	emtf_eff_or = np.count_nonzero(emtf_or)/n_acc

	return [n_acc,csc_eff_loose,csc_eff,csc_eff_tight,csc_eff_2loose,emtf_eff,emtf_eff_loose,emtf_eff_or,gmt_eff]
	#return [n_acc,csc_eff_loose,csc_eff,csc_eff_2loose,emtf_eff,emtf_eff_loose,emtf_eff_or,gmt_eff]

# Open file and tree
tree = uproot4.open(in_file)["MuonNtuplizerAnod"]["FlatTree"]

# Save relevant branches for Efficiency calculation into awkward arrays
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

# Calculate efficiencies
effs = get_eff(llp_accept,csc_accept,csc_accept_loose,csc_accept_tight,emtf_accept,emtf_accept_loose,gmt_accept,csc_sector,emtf_sector)

# Free up Memory
llp_accept, emtf_accept, gmt_accept, csc_accept_loose, csc_accept_tight, emtf_accept_loose, csc_sector, emtf_sector = None, None, None, None, None, None, None, None

# Print results
if not find_rate: print("%s,%s,%s,%i,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%"%(HM,LLPM,CTau,effs[0],effs[1]*100,effs[2]*100,effs[3]*100,effs[4]*100,effs[5]*100,effs[6]*100,effs[7]*100))
else: print("%s,%s,%s,%i,%.2f kHz,%.2f kHZ,%.2f kHz,%.2f kHZ,%.2f kHZ,%.2f kHZ,%.2f kHZ"%(HM,LLPM,CTau,effs[0],effs[1]*30000,effs[2]*30000,effs[3]*30000,effs[4]*30000,effs[5]*30000,effs[6]*30000,effs[7]*30000))
