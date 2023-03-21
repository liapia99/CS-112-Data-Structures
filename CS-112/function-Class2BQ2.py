# Julia Piascik 
import math 

def getArea(r):
  area = math.pow(r, 2) * math.pi
  return area

def getCircumference(r):
  cir = 2 * math.pi * r
  return cir 

print("=======================")
print("Area      Circumference")
print("=======================")
for i in range(1,11):
  print(i, round(getArea(i), 2), "\t    ", round(getCircumference(i), 2 ))

