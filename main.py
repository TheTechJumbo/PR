#Task 1
primaryKey=["BPCM", "BPSH", "RPSS", "RPLL", "YPLS", "YPLL", "RTMS", "RTLM", "YTLM", "YTLL", "SMNO", "SMPG", "CSST", "CSLX", "CGCR", "CGHM", "BOTH"]
categories=["Phone", "Phone", "Phone", "Phone", "Phone", "Phone", "Tablet","Tablet", "Tablet", "Tablet", "Sim", "Sim", "Case", "Case", "Charger", "Charger", "Charger"]
desc=["Compact", "Clam Shell", "RoboPhone – 5-inch screen and 64 GB memory", "RoboPhone – 6-inch screen and 256 GB memory", "Y-Phone Standard – 6-inch screen and 64 GB memory", "Y-Phone Deluxe – 6-inch screen and 256 GB memory", "RoboTab – 8-inch screen and 64 GB memory", "RoboTab – 10-inch screen and 128 GB memory", "Y-Tab Standard – 10-inch screen and 128 GB memory", "Y-Tab Deluxe – 10-inch screen and 256 GB memory", "SIM Free contract", "Pay As You Go contract", "Standard case", "Luxury case", "Car charger", "Home charger", "Both chargers"]
prcs=[29.99, 49.99, 199.99, 499.99, 549.99, 649.99, 149.99, 299.99, 499.99, 599.99,0.00, 9.99, 0.00, 50.00, 19.99, 15.99, 35.98]
devices=[]
contracts=[]
cases=[]
chargers=[]
ttlPrc=0
trsPrc=0
endPrc=0
devNum=0
rptPrchs="YES"
while rptPrchs=="YES":
	#choose a phone or tablet
	devType="a"
	while devType != "PHONE" and devType != "TABLET" :
		devType=input("Enter 'PHONE' or 'TABLET' to choose which type of device you would like: ")
	if devType == "PHONE":
		devRng=primaryKey[0:6]
		print("These are your possible phone choices along with their item codes and prices: ")
		print()
		for phone in range(6):
			print("•"+str(desc[phone])+" for £"+str(prcs[phone])+". Item code: "+str(primaryKey[phone]))
			print()
	else:
		devRng=primaryKey[6:10]
		print("These are your possible tablet choices along with their item codes and prices: ")
		print()
		for tablet in range(4):
			tablet+=6
			print("\a•"+str(desc[tablet])+" for £"+str(prcs[tablet])+". Item code: "+str(primaryKey[tablet]))
			print()
	devDec="a"
	while devDec not in devRng:
		print()
		devDec=input("From the above list, enter the item code for the device that you want to purchase: ")
	devIdx=primaryKey.index(devDec)
	devices.append(devIdx)
	print()

	#allow phone customers to choose whether the phone will be SIM Free or Pay As You Go
	cntrctDec="a"
	while cntrctDec not in primaryKey[-7:-5]:
		print()
		cntrctDec=input("Enter the item code for whichever contract you would like, either SIM Free(Item code: SMNO) or Pay As You Go(Item code: SMPG): ")
	cntrctIdx=primaryKey.index(cntrctDec)
	contracts.append(cntrctIdx)

	#allow the customer to choose a standard or luxury case
	caseDec="a"
	while caseDec not in primaryKey[-5:-3]:
		caseDec=input("\nEnter the item code for whichever case you would like, either standard(Item code: CSST) or luxury case(Item code: CSLX)? ")
	caseIdx=primaryKey.index(caseDec)
	cases.append(caseIdx)

	#allow the customer to choose the chargers required
	chrgrDec="a"
	while chrgrDec not in primaryKey[-3:]:
		chrgrDec=input("\nEnter the item code for whichever charger you would like, either a car charger(Item code: CGCR), a home charger(Item code: CGHM) or 'both'. If you want both chargers, type 'BOTH'. ")
	chrgrIdx=primaryKey.index(chrgrDec)
	chargers.append(chrgrIdx)

	#output a list of the items purchased and print the total price of this transaction
	print("\nYour basket:")
	for item in range(len(devices)):
		item-=1
		print("•"+str(desc[devices[item]]))
		print("•"+str(desc[contracts[item]]))
		print("•"+str(desc[cases[item]]))
		print("•"+str(desc[chargers[item]]))
	devLen=(len(devices)-1)
	devNum+=1
	currPrc=prcs[devices[devLen]]+prcs[contracts[devLen]]+prcs[cases[devLen]]+prcs[chargers[devLen]]
	ttlPrc+=currPrc
	rndCurrPrc=round(currPrc, 2)
	rndTtlPrc=round(ttlPrc, 2)
	print("\nThe price of your current transaction is £"+str(rndCurrPrc))
	print("The total cost of your basket is £"+str(rndTtlPrc))

#Task 2 and Task 3
	rptPrchs="a"
	while rptPrchs != "YES" and rptPrchs != "NO":
		rptPrchs=input("\nWould you like to buy any additional devices? Answer with 'YES' or NO': ")
		print()
	if rptPrchs == "NO":
		if devNum>1:
			for item in range(devNum-1):
				item+=1
				devPrc=(prcs[devices[item]])*0.9
				endPrc=devPrc+prcs[contracts[item]]+prcs[cases[item]]+prcs[chargers[item]]
		else:
			endPrc=ttlPrc
		break
print("The total cost of your basket, with the 10% discount for additional devices, is £"+str(endPrc))