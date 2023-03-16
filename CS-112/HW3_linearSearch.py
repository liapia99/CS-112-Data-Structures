#Julia Piascik
#Linear Search with Sort()

import random
import array 

def linearSearch(A, x):
    for i in range(len(A)):
        if A[i] == x:
            return i
    return -1

#main 
      
A = array.array('i', [])

for i in range(0,5000):
  w = random.randint(0,20000)
  A.append(w)
  sorted(A)
  
x = -1
while x <= 0:
  x = int(input("Enter in a number between 0 and 20,000 to look for:"))


finalResult = linearSearch(A, x)


if finalResult != -1:
    print("Number found at index", finalResult)
    
else:
    print("Number not found in array.")
