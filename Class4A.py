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
