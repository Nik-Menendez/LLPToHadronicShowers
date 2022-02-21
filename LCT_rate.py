from __future__ import division
import uproot4
import awkward1 as ak
import numpy as np
import sys
from tqdm import tqdm
from numba import njit

in_file = "/eos/uscms/store/user/nimenend/Eff_Rate/Final/ZeroBias_Data.root"
#in_file = "root://cmsxrootd.fnal.gov//store/user/nimenend/Eff_Rate/Final/ZeroBias_Data.root"
#in_file = "/eos/uscms/store/user/nimenend/Eff_Rate/Final/MH_125_MFF_12_CTau_9000mm.root"
#in_file = "root://cmsxrootd.fnal.gov//store/user/nimenend/Eff_Rate/Final/MH_125_MFF_12_CTau_900mm.root"

@njit
def get_rate(chambers):
	types = [11,12,13,21,22,31,32,41,42]
	passes={11:0,12:0,13:0,21:0,22:0,31:0,32:0,41:0,42:0}
	rate = {}
	nEvt = len(chambers)
	for x in (chambers):
		for me in types:
			passes[me] += me in x
	for me in types:
		rate[me] = passes[me]/nEvt*30000
	return rate

# Open file and tree
tree = uproot4.open(in_file)["MuonNtuplizerAnod"]["FlatTree"]

# Save relevant branches for Efficiency calculation into awkward arrays
print("Calculating LCT Rate")
chamber = (tree["csc_lct_station"].array()*10+tree["csc_lct_ring"].array())
rate = get_rate(chamber)
output = open("lct_output.txt","a")
output.write("LCT,%.2f kHz,%.2f kHz,%.2f kHz,%.2f kHz,%.2f kHz,%.2f kHz,%.2f kHz,%.2f kHz,%.2f kHz\n"%(rate[11],rate[12],rate[13],rate[21],rate[22],rate[31],rate[32],rate[41],rate[42]))
output.close()

print("Calculating ALCT Rate")
chamber = (tree["csc_alct_station"].array()*10+tree["csc_alct_ring"].array())
rate = get_rate(chamber)
output = open("lct_output.txt","a")
output.write("ALCT,%.2f kHz,%.2f kHz,%.2f kHz,%.2f kHz,%.2f kHz,%.2f kHz,%.2f kHz,%.2f kHz,%.2f kHz\n"%(rate[11],rate[12],rate[13],rate[21],rate[22],rate[31],rate[32],rate[41],rate[42]))
output.close()

print("Calculating CLCT Rate")
chamber = (tree["csc_clct_station"].array()*10+tree["csc_clct_ring"].array())
rate = get_rate(chamber)
output = open("lct_output.txt","a")
output.write("CLCT,%.2f kHz,%.2f kHz,%.2f kHz,%.2f kHz,%.2f kHz,%.2f kHz,%.2f kHz,%.2f kHz,%.2f kHz\n"%(rate[11],rate[12],rate[13],rate[21],rate[22],rate[31],rate[32],rate[41],rate[42]))
output.close()

