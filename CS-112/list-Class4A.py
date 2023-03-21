# Write a program to ask the user to enter 10 integers and append them one by one to an emptylist 2. Print it out. 3. Print out the sum, min, max and length of the list. 4. Shuffle the list. 5. Print out the shuffled list. 6. Sort the list. 7. Print out the sorted list. 8. Create a new list which has the same data with duplicates removed.Hint: import random for the shuffling,To shuffle:random.shuffle(List)

#Julia Piascik

import random

userList = []

for i in range(0,10):
  x = -1
  while x <= 0:
    x = int(input("Enter an integer:"))
    userList.append(x)
print(userList)


print("The sum is:", sum(userList))
print("The maximum is:", max(userList))
print("The minimum is:", min(userList))
print("The length of the list is:", len(userList))

print("The list before it is shuffled is:", userList)
random.shuffle(userList)
print("The shuffled list is:", userList)

userList.sort()
print("The sorted list is:", userList)

newUserList = list(set(userList))
print("Duplicates found and deleted:", newUserList)

