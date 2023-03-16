############################
# File: hamburger6.py
# Author: Julia Piascik
# Date: September 8th, 2022
############################

# print headings

print("\n Hamburger 6 Post-test Loop....")
print("===============================\n")

# post-test loop
while True:

    # input order and amount receivedd from customer
    noBigHugo = input("\n Enter amount of Big Hugo burgers desired ==> ")
    noDoubCheese = input("\n Enter amount of Double Cheese burgers desired ==> ")
    noCheese = input("\n Enter amount of Cheese burgers desired ==> ")
    amtGiven = input("\n Enter dollar amount given by customer ==$")

    # constant declarations
    priceBigHugo = 3.27
    priceDoubCheese = 2.50
    priceCheese = 1.55;

    # calc cost of burgers
    costBigHugo = float(noBigHugo) * (priceBigHugo)
    costDoubCheese = float(noDoubCheese) * (priceDoubCheese)
    costCheese = float(noCheese) * (priceCheese)

    # calc total cost of all burgers
    total = costBigHugo + costDoubCheese + costCheese

    # calc change from 20 dollars
    change = float(amtGiven) - total

    # output cost and change
    print("\n The total cost of these burgers is $", total)
    print("\n Your change from", amtGiven, "dollars is $", change)

    # prompt the user for more orders
    answer = input("\nDo again? (Y/N)")
    if answer == 'N' or answer == 'n':
        break
    #endif
# end while loop
print("\n ... end of job! ... \n")
    

# end main

    
    
