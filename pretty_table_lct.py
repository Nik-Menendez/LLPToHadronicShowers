from prettytable import from_csv
with open("lct_output.txt") as fp:
	mytable = from_csv(fp)

print(mytable)
