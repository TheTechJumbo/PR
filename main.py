#Task 1
primaryKey=["BPCM", "BPSH", "RPSS", "RPLL", "YPLS", "YPLL", "RTMS", "RTLM", "YTLM", "YTLL", "SMNO", "SMPG", "CSST", "CSLX", "CGCR", "CGHM", "BOTH"]
categories=["Phone", "Phone", "Phone", "Phone", "Phone", "Phone", "Tablet","Tablet", "Tablet", "Tablet", "Sim", "Sim", "Case", "Case", "Charger", "Charger", "Charger"]
desc=["Compact", "Clam Shell", "RoboPhone – 5-inch screen and 64 GB memory", "RoboPhone – 6-inch screen and 256 GB memory",
"Y-Phone Standard – 6-inch screen and 64 GB memory", "Y-Phone Deluxe – 6-inch screen and 256 GB memory", "RoboTab – 8-inch screen and 64 GB memory",
"RoboTab – 10-inch screen and 128 GB memory", "Y-Tab Standard – 10-inch screen and 128 GB memory", "Y-Tab Deluxe – 10-inch screen and 256 GB memory",
 "SIM Free contract", "Pay As You Go contract", "Standard case", "Luxury case", "Car charger", "Home charger", "Both chargers"]
prcs=[29.99, 49.99, 199.99, 499.99, 549.99, 649.99, 149.99, 299.99, 499.99, 599.99,0.00, 9.99, 0.00, 50.00, 19.99, 15.99, 35.98]
devices=[]
contracts=[]
cases=[]
chargers=[]
ttlPrc=0
trsPrc=0
fnlPrc=0
devNum=0

class colour:
	RED="\033[0;31;40m"
	YELLOW="\033[0;33;40m"
	GREEN="\033[0;32;40m"
	END="\033[0;47;40m"
def error():
	print(colour.RED +" INPUT VALUE INVALID\n"+ colour.YELLOW)

rptPrchs="YES"
while rptPrchs=="YES":
	#choose a phone or tablet
	devType=input(colour.YELLOW + "Please enter 'PHONE' or 'TABLET' to choose which type of device you would like:")
	while devType != "PHONE" and devType != "TABLET" :
		error()
		devType=input("Please enter 'PHONE' or 'TABLET' to choose which type of device you would like: ")
	if devType == "PHONE":
		devRng=primaryKey[0:6]
		print("These are your possible phone choices along with their item codes and prices: \n")
		for phone in range(6):
			print(colour.GREEN+"•"+str(desc[phone])+" for £"+str(prcs[phone])+". Item code: "+str(primaryKey[phone])+"\n")
			cntrctDec="a"
	else:
		devRng=primaryKey[6:10]
		print("These are your possible tablet choices along with their item codes and prices: \n")
		for tablet in range(4):
			tablet+=6
			print("•"+str(desc[tablet])+" for £"+str(prcs[tablet])+". Item code: "+str(primaryKey[tablet]))
	devDec=input("From the above list, enter the item code for the device that you want to purchase: \n")
	while devDec not in devRng:
		error()
		devDec=input("From the above list, enter the item code for the device that you want to purchase: \n")
	devIdx=primaryKey.index(devDec)
	devices.append(devIdx)

	#allow phone customers to choose whether the phone will be SIM Free or Pay As You Go
	if devType=="PHONE":
		cntrctDec=input("Enter the item code for whichever contract you would like, either SIM Free(Item code: SMNO) or Pay As You Go(Item code: SMPG): ")
		while cntrctDec not in primaryKey[-7:-5]:
			error()
			cntrctDec=input("Enter the item code for whichever contract you would like, either SIM Free(Item code: SMNO) or Pay As You Go(Item code: SMPG): ")
		cntrctIdx=primaryKey.index(cntrctDec)
		contracts.append(cntrctIdx)

	#allow the customer to choose a standard or luxury case
	caseDec=input("\nEnter the item code for whichever case you would like, either standard(Item code: CSST) or luxury case(Item code: CSLX)? ")
	while caseDec not in primaryKey[-5:-3]:
		error()
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
		print(colour.YELLOW+"•"+str(desc[devices[item]]))
		print("•"+str(desc[contracts[item]]))
		print("•"+str(desc[cases[item]]))
		print("•"+str(desc[chargers[item]]))
	devLen=(len(devices)-1)
	devNum+=1
	currPrc=prcs[devices[devLen]]+prcs[contracts[devLen]]+prcs[cases[devLen]]+prcs[chargers[devLen]]
	ttlPrc+=currPrc
	currPrc=round(currPrc, 2)
	ttlPrc=round(ttlPrc, 2)
	print("\nThe price of your current transaction is £"+str(currPrc))
	print("The total cost of your basket is £"+str(ttlPrc))

#Task 2 and Task 3
	rptPrchs="a"
	while rptPrchs != "YES" and rptPrchs != "NO":
		rptPrchs=input("\nWould you like to buy any additional devices? Answer with 'YES' or NO': \n")
	if rptPrchs == "NO":
		if devNum>1:
			for item in range(devNum-1):
				item+=1
				devPrc=(prcs[devices[item]])*0.9
				fnlPrc=prcs[contracts[item]]+prcs[cases[item]]+prcs[chargers[item]]
				fnlPrc+=devPrc
		else:
			fnlPrc=ttlPrc
		break
fnlPrc=round(fnlPrc, 2)
print("The total cost of your basket, with the 10% discount for additional devices, is £"+str(fnlPrc))


