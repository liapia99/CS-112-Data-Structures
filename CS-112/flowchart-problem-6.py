"""
File: Flowchart Program 6
Author: Julia Piascik
Date: Oct. 9, 2022
Purpose: Create a Program for Flowchart Question 6

"""

ans = 'Y'

while ans == 'Y' or ans =='y':
    
    A = input("What is the value of A? ")
    A = int(A)

    B = input("What is the value of B? ")
    B = int(B)


    if A > B:
        print("Larger")
    else:
        print("Not Larger")
    #endif

    ans = input("Do again? (Y/N)")


print("End of Program.")





