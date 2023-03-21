#Julia Piascik 

b = {  "name" : "Banana",  "price" : 1.5}
a = {  "name" : "Apple",  "price" : 2.3}
o = {  "name" : "Oranges",  "price" : 4.5}
c = {  "name" : "Cherry",  "price" : 6}
fruit_price = {  "b" : b,  "a" : a, "o" : o, "c" : c}

b = { "pound" : 35}
a = { "pound" : 42}
o = { "pound" : 40}
c = { "pound" : 12}
fruit_stock = {  "b" : b,  "a" : a, "o" : o, "c" : c}

print("Fruit           Price           Stock \n")
print(fruit_price["b"]["name"], '\t','\t', fruit_price["b"]["price"], '\t', '\t',fruit_stock["b"]["pound"])
print(fruit_price["a"]["name"], '\t','\t', fruit_price["a"]["price"], '\t','\t', fruit_stock["a"]["pound"])
print(fruit_price["o"]["name"], '\t', fruit_price["o"]["price"], '\t','\t', fruit_stock["o"]["pound"])
print(fruit_price["c"]["name"], '\t','\t', fruit_price["c"]["price"], '\t','\t', fruit_stock["c"]["pound"],"\n")

bt = (fruit_price["b"]["price"]*fruit_stock["b"]["pound"])
at = (fruit_price["a"]["price"]*fruit_stock["a"]["pound"])
ot = (fruit_price["o"]["price"]*fruit_stock["o"]["pound"])
ct = (fruit_price["c"]["price"]*fruit_stock["c"]["pound"])
print("Total value of bananas in the shop is $", bt,"dollars.")
print("Total value of apples in the shop is $", at,"dollars.")
print("Total value of oranges in the shop is $", ot,"dollars.")
print("Total value of cherries in the shop is $", ct,"dollars.")

whole = (bt+at+ot+ct)
print("Total value of the whole shop is $", whole,"dollars.")
