tuplas=("Mateus", "python", "udemy")


print(tuplas [0])           #Mateus

print(tuplas [1])           #python        # serve para ver qual é o valor que esta nessa posição

print(tuplas [2])           #udemy



print(tuplas [0:2])              # vai mostrar o valor 0 e 1 pois desta forma ira cortar o valor dois 


print(tuplas [0:1])              # vai mostrar só o primeiro valor pois ira cortar o valor um


print(len (tuplas))        #3     # mostra a quantidade de objetos que tem dentro da tupla


print(tuplas+tuplas)        # repete a tupla 

print(tuplas*5)             # repete a quantidade de vez colocada no exemplo foi 5 então a tupla repetiu 5 vez


print("python" in tuplas)      # mostra se esse objeto existe dentro da tupla


lista= [1, 4, "Jorge"]
tuplas2 = tuple(lista)      # dessa forma corveti uma lista em tupla
print(tuplas2)
