
miLista = ["Manzana", "Pera", "Uvas", "Naranjas"]
print(miLista[3])
print(miLista[0])

miLista[2]= "Sandia"

print(miLista)

for x in miLista: 
    print(x)

if "Uvas" in miLista:
    print("Existe la Uvas en la lista")

print(len(miLista))

miLista.append("Platano")

for x in miLista: 
    print(x)
print("----------")
miLista.remove("Sandia")
for x in miLista: 
    print(x)

print("----------")
miSegundaLista = miLista.copy
for x in miLista:
    print(x)

