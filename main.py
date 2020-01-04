#Task 1
primaryKey=["BPCM", "BPSH", "RPSS", "RPLL", "YPLS", "YPLL", "RTMS", "RTLM", "YTLM", "YTLL", "SMNO", "SMPG", "CSST", "CSLX", "CGCR", "CGHM", "BOTH"]
categories=["Phone", "Phone", "Phone", "Phone", "Phone", "Phone", "Tablet","Tablet", "Tablet", "Tablet", "Sim", "Sim", "Case", "Case", "Charger", "Charger", "Charger"]
descriptions=["Compact", "Clam Shell", "RoboPhone – 5-inch screen and 64 GB memory", "RoboPhone – 6-inch screen and 256 GB memory", "Y-Phone Standard – 6-inch screen and 64 GB memory", "Y-Phone Deluxe – 6-inch screen and 256 GB memory", "RoboTab – 8-inch screen and 64 GB memory", "RoboTab – 10-inch screen and 128 GB memory", "Y-Tab Standard – 10-inch screen and 128 GB memory", "Y-Tab Deluxe – 10-inch screen and 256 GB memory", "SIM Free contract", "Pay As You Go contract", "Standard case", "Luxury case", "Car charger", "Home charger", "Both chargers"]
prices=[29.99, 49.99, 199.99, 499.99, 549.99, 649.99, 149.99, 299.99, 499.99, 599.99,0.00, 9.99, 0.00, 50.00, 19.99, 15.99, 35.98]
devices=[]
contracts=[]
cases=[]
chargers=[]
totalPrice=0
endPrice=0
repeatPurchase="YES"
while repeatPurchase=="YES":
	#choose a phone or tablet
	deviceType="a"
	while deviceType != "PHONE" and deviceType != "TABLET" :
		deviceType=input("Enter 'PHONE' or 'TABLET' to choose which type of device you would like: ")
	print()
	if deviceType == "phone":
		deviceRange=primaryKey[0:6]
		print("These are your possible phone choices along with their item codes and prices: ")
		print()
		for phone in range(6):
			print("•"+str(descriptions[phone])+" for £"+str(prices[phone])+". Item code: "+str(primaryKey[phone]))
			print()
	else:
		deviceRange=primaryKey[6:10]
		print("These are your possible tablet choices along with their item codes and prices: ")
		print()
		for tablet in range(4):
			tablet+=6
			print("•"+str(descriptions[tablet])+" for £"+str(prices[tablet])+". Item code: "+str(primaryKey[tablet]))
			print()
	deviceDec="a"
	while deviceDec not in deviceRange:
		print()
		deviceDec=input("From the above list, enter the item code for the device that you want to purchase: ")
	deviceIdx=primaryKey.index(deviceDec)
	devices.append(deviceIdx)
	print()

	#allow phone customers to choose whether the phone will be SIM Free or Pay As You Go
	contractDec="a"
	while contractDec not in primaryKey[-7:-5]:
		print()
		contractDec=input("Enter the item code for whichever contract you would like, either SIM Free(Item code: SMNO) or Pay As You Go(Item code: SMPG): ")
	contractIdx=primaryKey.index(contractDec)
	contracts.append(contractIdx)

	#allow the customer to choose a standard or luxury case
	caseDec="a"
	while caseDec not in primaryKey[-5:-3]:
		print()
		caseDec=input("Enter the item code for whichever case you would like, either standard(Item code: CSST) or luxury case(Item code: CSLX)? ")
	caseIdx=primaryKey.index(caseDec)
	cases.append(caseIdx)

	#allow the customer to choose the chargers required
	chargerDec="a"
	while chargerDec not in primaryKey[-3:]:
		print()
		chargerDec=input("Enter the item code for whichever charger you would like, either a car charger(Item code: CGCR), a home charger(Item code: CGHM) or 'both'. If you want both chargers, type 'BOTH'. ")
	chargerIdx=primaryKey.index(chargerDec)
	chargers.append(chargerIdx)

	#output a list of the items purchased and print the total price of this transaction
	print()
	print("Your basket:")
	for item in range(len(devices)):
		item-=1
		print("•"+str(descriptions[devices[item]]))
		print("•"+str(descriptions[contracts[item]]))
		print("•"+str(descriptions[cases[item]]))
		print("•"+str(descriptions[chargers[item]]))
		currentPrice=prices[devices[item]]+prices[contracts[item]]+prices[cases[item]]+prices[chargers[item]]
	totalPrice+=currentPrice
	print()
	print("The total cost of your basket is £"+str(totalPrice))
	devNum=len(devices)
#Task 2 and Task 3
	repeatPurchase="a"
	while repeatPurchase != "YES" and repeatPurchase != "NO":
		repeatPurchase=input("Would you like to buy any additional devices? Answer with 'YES' or NO': ")
		print()
	if repeatPurchase == "NO":
		if devNum>0:
			for item in range((devNum)-1):
				item+=1
				devPrice=(prices[devices[item]])*0.9
				endPrice+=devPrice
			endPrice+=(prices[devices[0]])
		break
print("The total cost of your basket is £"+str(endPrice))