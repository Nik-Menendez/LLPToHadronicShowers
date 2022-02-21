from __future__ import division
import uproot4
import awkward1 as ak
import numpy as np
import sys
from collections import Counter

in_file = str(sys.argv[1])
#in_file = "root://cmsxrootd.fnal.gov/%s"%(in_file[10:])
find_rate = True

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

def get_eff(llp_accept,emtf_accept,run,lumi,event):

	# Create a mask for events in acceptance
	if not find_rate: 
		llp_pass = np.array(ak.sum(llp_accept, axis=-1)>=nllp1)
		llp_pass2= np.array(ak.sum(llp_accept, axis=-1)>=nllp2)
	else: llp_pass = True
	#n_acc    = np.count_nonzero(llp_pass)
	#if n_acc==0: return [0,0,0,0]

	# Apppply mask to the csc, emtf, and gmt
	if not find_rate:
		emtf_pass = emtf_accept[llp_pass]
	else:
		emtf_pass = emtf_accept
	n_acc = len(emtf_pass)
	n_acc2= len(emtf_pass)

	# Calculate efficiency for each
	emtf_eff = np.count_nonzero(ak.sum(emtf_pass,axis=1))/n_acc

	emtf_mask = ak.sum(emtf_pass,axis=1)>0
	end_run =   ak.flatten(run[emtf_mask])
	end_lumi =  ak.flatten(lumi[emtf_mask])
	end_event = ak.flatten(event[emtf_mask])

	return [n_acc,emtf_eff,end_run,end_lumi,end_event]

# Open file and tree
tree = uproot4.open(in_file)["MuonNtuplizer"]["FlatTree"]

# Save relevant branches for Efficiency calculation into awkward arrays
if not find_rate: llp_accept  = (tree["gen_llp_in_acceptance"].array())
else: llp_accept = True
emtf_accept = (tree["emtfshower_isOneNominalInTime"].array())
event = tree["event_event"].array()
run = tree["event_run"].array()
lumi = tree["event_lumi"].array()

# Calculate efficiencies
effs = get_eff(llp_accept,emtf_accept,run,lumi,event)

f = open("passing_events.txt","a")
for i in range(len(effs[2])):
	f.write("%i:%i:%i\n"%(effs[2][i],effs[3][i],effs[4][i]))
f.close()

f = open("Rate_count.csv","a")
f.write("%i,%i\n"%(effs[0],len(effs[2])))
f.close()

# Print results
