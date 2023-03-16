############################
# File: hamburger8.py
# Author: Julia Piascik
# Date: September 8th, 2022
# Purpose: Nested if statements - none 3 if statements and 3 #endifs
############################

# print headings

print("\n ... Hamburger 8 ...")
print("===============================\n")


# prompt user for order

qty = input("\n Enter the number of hamburgers desired ==>")
hamburgerType = input("\n Type? Enter C for cheese, P for plain, or D for Double==>")

# determine cost of hamburgers
if hamburgerType == 'C' or hamburgerType =='c':
    cost = 2.79
else:
    if hamburgerType == 'P'or hamburgerType =='p':
        cost = 2.05
    else:
        if hamburgerType == 'D'or hamburgerType =='d':
            cost = 3.59
        else:
            print("Wrong type! Run again!")
            cost = 0.0
#endif
#endif
#endif

# calc total
total = cost * float(qty)
# output total cost
print("\n Total cost is ==>$", total)

#prompt user for amount tended
amtGiven = input("\n Enter amount tended ==> $")

# calc and print change
change = float(amtGiven) - total

print("\n Your change is $",change)
    
print("\n\t Thank You!")

#endmain
