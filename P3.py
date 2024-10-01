Pounds = float (input ('how many pounds would you like to purchase?\nInput number here: '))
GrossSales = Pounds * .99
if ((Pounds >= 10) and (Pounds <= 99.99)):
    DiscPerc = 0.10
    DiscStr = '10% Off'
else:
    if ((Pounds > 99.99) and (Pounds <= 999.99)):
         DiscPerc = 0.20
         DiscStr = '20% Off'
    else:
        if ((Pounds > 999.99) and (Pounds <= 9999.99 )):
            DiscPerc = 0.30
            DiscStr = '30% Off'
        else:
            if (Pounds >= 10000):
                DiscPerc = 0.40
                DiscStr = '--40% Off--'
            else:
                DiscPerc = 0
                DiscStr = '0%'
DiscAmm = GrossSales * DiscPerc
FinalAmm = GrossSales - DiscAmm
print ('Number of pounds:',Pounds,'\n Gross sales: ',GrossSales,'\n Discount: ',DiscStr,'\n Final Ammount: ',FinalAmm) 