

def tempConvert(f):
  c = (5.0/9.0) * (f–32)
  return c 


print("=======================")
print("Fahrenheit      Celsius")
print("=======================")
for i in range(50,101,5):
  celsius = tempConvert(i)
  print(i, "\t    ", round(celsius,1))
