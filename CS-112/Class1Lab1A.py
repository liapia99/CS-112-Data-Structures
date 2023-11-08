"""
File: Class1Lab1A
Author: Julia Piascik
Date: Jan. 17, 2023
Basic Python Code 1 
"""
eggs = int(input("How many eggs?"))
dozen = eggs//12
egg = eggs%12
total = (dozen * 3.25) + (egg * 0.45)

print("You ordered",eggs,"eggs. That is",dozen,"dozen at $3.25 per dozen and",egg,"loose eggs at 45 cents each for a total of $",total)
print("End of Program.")

      
