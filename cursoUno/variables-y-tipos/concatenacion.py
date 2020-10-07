nombre = "Guillermo"
apellido = "Del Rio"
web = "visiondoble"

print(nombre, apellido, web)

#cocatenando
print(nombre + " " + apellido + " - " + web)

#otra manera de cocatenar
print(f"{nombre} {apellido} - mi web es: {web}")

#otra manera de usar la funcion "f"
numero = 31
edad = f"mi edad es {numero}"
print(edad)

########
print("hola mi nombre es: {} {} y mi web es: {} y {}".format(nombre, apellido, web, edad))

#ordenando el orden de las variables para el formato
print("hola mi nombre es: {a} {c} y mi web es: {b} y {d}".format( a=nombre, b=apellido, c=web, d=edad))
