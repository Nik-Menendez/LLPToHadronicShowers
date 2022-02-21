echo -e "Type,ME11,ME12,ME13,ME21,ME22,ME31,ME32,ME41,ME42" > lct_output.txt
python3 LCT_rate.py
python3 pretty_table_lct.py > LCT_table.txt
echo -e "LCT Rates for each chamber type"
cat LCT_table.txt
