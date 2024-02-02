
persona={
    "nombre":"Pedro",
    "apellidos":"Picapiedra",
    "empleo":"Obrero"
}

print(persona)
print("-----------------")

print(persona["nombre"])
print("-----------------")

print(persona.get("apellidos"))
print("-----------------")

print(persona.get("empleo"))
persona["empleo"]= "Chofer"
print(persona.get("empleo"))
print("-----------------")

for x in persona:
    print(x)
    print(persona[x])
print("-----------------")

for x in persona.values():
    print(x)
print("-----------------")

for x, y in persona.items():
    print(x,y)
print("-----------------")

print("Exite la llave nombre", "nombre" in persona)
print("Exite la llave puesto", "puesto" in persona)
print("-----------------")

print("Elemento en el diccionario", len(persona))
print("-----------------")

persona["id"]= 123
for x in persona:
    print(x)
print("-----------------")

persona.pop("id")
for x in persona:
    print(x)
print("-----------------")

persona.popitem
for x in persona:
    print(x)
print("-----------------")

del persona["apellidos"]
for x in persona:
    print(x)
print("-----------------")

persona.clear()
print("Elementos en el dioccionario", len(persona))
print("-----------------")

persona={
    "nombre":"Pedro",
    "apellidos":"Picapiedra",
    "empleo":"Obrero"
}
persona2 = persona.copy()
for x in persona2:
    print(x)
print("-----------------")

persona3= dict(persona)
for x in persona3:
    print(x)
print("-----------------")