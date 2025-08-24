# pass test min 40 % total and 33 % in each 3 subs
Phy=int(input("Enter Physics marks: "))
Chem=int(input("Enter Chemistry marks: "))
Math=int(input("Enter Math marks: "))
Phy_Per= (Phy/100)*100
Chem_Per= (Chem/100)*100
Math_Per= (Math/100)*100
Total_per= (Phy_Per + Chem_Per + Math_Per)/3

if Total_per >= 40 and Phy_Per >= 33 and Chem_Per >= 33 and Math_Per >= 33:
    print(f'You are pass, with total percentage:{Total_per}')
else:
    print("Better luck next time")
