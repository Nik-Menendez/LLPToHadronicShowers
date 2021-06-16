search_dir=/eos/uscms/store/user/nimenend/Eff_Rate/Final
for entry in "$search_dir"/*
do
	python3 efficiency_rate.py $entry eff
done
