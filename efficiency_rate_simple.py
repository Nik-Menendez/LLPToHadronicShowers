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

def get_eff(llp_accept,csc_accept,csc_accept_loose,csc_accept_tight,csc_ring):

	# Create a mask for events in acceptance
	if not find_rate: 
		llp_pass = np.array(ak.sum(llp_accept, axis=-1)>=nllp1)
		llp_pass2= np.array(ak.sum(llp_accept, axis=-1)>=nllp2)
	else: llp_pass = True

	# Apppply mask to the csc, emtf, and gmt
	if not find_rate:
		csc_pass  = csc_accept[llp_pass]
		csc_pass_loose = csc_accept_loose[llp_pass]
		csc_pass_tight = csc_accept_tight[llp_pass]
		csc_pass_ring = csc_ring[llp_pass]
	else:
		csc_pass  = csc_accept
		csc_pass_loose = csc_accept_loose
		csc_pass_tight = csc_accept_tight
		csc_pass_ring = csc_ring
	n_acc = len(csc_pass)

	new_nom = [None] * len(csc_pass_ring)
	new_loose = [None] * len(csc_pass_ring)
	new_tight = [None] * len(csc_pass_ring)

	for i in range(len(csc_pass_ring)):
		new_ring = csc_pass_ring[i] == 1
		new_nom[i] = csc_pass[i]*new_ring
		new_loose[i] = csc_pass_loose[i]*new_ring
		new_tight[i] = csc_pass_tight[i]*new_ring
			
	awk_nom = ak.Array(new_nom)
	awk_loose = ak.Array(new_loose)
	awk_tight = ak.Array(new_tight)

	# Calculate efficiency for each
	csc_eff  = np.count_nonzero(ak.sum(csc_pass,axis=1))/n_acc
	csc_eff_loose  = np.count_nonzero(ak.sum(csc_pass_loose,axis=1))/n_acc
	csc_eff_tight  = np.count_nonzero(ak.sum(csc_pass_tight,axis=1))/n_acc
	csc_eff1  = np.count_nonzero(ak.sum(awk_nom,axis=1))/n_acc
	csc_eff_loose1  = np.count_nonzero(ak.sum(awk_loose,axis=1))/n_acc
	csc_eff_tight1  = np.count_nonzero(ak.sum(awk_tight,axis=1))/n_acc
	return [n_acc,csc_eff_loose,csc_eff_loose1,csc_eff,csc_eff1,csc_eff_tight,csc_eff_tight1]

# Open file and tree
tree = uproot4.open(in_file)["MuonNtuplizer"]["FlatTree"]

# Save relevant branches for Efficiency calculation into awkward arrays
if not find_rate: llp_accept  = (tree["gen_llp_in_acceptance"].array())
else: llp_accept = True
csc_accept  = (tree["csc_shower_isNominalInTime"].array())
csc_accept_loose = (tree["csc_shower_isLooseInTime"].array())
csc_accept_tight = (tree["csc_shower_isTightInTime"].array())
csc_ring = tree["csc_shower_ring"].array()

# Calculate efficiencies
effs = get_eff(llp_accept,csc_accept,csc_accept_loose,csc_accept_tight,csc_ring)

# Free up Memory
llp_accept, csc_accept_loose, csc_accept_tight, csc_ring = None, None, None, None

if not find_rate: print("%s,%s,%s,%i,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%"%(HM,LLPM,CTau,effs[0],effs[1]*100,effs[2]*100,effs[3]*100,effs[4]*100,effs[5]*100,effs[6]*100))
else: print("%s,%s,%s,%i,%.2f kHz,%.2f kHZ,%.2f kHz,%.2f kHz,%.2f kHZ,%.2f kHz"%(HM,LLPM,CTau,effs[0],effs[1]*30000,effs[2]*30000,effs[3]*30000,effs[4]*30000,effs[5]*30000,effs[6]*30000))
