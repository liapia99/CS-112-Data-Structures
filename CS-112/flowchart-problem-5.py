"""
File: Flowchart Program 5
Author: Julia Piascik
Date: Oct. 9, 2022
Purpose: Create a Program for Flowchart Question 5

"""
while True:
    
    idn = input("What is your ID number?")
    if idn == '-999':
        break
    #endif
    t1 = float(input("What is Test 1 score?"))
    t2 = float(input("What is Test 2 score?"))
    t3 = float(input("What is Test 3 score?"))
    final = float(input("What is Final Exam score?"))
    

    finalSC = (t1 * 0.2) + (t2 * 0.2) + (t3 * 0.2) + (final * 0.4)

    print("Your ID number is:",idn," and your final score is:", finalSC,"%.")

    

print("End of Program.")
