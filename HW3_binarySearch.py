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
