############################
# File: hamburger7.py
# Author: Julia Piascik
# Date: September 8th, 2022
############################

# print headings

print("\n Hamburger 7 ...")
print("===============================\n")

                # declaration of price constants

costHamburger = 1.75;
costCheese = 0.56;
costDrink = 0.99;
costFrenchFries = 1.56;

                # input order
noHamburgers = input("\n Enter amount of hamburgers desired ==>")
cheese              =input("\nDo you want cheese on it? (Y/N) ==>")

                # decide whether cheese is required
if cheese =='Y' or cheese == 'y':
    noCheeses = input("\n How many with cheese?, 0 for none==>")
else:
    noCheeses = 0
    #endif

                # input number of drinks and french fries
noDrinks = input("\n Enter amount of drinks desired, 0 for none==>")
noFrenchFries = input("\n Enter amount of french fries desired, 0 for none==>")
   

                # calc and print cost of hamburgers
hambCost = float(noHamburgers) * costHamburger
print("... cost of burgers is $", hambCost)

                # calc and print cost of cheese
cheeseCost = float(noCheeses) * costCheese
print("... cost of cheese is $", cheeseCost)


                # calc and print cost of drinks
drinkCost = float(noDrinks) * costDrink
print("... cost of drinks is $", drinkCost)

                # calc and print cost of rench fries
ffCost = float(noFrenchFries) * costFrenchFries
print("... cost of French Fries is $", ffCost)


                # calc and print total cost
totalCost = hambCost + cheeseCost + drinkCost + ffCost
print("... total cost is $", totalCost)

                # input payment amount
amtGiven = input("\n Amount tended:$")

                # input payment amount
change = float(amtGiven)-totalCost
    

                # output change
print("\n Your change from", amtGiven," dollars is $",change)
    
print("\n\t Thank you!")

    # end main
