#echo -e "Higgs Mass,LLP Mass,cTau,CSC (loose),CSC (nom),CSC (tight),CSC (2loose),EMTF (1nom),EMTF (2loose),EMTF (1nom or 2loose),GMT,ALCT Corr,CLCT Corr" > Efficiency_output.txt
#echo -e "Higgs Mass,LLP Mass,cTau,N in Acc,CSC (loose),CSC (nom),CSC (tight),CSC (2loose),EMTF (1nom),EMTF (2loose),EMTF (1nom or 2loose)" > Efficiency_output.txt
echo -e "Higgs Mass,LLP Mass,cTau,N in Acc,Loose,Nominal,Tight" > Efficiency_output.txt
#echo -e "Higgs Mass,LLP Mass,cTau,N in Acc,Loose,Loose R1,Nom,Nom R1,Tight,Tight R1" > Efficiency_output.txt
search_dir=/eos/uscms/store/user/nimenend/Eff_Rate/Final
for entry in "$search_dir"/*
do
	echo $entry
	python3 efficiency_rate_simple.py $entry eff >> Efficiency_output.txt
done
python3 pretty_table.py > Efficiency_table.txt
echo ""
echo "Efficiencies and Rates in Anode"
cat Efficiency_table.txt
