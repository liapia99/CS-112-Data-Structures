#Julia Piascik

import array


A = array.array('i', [])

for i in range(0,10):
  x = int(input("Enter an integer:"))
  A.append(x)
print(A)
# end for
sum = 0
for mem in A:
  print(mem)
  sum = sum + mem
print("The sum is:", sum)
# end for

average = sum / 10
print("The average is:", average)

print("Numbers that are bigger than the average are:")
for mem in A:
  if mem > average:
    print(mem, end=", ")
  # end if
# end for

max = max(A)
print("The maximum is:", max)

min = min(A)
print("The minimum is:", min)

