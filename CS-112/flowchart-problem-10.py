"""
File: Flowchart Program 10
Author: Julia Piascik
Date: Oct. 9, 2022
Purpose: Create a Program for Flowchart Question 10

"""
x = input("Input a number ==>")

min = x
max = x
    
if x == '-999':
    print("List is null, no max and no min.")
else:
    while True:
        x = input("Input a number ==>")
        if x == '-999':
            break
            print("Max=",max,"Min=",min)
        else: 
            if x > max:
                max = x
            else:
                if x < min:
                    min = x
                #endif    
            #endif
        #endif  
#endif

print("Max=",max,"Min=",min)
print("End of Program.")

