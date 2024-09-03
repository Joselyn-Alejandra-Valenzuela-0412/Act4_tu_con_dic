# ejemplo de uso de listas
misnovias=["Agripina","Anastacia","Maria"]
misNumeros=[666, 77, 10]
#mostrando mis novias
print(misnovias)
#mostrando mis numeros
print(misNumeros)
print("---accediendo a los elementos de la lista---")
print(misnovias[-2])
if "Ana" in misnovias:
    print("si, 'Ana' esta en la lista de mis novias")
else: 
    print("chale no eres mi novia")
    print("Numero de novias")
    Nnovias=len(misnovias)
    print(f"Numero de novias = {Nnovias}")
    thislist = ["apple", "banana", "cherry"]
    print("ciclo for en listas")
posicion=0
for medianaranja in misnovias:
    print(posicion,"",medianaranja)
    posicion +=1