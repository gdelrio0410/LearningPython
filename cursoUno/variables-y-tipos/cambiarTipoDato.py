texto = "soy un texto"
numero = 7854

#Error solo se pueden concatenar strings no se pueden cacatenar strings con enteros
#print(texto + " " + numero)

print(texto + " " + str(numero))

print(numero)
print(type(numero))

numero = str(numero)
print(numero)
print(type(numero))

numero = float(numero)
print(numero)
print(type(numero))

numero = int(numero)
print(numero)
print(type(numero))