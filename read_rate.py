from csv import reader

nEv, nPass = 0,0
with open('Rate_count.csv','r') as f:
	arr = reader(f)

	for row in arr:
		nEv += int(row[0])
		nPass += int(row[1])

print("With %i total events, %i pass"%(nEv,nPass))
print("Rate = %.2f kHz"%(nPass/nEv*30000))
