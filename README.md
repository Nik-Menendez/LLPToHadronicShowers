# LLPToHadronicShowers

## Calcuating Efficiency and Rate Simply
1) Python script efficiency_rate_simple.py calculates the efficiency or rate (depeding on type of file) the most simple way by just reading in the necessary trees and counting the rate/efficiency.
2) It is controlled by run_efficiency_simple.sh which loops over all the input files and combines all the outputs into a single table.
3) All the input files are prepared in hadd_all.sh. Point the script to the directories of the latest ntuples and pick a destination to put all the files in. That destination is the one run_efficiency_simple.sh should run on.

## Calcuating Efficiency and Rate With More Complicated Procedures
1) Python script efficiency_rate.py is used to calculate the efficieny if changes needed to be made to the emulator output (i.e. changing the timing bins, changing whether you looked at anode or cathode and for which stations, etc.)
2) It is controlled by run_efficiency.sh and works the same as the simple version.
3) All input files are still prepared by hadd_all.sh.

## Which version to use
* If you want the rate/efficiency of what the emulator puts out, just use efficiency_rate_simple.py
* If you need to make changes to the emulator output, use efficiency_rate.py. If you don't understand the way changes are made in that script, feel free to ask.
