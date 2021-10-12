from __future__ import division

import pandas as pd
import numpy as np
from tqdm import tqdm
import pickle
import matplotlib.pyplot as plt

hard_cuts = True
showerChoice = 1

in_dir = "/eos/uscms/store/user/nimenend/Eff_Rate/Final/"
bkg_files = ["ZeroBias_Data"]
sig_files = [
"MH_1000_MFF_450_CTau_100000mm",
"MH_125_MFF_12_CTau_9000mm",
"MH_125_MFF_12_CTau_900mm",
"MH_125_MFF_1_CTau_10000mm",
"MH_125_MFF_1_CTau_1000mm",
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
]

MEs = [11, 12, 13, 21, 22, 31, 32, 41, 42]
comp_chamber = [ 'Ev_max_nComp_ME11',
                 'Ev_max_nComp_ME12',
                 'Ev_max_nComp_ME13',
                 'Ev_max_nComp_ME21',
                 'Ev_max_nComp_ME22',
                 'Ev_max_nComp_ME31',
                 'Ev_max_nComp_ME32',
                 'Ev_max_nComp_ME41',
                 'Ev_max_nComp_ME42']
wire_chamber = [ 'Ev_max_nWire_ME11',
                 'Ev_max_nWire_ME12',
                 'Ev_max_nWire_ME13',
                 'Ev_max_nWire_ME21',
                 'Ev_max_nWire_ME22',
                 'Ev_max_nWire_ME31',
                 'Ev_max_nWire_ME32',
                 'Ev_max_nWire_ME41',
                 'Ev_max_nWire_ME42']

print("Opening signal samples:")
first = True
for s in tqdm(sig_files):

	with open('output/comp68_wire79/maxHits_%s.p'%(s), 'rb') as handle:
		maxes = pickle.load(handle)

	if first:
		comp_sig = pd.DataFrame(maxes["comp"])
		wire_sig = pd.DataFrame(maxes["wire"])
		first = False
	else:
		temp_comp = pd.DataFrame(maxes["comp"])
		temp_wire = pd.DataFrame(maxes["wire"])
		comp_sig = comp_sig.append(temp_comp)
		wire_sig = wire_sig.append(temp_wire)

print("Opening background samples:")
with open('output/comp68_wire79/maxHits_%s.p'%(bkg_files[0]), 'rb') as handle:	
	maxes = pickle.load(handle)

comp_bkg = pd.DataFrame(maxes["comp"])
wire_bkg = pd.DataFrame(maxes["wire"])
del maxes

# Rename columns to coincide with old code
new_names_comp, new_names_wire = {}, {}
for i in range(len(MEs)):
	new_names_comp[MEs[i]] = comp_chamber[i]
	new_names_wire[MEs[i]] = wire_chamber[i]

comp_sig = comp_sig.rename(columns=new_names_comp)
comp_bkg = comp_bkg.rename(columns=new_names_comp)
wire_sig = wire_sig.rename(columns=new_names_wire)
wire_bkg = wire_bkg.rename(columns=new_names_wire)

comp_sig_tot = len(comp_sig)
comp_bkg_tot = len(comp_bkg)
wire_sig_tot = len(wire_sig)
wire_bkg_tot = len(wire_bkg)

## optimizing thresholds
## pick 5 values for each chamber
## use table 3 as a starting point
comparator_seed = [
    105, 61, 25, 40, 40, 40, 35, 45, 35
]

comparator_delta = [
    1, 5, 5, 5, 5, 5, 5, 5, 5
]

comparator_width = [
    0, 1, 1, 1, 1, 1, 1, 1, 1
]


wire_seed = [
    102, 60, 17, 41, 28, 39, 21, 38, 23
]

wire_delta = [
    1, 2, 2, 2, 2, 2, 2, 2, 2
]

wire_width = [
    0, 1, 1, 1, 1, 1, 1, 1, 1
]

prev_nom_compXX = [100,55,20,35,29,35,25,40,30]
prev_nom_wireXX = [100,55,20,35,29,35,25,40,30]

## 9 variables
## each variable scans 10 points
## 3 time bins
## 2 types of hits
## 3 rate working points

def generate_range(station):
    return [i for i in range(comparator_seed[station] - comparator_width[station] * comparator_delta[station],
                    comparator_seed[station] + (comparator_width[station] + 1) * comparator_delta[station],
                    comparator_delta[station])]

def generate_wire_range(station):
    return [i for i in range(wire_seed[station] - wire_width[station] * wire_delta[station],
                    wire_seed[station] + (wire_width[station] + 1) * wire_delta[station],
                    wire_delta[station])]

def calculate_comp_efficiency(T1, T2, T3, T4, T5, T6, T7, T8, T9):
    return len(comp_sig[(comp_sig['Ev_max_nComp_ME11'] > T1) |
                        (comp_sig['Ev_max_nComp_ME12'] > T2) |
                        (comp_sig['Ev_max_nComp_ME13'] > T3) |
                        (comp_sig['Ev_max_nComp_ME21'] > T4) |
                        (comp_sig['Ev_max_nComp_ME22'] > T5) |
                        (comp_sig['Ev_max_nComp_ME31'] > T6) |
                        (comp_sig['Ev_max_nComp_ME32'] > T7) |
                        (comp_sig['Ev_max_nComp_ME41'] > T8) |
                        (comp_sig['Ev_max_nComp_ME42'] > T9)])

def calculate_comp_efficiency_norm(T1, T2, T3, T4, T5, T6, T7, T8, T9):
    return calculate_comp_efficiency(T1, T2, T3, T4, T5, T6, T7, T8, T9)/ comp_sig_tot

def calculate_wire_efficiency(T1, T2, T3, T4, T5, T6, T7, T8, T9):
    return len(wire_sig[(wire_sig['Ev_max_nWire_ME11'] > T1) |
                        (wire_sig['Ev_max_nWire_ME12'] > T2) |
                        (wire_sig['Ev_max_nWire_ME13'] > T3) |
                        (wire_sig['Ev_max_nWire_ME21'] > T4) |
                        (wire_sig['Ev_max_nWire_ME22'] > T5) |
                        (wire_sig['Ev_max_nWire_ME31'] > T6) |
                        (wire_sig['Ev_max_nWire_ME32'] > T7) |
                        (wire_sig['Ev_max_nWire_ME41'] > T8) |
                        (wire_sig['Ev_max_nWire_ME42'] > T9)])

def calculate_wire_efficiency_norm(T1, T2, T3, T4, T5, T6, T7, T8, T9):
    return calculate_wire_efficiency(T1, T2, T3, T4, T5, T6, T7, T8, T9) / wire_sig_tot

def calculate_comp_rate(T1, T2, T3, T4, T5, T6, T7, T8, T9):
    return len(comp_bkg[(comp_bkg['Ev_max_nComp_ME11'] > T1) |
                        (comp_bkg['Ev_max_nComp_ME12'] > T2) |
                        (comp_bkg['Ev_max_nComp_ME13'] > T3) |
                        (comp_bkg['Ev_max_nComp_ME21'] > T4) |
                        (comp_bkg['Ev_max_nComp_ME22'] > T5) |
                        (comp_bkg['Ev_max_nComp_ME31'] > T6) |
                        (comp_bkg['Ev_max_nComp_ME32'] > T7) |
                        (comp_bkg['Ev_max_nComp_ME41'] > T8) |
                        (comp_bkg['Ev_max_nComp_ME42'] > T9)])

def calculate_wire_rate(T1, T2, T3, T4, T5, T6, T7, T8, T9):
    return len(wire_bkg[(wire_bkg['Ev_max_nWire_ME11'] > T1) |
                        (wire_bkg['Ev_max_nWire_ME12'] > T2) |
                        (wire_bkg['Ev_max_nWire_ME13'] > T3) |
                        (wire_bkg['Ev_max_nWire_ME21'] > T4) |
                        (wire_bkg['Ev_max_nWire_ME22'] > T5) |
                        (wire_bkg['Ev_max_nWire_ME31'] > T6) |
                        (wire_bkg['Ev_max_nWire_ME32'] > T7) |
                        (wire_bkg['Ev_max_nWire_ME41'] > T8) |
                        (wire_bkg['Ev_max_nWire_ME42'] > T9)])

def calculate_comp_rate_norm(T1, T2, T3, T4, T5, T6, T7, T8, T9):
    return calculate_comp_rate(T1, T2, T3, T4, T5, T6, T7, T8, T9) / comp_bkg_tot*32*1000

def calculate_wire_rate_norm(T1, T2, T3, T4, T5, T6, T7, T8, T9):
    return calculate_wire_rate(T1, T2, T3, T4, T5, T6, T7, T8, T9) / wire_bkg_tot*32*1000

def calculate_loss(T1, T2, T3, T4, T5, T6, T7, T8, T9):
    return (calculate_comp_efficiency(T1, T2, T3, T4, T5, T6, T7, T8, T9)/np.sqrt(calculate_comp_rate(T1, T2, T3, T4, T5, T6, T7, T8, T9)))

# Calculate guesses for thresholds in each chamber
idx = 0
current_max = 0

min_=0
max_=150
it_=1


## choice of shower
r1=1
r2=1

# loose
if showerChoice == 0:
    r1=3
    r2=4
# nominal
elif showerChoice == 1:
    r1=2
    r2=3
# tight
elif showerChoice == 2:
    r1=1
    r2=2

r = [r1, r2, r2, r1, r2, r1, r2, r1, r2]

l1=.15
l2=.18
rmin = [0.0,.02,.02,.02,.02,.02,.02,.02,.02]
rmax_t = [.02, l2, l2, l1, l2, l1, l2, l1, l2]
rmax = [i*1 for i in rmax_t]


compXX = [0,0,0,0,0,0,0,0,0]
wireXX = [0,0,0,0,0,0,0,0,0]

print("Calculating base Comparator Thresholds:")
for inc in (range(len(comp_chamber))):

    comp_efficiency=[0]
    comp_rate=[0]
    comp_limits=[0]
    best = 0.0
    best_cut = 149

    for limit in tqdm(range(min_,max_,it_),leave=False):
        comp_efficiency.append(len(comp_sig[(comp_sig[comp_chamber[inc]] > limit)])/comp_sig_tot*100)

        comp_rate.append(len(comp_bkg[(comp_bkg[comp_chamber[inc]] > limit)])/comp_bkg_tot*30*1000)

        comp_limits.append(limit)

    for i in range(len(comp_rate)):
        if comp_rate[i] > rmin[inc] and comp_rate[i] < rmax[inc]:
            if np.power(comp_efficiency[i],r[inc])/np.sqrt(comp_rate[i]) > best:
                best = np.power(comp_efficiency[i],r[inc])/np.sqrt(comp_rate[i])
                best_cut = comp_limits[i]

    if hard_cuts:
        compXX = prev_nom_compXX #nominal
        #compXX = [149, 64, 21, 33, 34, 33, 25, 32, 31] #tight
        #compXX = [99, 57, 25, 45, 36, 43, 29, 43, 32] #loose
        best_cut = compXX[inc]
    print( "For " + comp_chamber[inc] + ":")
    print( "Best threshold > %i" %(best_cut))
    print( 'rate =', comp_rate[best_cut+1], 'kHz and efficiency =', comp_efficiency[best_cut+1], '% for threshold >', comp_limits[best_cut+1])
    print( "-----------------------------------------------------------------------")
    compXX[inc] = best_cut

#compXX[0] = 100 
efficiency_comp_final = len(comp_sig[(comp_sig['Ev_max_nComp_ME11'] > compXX[0]) |
                                     (comp_sig['Ev_max_nComp_ME12'] > compXX[1]) |
                                     (comp_sig['Ev_max_nComp_ME13'] > compXX[2]) |
                                     (comp_sig['Ev_max_nComp_ME21'] > compXX[3]) |
                                     (comp_sig['Ev_max_nComp_ME22'] > compXX[4]) |
                                     (comp_sig['Ev_max_nComp_ME31'] > compXX[5]) |
                                     (comp_sig['Ev_max_nComp_ME32'] > compXX[6]) |
                                     (comp_sig['Ev_max_nComp_ME41'] > compXX[7]) |
                                     (comp_sig['Ev_max_nComp_ME42'] > compXX[8])])/comp_sig_tot*100

rate_comp_final       = len(comp_bkg[(comp_bkg['Ev_max_nComp_ME11'] > compXX[0]) |
                                     (comp_bkg['Ev_max_nComp_ME12'] > compXX[1]) |
                                     (comp_bkg['Ev_max_nComp_ME13'] > compXX[2]) |
                                     (comp_bkg['Ev_max_nComp_ME21'] > compXX[3]) |
                                     (comp_bkg['Ev_max_nComp_ME22'] > compXX[4]) |
                                     (comp_bkg['Ev_max_nComp_ME31'] > compXX[5]) |
                                     (comp_bkg['Ev_max_nComp_ME32'] > compXX[6]) |
                                     (comp_bkg['Ev_max_nComp_ME41'] > compXX[7]) |
                                     (comp_bkg['Ev_max_nComp_ME42'] > compXX[8])])/comp_bkg_tot*30*1000

print( "Combined Result:")
print( "rate =", rate_comp_final, "kHz, efficiency =", efficiency_comp_final, "%")

rate_num_final       = len(comp_bkg[(comp_bkg['Ev_max_nComp_ME11'] > compXX[0]) |
                                    (comp_bkg['Ev_max_nComp_ME12'] > compXX[1]) |
                                    (comp_bkg['Ev_max_nComp_ME13'] > compXX[2]) |
                                    (comp_bkg['Ev_max_nComp_ME21'] > compXX[3]) |
                                    (comp_bkg['Ev_max_nComp_ME22'] > compXX[4]) |
                                    (comp_bkg['Ev_max_nComp_ME31'] > compXX[5]) |
                                    (comp_bkg['Ev_max_nComp_ME32'] > compXX[6]) |
                                    (comp_bkg['Ev_max_nComp_ME41'] > compXX[7]) |
                                    (comp_bkg['Ev_max_nComp_ME42'] > compXX[8])])

print( "Number of events that pass:", rate_num_final, " out of", comp_bkg_tot)
print("")

print("Calculating base wire thresholds:")
for inc in (range(len(wire_chamber))):

    wire_efficiency=[0]
    wire_sig_tot = len(wire_sig)
    wire_rate=[0]
    wire_bkg_tot = len(wire_bkg)
    wire_limits=[0]
    best = 0.0
    best_cut = 149

    for limit in tqdm(range(min_,max_,it_),leave=False):
        wire_efficiency.append(len(wire_sig[(wire_sig[wire_chamber[inc]] > limit)])/wire_sig_tot*100)

        wire_rate.append(len(wire_bkg[(wire_bkg[wire_chamber[inc]] > limit)])/wire_bkg_tot*30*1000)

        wire_limits.append(limit)

    for i in range(len(wire_rate)):
        if wire_rate[i] > rmin[inc] and wire_rate[i] < rmax[inc]:
            if np.power(wire_efficiency[i],r[inc])/np.sqrt(wire_rate[i]) > best:
                best = np.power(wire_efficiency[i],r[inc])/np.sqrt(wire_rate[i])
                best_cut = wire_limits[i]

    if hard_cuts:
        wireXX = prev_nom_wireXX #nominal
        #wireXX = [149, 108, 27,  75, 44,  83, 34,  83, 40] #tight
        #wireXX = [105, 93, 33, 134, 80, 118, 75, 128, 87] #loose
        best_cut = wireXX[inc]
    print( "For " + wire_chamber[inc] + ":")
    print( "Best threshold > %i" %(best_cut))
    print( 'rate =', wire_rate[best_cut+1], 'kHz and efficiency =', wire_efficiency[best_cut+1], '% for threshold >', wire_limits[best_cut+1])
    print( "-----------------------------------------------------------------------")
    wireXX[inc] = best_cut

#wireXX[0] = 140
efficiency_wire_final = len(wire_sig[(wire_sig['Ev_max_nWire_ME11'] > wireXX[0]) |
                                     (wire_sig['Ev_max_nWire_ME12'] > wireXX[1]) |
                                     (wire_sig['Ev_max_nWire_ME13'] > wireXX[2]) |
                                     (wire_sig['Ev_max_nWire_ME21'] > wireXX[3]) |
                                     (wire_sig['Ev_max_nWire_ME22'] > wireXX[4]) |
                                     (wire_sig['Ev_max_nWire_ME31'] > wireXX[5]) |
                                     (wire_sig['Ev_max_nWire_ME32'] > wireXX[6]) |
                                     (wire_sig['Ev_max_nWire_ME41'] > wireXX[7]) |
                                     (wire_sig['Ev_max_nWire_ME42'] > wireXX[8])])/wire_sig_tot*100

rate_wire_final       = len(wire_bkg[(wire_bkg['Ev_max_nWire_ME11'] > wireXX[0]) |
                                     (wire_bkg['Ev_max_nWire_ME12'] > wireXX[1]) |
                                     (wire_bkg['Ev_max_nWire_ME13'] > wireXX[2]) |
                                     (wire_bkg['Ev_max_nWire_ME21'] > wireXX[3]) |
                                     (wire_bkg['Ev_max_nWire_ME22'] > wireXX[4]) |
                                     (wire_bkg['Ev_max_nWire_ME31'] > wireXX[5]) |
                                     (wire_bkg['Ev_max_nWire_ME32'] > wireXX[6]) |
                                     (wire_bkg['Ev_max_nWire_ME41'] > wireXX[7]) |
                                     (wire_bkg['Ev_max_nWire_ME42'] > wireXX[8])])/wire_bkg_tot*30*1000

print( "Combined Result:")
print( "rate =", rate_wire_final, "kHz, efficiency =", efficiency_wire_final, "%")

rate_num_final       = len(wire_bkg[(wire_bkg['Ev_max_nWire_ME11'] > wireXX[0]) |
                                    (wire_bkg['Ev_max_nWire_ME12'] > wireXX[1]) |
                                    (wire_bkg['Ev_max_nWire_ME13'] > wireXX[2]) |
                                    (wire_bkg['Ev_max_nWire_ME21'] > wireXX[3]) |
                                    (wire_bkg['Ev_max_nWire_ME22'] > wireXX[4]) |
                                    (wire_bkg['Ev_max_nWire_ME31'] > wireXX[5]) |
                                    (wire_bkg['Ev_max_nWire_ME32'] > wireXX[6]) |
                                    (wire_bkg['Ev_max_nWire_ME41'] > wireXX[7]) |
                                    (wire_bkg['Ev_max_nWire_ME42'] > wireXX[8])])

print( "Number of events that pass:", rate_num_final, " out of", wire_bkg_tot)
print("")

if hard_cuts:
    compXX = prev_nom_compXX #nominal
    #compXX = [149, 64, 21, 33, 34, 33, 25, 32, 31] #tight
    #compXX = [99, 57, 25, 45, 36, 43, 29, 43, 32] #loose
    wireXX = prev_nom_wireXX #nominal
    #wireXX = [149, 108, 27,  75, 44,  83, 34,  83, 40] #tight
    #wireXX = [105, 93, 33, 134, 80, 118, 75, 128, 87] #loose


print( "Guess Comparator Thresholds:")
print( "ME11: %i, ME12: %i, ME13: %i," %(compXX[0],compXX[1],compXX[2]))
print( "ME21: %i, ME22: %i," %(compXX[3],compXX[4]))
print( "ME31: %i, ME32: %i," %(compXX[5],compXX[6]))
print( "ME41: %i, ME42: %i," %(compXX[7],compXX[8]))
print( "With rate and efficiency:")
print( "rate = %f kHz, efficiency = %f%%" %(rate_comp_final,efficiency_comp_final))
print("")
print( "Guess Wire Thresholds:")
print( "ME11: %i, ME12: %i, ME13: %i," %(wireXX[0],wireXX[1],wireXX[2]))
print( "ME21: %i, ME22: %i," %(wireXX[3],wireXX[4]))
print( "ME31: %i, ME32: %i," %(wireXX[5],wireXX[6]))
print( "ME41: %i, ME42: %i," %(wireXX[7],wireXX[8]))
print( "With rate and efficiency:")
print( "rate = %f kHz, efficiency = %f%%" %(rate_wire_final,efficiency_wire_final))
print("")

comparator_seed = compXX
wire_seed = wireXX

best_eff, best_rate, best_idx = 0, 0, 0
best_wire = wire_seed
print("Calculating optimal wire thresholds using guesses as base")
for i1 in tqdm(generate_wire_range(0)):
    for i2 in tqdm(generate_wire_range(1),leave=False):
        for i3 in tqdm(generate_wire_range(2),leave=False):
            for i4 in tqdm(generate_wire_range(3),leave=False):
                for i5 in tqdm(generate_wire_range(4),leave=False):
                    for i6 in tqdm(generate_wire_range(5),leave=False):
                        for i7 in tqdm(generate_wire_range(6),leave=False):
                            for i8 in tqdm(generate_wire_range(7),leave=False):
                                for i9 in tqdm(generate_wire_range(8),leave=False):
                                    idx += 1
                                    #comp_rate = calculate_comp_rate_norm(i1, i2, i3, i4, i5, i6, i7, i8, i9)
                                    wire_rate = calculate_wire_rate_norm(i1, i2, i3, i4, i5, i6, i7, i8, i9)
                                    if (0.4 < wire_rate and wire_rate < 0.75):
                                        wire_eff = calculate_wire_efficiency_norm(i1, i2, i3, i4, i5, i6, i7, i8, i9)
                                        if wire_eff > best_eff:
                                            best_eff = wire_eff
                                            best_rate = wire_rate
                                            best_idx = idx
                                            best_wire = [i1, i2, i3, i4, i5, i6, i7, i8, i9]
                                        #if wire_eff > 0.29:
                                            #print( idx, i1, i2, i3, i4, i5, i6, i7, i8, i9, "rate", wire_rate, "eff", wire_eff, "best", best_idx)

print( best_rate, best_eff*100, best_idx, best_wire)
print("")

best_eff, best_rate, best_idx = 0, 0, 0
best_comp = comparator_seed
print("Calculating optimal comparator thresholds using guesses as base")
for i1 in tqdm(generate_range(0)):
    for i2 in tqdm(generate_range(1),leave=False):
        for i3 in tqdm(generate_range(2),leave=False):
            for i4 in tqdm(generate_range(3),leave=False):
                for i5 in tqdm(generate_range(4),leave=False):
                    for i6 in tqdm(generate_range(5),leave=False):
                        for i7 in tqdm(generate_range(6),leave=False):
                            for i8 in tqdm(generate_range(7),leave=False):
                                for i9 in tqdm(generate_range(8),leave=False):
                                    idx += 1
                                    comp_rate = calculate_comp_rate_norm(i1, i2, i3, i4, i5, i6, i7, i8, i9)
                                    #wire_rate = calculate_wire_rate_norm(i1, i2, i3, i4, i5, i6, i7, i8, i9)
                                    if (0.4 < comp_rate and comp_rate < 0.75):
                                        comp_eff = calculate_comp_efficiency_norm(i1, i2, i3, i4, i5, i6, i7, i8, i9)
                                        if comp_eff > best_eff:
                                            best_eff = comp_eff
                                            best_rate = comp_rate
                                            best_idx = idx
                                            best_comp = [i1, i2, i3, i4, i5, i6, i7, i8, i9]
                                        #if comp_eff > 0.29:
                                            #print( idx, i1, i2, i3, i4, i5, i6, i7, i8, i9, "rate", comp_rate, "eff", comp_eff, "best", best_idx)

print( best_rate, best_eff*100, best_idx, best_comp)
print("")
