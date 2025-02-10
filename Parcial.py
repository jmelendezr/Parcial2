##Desarrolar un programa que determine si en una lista no existen elementos repetidos.
n = int(input("¿Cuántos elementos tiene la lista? "))

lista = [None] * n  

for i in range(n):
    lista[i] = input("Ingresa un elemento: ")

if len(lista) == len(set(lista)):
    print("La lista no tiene elementos repetidos.")
else:
    print("La lista tiene elementos repetidos.")

## Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o mas vocales. Si la cadena existe debe impromirla y si no existe debe iprimir no existe.
def x(cadena): 
    vocales = "aeiouAEIOU"
    contador = sum(1 for letra in cadena if letra in vocales) 
    return contador >= 2

n = int(input("¿Cuántos elementos tiene la lista? "))

lista = [None] * n  
for i in range(n):
    lista[i] = input("Ingresa un elemento: ")

cadenas_vocales = [palabra for palabra in lista if x(palabra)]

if cadenas_vocales:
    print("Cadena encontrada:", cadenas_vocales[0])
else:
    print("No existe")

    

## Desarrollar un programa que dadas dos listas determine que elementos tiene la primera lista que no tenga la segunda lista.


## Desarrolla un algoritmo que calcule el promedio de un arreglo de reales
n = int(input("¿Cuántos numeros tiene el arreglo? "))

lista = [None] * n  
sum=0
for i in range(n):
    lista[i] = int(input("Ingresa un numero entero: "))
    sum+=lista[i]
print (lista)
print ("La suma de el arreglo es igual a: ",sum)
prom = sum / n
print("El promedio del arreglo es igual a: ",prom)

##Desarrollar un algoritmo que determine la mediana de un arreglo de enteros. La mediana es el numero que queda en la mitad del arreglo despues de ser ordenado