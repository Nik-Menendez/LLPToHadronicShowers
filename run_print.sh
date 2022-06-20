rm -f passing_events.txt
rm -f Rate_count.csv

search_dir=/eos/uscms/store/user/nimenend/Eff_Rate/ZeroBias/crab_ZeroBias_Run2018D_L1_ANA/220402_161205/0000
for entry in "$search_dir"/*
do
	#echo $entry
	python3 print_events.py $entry eff
done
echo "Finished 12.5%"

search_dir=/eos/uscms/store/user/nimenend/Eff_Rate/ZeroBias/crab_ZeroBias_Run2018D_L1_ANA/220402_161205/0001
for entry in "$search_dir"/*
do
	#echo $entry
	python3 print_events.py $entry eff
done
echo "Finished 25%"

search_dir=/eos/uscms/store/user/nimenend/Eff_Rate/ZeroBias/crab_ZeroBias_Run2018D_L1_ANA/220402_161205/0002
for entry in "$search_dir"/*
do
	#echo $entry
	python3 print_events.py $entry eff
done
echo "Finished 37.5%"

search_dir=/eos/uscms/store/user/nimenend/Eff_Rate/ZeroBias/crab_ZeroBias_Run2018D_L1_ANA/220402_161205/0003
for entry in "$search_dir"/*
do
	#echo $entry
	python3 print_events.py $entry eff
done
echo "Finished 50%"

search_dir=/eos/uscms/store/user/nimenend/Eff_Rate/ZeroBias/crab_ZeroBias_Run2018D_L1_ANA/220402_161205/0004
for entry in "$search_dir"/*
do
	#echo $entry
	python3 print_events.py $entry eff
done
echo "Finished 62.5%"

search_dir=/eos/uscms/store/user/nimenend/Eff_Rate/ZeroBias/crab_ZeroBias_Run2018D_L1_ANA/220402_161205/0005
for entry in "$search_dir"/*
do
	#echo $entry
	python3 print_events.py $entry eff
done
echo "Finished 75%"

search_dir=/eos/uscms/store/user/nimenend/Eff_Rate/ZeroBias/crab_ZeroBias_Run2018D_L1_ANA/220402_161205/0006
for entry in "$search_dir"/*
do
	#echo $entry
	python3 print_events.py $entry eff
done
echo "Finished 87.5%"

search_dir=/eos/uscms/store/user/nimenend/Eff_Rate/ZeroBias/crab_ZeroBias_Run2018D_L1_ANA/220402_161205/0007
for entry in "$search_dir"/*
do
	#echo $entry
	python3 print_events.py $entry eff
done
echo "Finished 100%"

search_dir=/eos/uscms/store/user/nimenend/Eff_Rate/ZeroBias/crab_ZeroBias_Run2018D_L1_ANA/220402_161205/0008
for entry in "$search_dir"/*
do
	#echo $entry
	python3 print_events.py $entry eff
done
echo "Finished 100%"

python3 read_rate.py
