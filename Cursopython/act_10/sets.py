
miSet = {"Manzana", "Pera", "Sandia"} #No tienen orden
print(miSet)
print("------------")

print(len(miSet))
print("------------")

for x in miSet:
    print(x)
print("------------")

print("Buscamos Sandia")
print("Sanidia" in miSet)

print("Buscamos Platano")
print("Platano" in miSet)

miSet.update(["Platano", "Mango", "Guayaba"])

for x in miSet:
    print(x)
print("------------")

miSet.add("Cerveza")

for x in miSet:
    print(x)
print("------------")

x = miSet.pop()
print(x)
print("------------")

for x in miSet:
    print(x)
print("------------")

miSet.clear()
print(len(miSet))
print("------------")

del miSet
print("Con del eliminamos el set")
print("------------")