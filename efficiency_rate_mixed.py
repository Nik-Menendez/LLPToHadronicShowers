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

def get_eff(llp_accept,csc_accept,csc_accept_loose,csc_accept_tight,csc_ring,csc_acceptA,csc_accept_looseA,csc_accept_tightA,csc_ringA):

	# Create a mask for events in acceptance
	if not find_rate: 
		llp_pass = np.array(ak.sum(llp_accept, axis=-1)>=nllp1)
	else: llp_pass = True

	# Apppply mask to the csc, emtf, and gmt
	if not find_rate:
		csc_pass  = csc_accept[llp_pass]
		csc_pass_loose = csc_accept_loose[llp_pass]
		csc_pass_tight = csc_accept_tight[llp_pass]
		csc_pass_ring = csc_ring[llp_pass]
		csc_passA  = csc_acceptA[llp_pass]
		csc_pass_looseA = csc_accept_looseA[llp_pass]
		csc_pass_tightA = csc_accept_tightA[llp_pass]
		csc_pass_ringA = csc_ringA[llp_pass]
	else:
		csc_pass  = csc_accept
		csc_pass_loose = csc_accept_loose
		csc_pass_tight = csc_accept_tight
		csc_pass_ring = csc_ring
		csc_passA  = csc_acceptA
		csc_pass_looseA = csc_accept_looseA
		csc_pass_tightA = csc_accept_tightA
		csc_pass_ringA = csc_ringA
	n_acc = len(csc_pass)

	new_nom1   = [None] * len(csc_pass_ring)
	new_loose1 = [None] * len(csc_pass_ring)
	new_tight1 = [None] * len(csc_pass_ring)
	new_nom2   = [None] * len(csc_pass_ring)
	new_loose2 = [None] * len(csc_pass_ring)
	new_tight2 = [None] * len(csc_pass_ring)
	new_nomM   = [None] * len(csc_pass_ring)
	new_looseM = [None] * len(csc_pass_ring)
	new_tightM = [None] * len(csc_pass_ring)

	for i in range(len(csc_pass_ring)):
		ring1 = csc_pass_ring[i] == 1
		ring2 = csc_pass_ringA[i] > 1

		new_nom1[i] = csc_pass[i]*ring1
		new_loose1[i] = csc_pass_loose[i]*ring1
		new_tight1[i] = csc_pass_tight[i]*ring1
		
		new_nom2[i] = csc_passA[i]*ring2
		new_loose2[i] = csc_pass_looseA[i]*ring2
		new_tight2[i] = csc_pass_tightA[i]*ring2

		new_nomM[i] = [None] * len(new_nom2[i])
		new_looseM[i] = [None] * len(new_nom2[i])
		new_tightM[i] = [None] * len(new_nom2[i])

		for j in range(len(new_nom2[i])):
			if j < len(new_nom1[i]):
				new_nomM[i][j] = (new_nom1[i][j] + new_nom2[i][j])
				new_looseM[i][j] = (new_loose1[i][j] + new_loose2[i][j])
				new_tightM[i][j] = (new_tight1[i][j] + new_tight2[i][j])
			else:
				new_nomM[i][j] = (new_nom2[i][j])
				new_looseM[i][j] = (new_loose2[i][j])
				new_tightM[i][j] = (new_tight2[i][j])

	awk_nom1 = ak.Array(new_nom1)
	awk_loose1 = ak.Array(new_loose1)
	awk_tight1 = ak.Array(new_tight1)
	awk_nomM = ak.Array(new_nomM)
	awk_looseM = ak.Array(new_looseM)
	awk_tightM = ak.Array(new_tightM)

	# Calculate efficiency for each
	csc_eff  = np.count_nonzero(ak.sum(csc_pass,axis=1))/n_acc
	csc_eff_loose  = np.count_nonzero(ak.sum(csc_pass_loose,axis=1))/n_acc
	csc_eff_tight  = np.count_nonzero(ak.sum(csc_pass_tight,axis=1))/n_acc
	csc_eff1  = np.count_nonzero(ak.sum(awk_nom1,axis=1))/n_acc
	csc_eff_loose1  = np.count_nonzero(ak.sum(awk_loose1,axis=1))/n_acc
	csc_eff_tight1  = np.count_nonzero(ak.sum(awk_tight1,axis=1))/n_acc
	csc_effM  = np.count_nonzero(ak.sum(awk_nomM,axis=1))/n_acc
	csc_eff_looseM  = np.count_nonzero(ak.sum(awk_looseM,axis=1))/n_acc
	csc_eff_tightM  = np.count_nonzero(ak.sum(awk_tightM,axis=1))/n_acc
	return [n_acc,csc_eff_loose,csc_eff_loose1,csc_eff_looseM,csc_eff,csc_eff1,csc_effM,csc_eff_tight,csc_eff_tight1,csc_eff_tightM]

# Open file and tree
tree = uproot4.open(in_file)["MuonNtuplizer"]["FlatTree"]

# Save relevant branches for Efficiency calculation into awkward arrays
if not find_rate: llp_accept  = (tree["gen_llp_in_acceptance"].array())
else: llp_accept = True
csc_accept  = (tree["csc_shower_isNominalInTime"].array())
csc_accept_loose = (tree["csc_shower_isLooseInTime"].array())
csc_accept_tight = (tree["csc_shower_isTightInTime"].array())
csc_ring = tree["csc_shower_ring"].array()

# Open file and tree
tree = uproot4.open(in_file)["MuonNtuplizerAnod"]["FlatTree"]

# Save relevant branches for Efficiency calculation into awkward arrays
csc_acceptA  = (tree["csc_shower_isNominalInTime"].array())
csc_accept_looseA = (tree["csc_shower_isLooseInTime"].array())
csc_accept_tightA = (tree["csc_shower_isTightInTime"].array())
csc_ringA = tree["csc_shower_ring"].array()

# Calculate efficiencies
effs = get_eff(llp_accept,csc_accept,csc_accept_loose,csc_accept_tight,csc_ring,csc_acceptA,csc_accept_looseA,csc_accept_tightA,csc_ringA)

# Free up Memory
llp_accept, csc_accept_loose, csc_accept_tight, csc_ring, csc_accept_looseA, csc_accept_tightA, csc_ringA = None, None, None, None, None, None, None

if not find_rate: print("%s,%s,%s,%i,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%,%.2f%%"%(HM,LLPM,CTau,effs[0],effs[1]*100,effs[2]*100,effs[3]*100,effs[4]*100,effs[5]*100,effs[6]*100,effs[7]*100,effs[8]*100,effs[9]*100))
else: print("%s,%s,%s,%i,%.2f kHz,%.2f kHZ,%.2f kHz,%.2f kHz,%.2f kHZ,%.2f kHz,%.2f kHz,%.2f kHZ,%.2f kHz"%(HM,LLPM,CTau,effs[0],effs[1]*30000,effs[2]*30000,effs[3]*30000,effs[4]*30000,effs[5]*30000,effs[6]*30000,effs[7]*30000,effs[8]*30000,effs[9]*30000))
