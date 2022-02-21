rm -f passing_events.txt
rm -f Rate_count.csv

search_dir=/eos/uscms/store/user/nimenend/Eff_Rate/ZeroBias/crab_ZeroBias_Run2018D_L1_ANA/211203_170538/0000
for entry in "$search_dir"/*
do
	#echo $entry
	python3 print_events.py $entry eff
done
echo "Finished 20%"

search_dir=/eos/uscms/store/user/nimenend/Eff_Rate/ZeroBias/crab_ZeroBias_Run2018D_L1_ANA/211203_170538/0001
for entry in "$search_dir"/*
do
	#echo $entry
	python3 print_events.py $entry eff
done
echo "Finished 40%"

search_dir=/eos/uscms/store/user/nimenend/Eff_Rate/ZeroBias/crab_ZeroBias_Run2018D_L1_ANA/211203_170538/0002
for entry in "$search_dir"/*
do
	#echo $entry
	python3 print_events.py $entry eff
done
echo "Finished 60%"

search_dir=/eos/uscms/store/user/nimenend/Eff_Rate/ZeroBias/crab_ZeroBias_Run2018D_L1_ANA/211203_170538/0003
for entry in "$search_dir"/*
do
	#echo $entry
	python3 print_events.py $entry eff
done
echo "Finished 80%"

search_dir=/eos/uscms/store/user/nimenend/Eff_Rate/ZeroBias/crab_ZeroBias_Run2018D_L1_ANA/211203_170538/0004
for entry in "$search_dir"/*
do
	#echo $entry
	python3 print_events.py $entry eff
done
echo "Finished 100%"

python3 read_rate.py
