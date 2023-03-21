#Julia Piascik
# Write a program that a. Generates 5000 random numbers and puts them in an array.b. Sorts the numbers using any sorting technique (Selection sort is fine, but you can tryanother one).c. Ask the user for a number between 0 and 20,000 and search for it in your sorted arrayusing a simple linear search. Is this a good idea?d. Ask the user for a number between 0 and 20,000 and search for it in your sorted arrayusing a binary search.Hint: To generate random numbers you need to include this module:import randomTo get a random number w :w = random.randint(0,20000)This will give w a random value between 0 and 20,000

#Julia Piascik
#Binary Search with Merge Sort 
import random
import array 

def binarySearch(A, x):
    start = 0
    end = len(A) - 1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == x:
            return mid
        elif A[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def mergeSort( A ):
  if len(A) > 1:
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]

        mergeSort(left)
        mergeSort(right)
    
        i = 0
        j = 0
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              A[k] = left[i]
              i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            A[k]=right[j]
            j += 1
            k += 1
  return A
    
    
#main 
      
A = array.array('i', [])

for i in range(0,5000):
  w = random.randint(0,20000)
  A.append(w)
  
  
x = -1
while x <= 0:
  x = int(input("Enter in a number between 0 and 20,000 to look for:"))

sort = mergeSort(A)

finalResult = binarySearch(sort, x)

if finalResult != -1:
    print("Number found at index", finalResult)
else:
    print("Number not found in array.")


#Linear Search --------------------------------------------------------------------------------------
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

