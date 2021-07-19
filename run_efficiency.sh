echo -e "Higgs Mass,LLP Mass,cTau,CSC (loose),CSC (nom),CSC (tight),CSC (2loose),EMTF (1nom),EMTF (2loose),EMTF (1nom or 2loose),GMT,ALCT Corr,CLCT Corr" > Efficiency_output.txt
search_dir=/eos/uscms/store/user/nimenend/Eff_Rate/Final
for entry in "$search_dir"/*
do
	echo $entry
	python3 efficiency_rate.py $entry eff >> Efficiency_output.txt
done
python3 pretty_table.py > Efficiency_table.txt
cat Efficiency_table.txt
