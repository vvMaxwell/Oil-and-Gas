#Welcome Message & Input
inputGasOil = input("--------------------------------------------"\
"\n*** Welcome to Gas Station Supplier Program! ***"\
"\n--------------------------------------------"\
"\nPlease input the following pruchase:\nG: Gas\nO: Oil\n>>> ")
#If input for G
if inputGasOil.upper() == "G":
    gasLitres = input("Enter number of litres to be purchased: ")
    gasLitres = int(gasLitres)
    gasCost = gasLitres * 1.07
#If input for G more than 4000
    if gasLitres >= 4000:
        gasDiscounted = (gasLitres * 1.07) * 0.9
        priceBeforeTax = gasDiscounted
    else:
        print(gasCost)
        priceBeforeTax = gasCost
#If input for O
elif inputGasOil.upper() == "O":
    cases = input("Enter # of cases of Oil: ")
    cases = int(cases)
    oilLitres = cases * 12
    oilNoDiscount = oilLitres * 1.27
#If input for O more than 4000
    if cases > 8:
        oilDiscounted = oilLitres * 1.27 * 0.9
        priceBeforeTax = oilDiscounted
    else:
        priceBeforeTax = oilNoDiscount
#Error statement
else:
    print("Invalid input, you should enter g/G or o/O")
province = input("Enter province: ").upper()
#Provinces 5% tax
if province in ["AB","BC","MB","NT","NU","QC","SK","YT"]:
    gstDeduction = priceBeforeTax * 0.05
    costAfterTax = (priceBeforeTax * 1.05)
#Provinces 13% tax
elif province == "ON":
    gstDeduction = priceBeforeTax * 0.13
    costAfterTax = (priceBeforeTax * 1.13)
#Provinces 15% tax
else:
    gstDeduction = priceBeforeTax * 0.15
    costAfterTax = (priceBeforeTax * 1.15)
if inputGasOil.upper() == "G":
    print(f"-----------------------------------------------------------------------------------------------------------\n\
Product       # Of Liters       Price Before       Price After       GST       Total Price\n\
GAS            {gasLitres:>10.1f} {gasCost:>18.1f} {priceBeforeTax:>17.1f} {gstDeduction:>9.2f} {costAfterTax:>17.2f}\n\
-----------------------------------------------------------------------------------------------------------")
if inputGasOil.upper() == "O":
    print(f"-----------------------------------------------------------------------------------------------------------\n\
Product       # Of Liters       Price Before       Price After       GST       Total Price\n\
OIL            {oilLitres:>10.1f} {oilNoDiscount:>18.1f} {priceBeforeTax:17.1f} {gstDeduction:>9.2f} {costAfterTax:>17.2f}\n\
-----------------------------------------------------------------------------------------------------------")    
print("Thanks for your business, Good Bye.")