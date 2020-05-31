animales = ['perro', 'gato', 'loro', 'iguana', 'tortuga']
for idx, item in enumerate(animales):
    print('indice: '+str(idx)+' contenido: '+item) 
animales.sort(reverse=True)
print(animales)

spam = [0, 1, 2, 3, 4, 5]
cheese = spam # The reference is being copied, not the list.
cheese[1] = 'Hello!' # This changes the list value.
print(id(cheese))
print(id(spam))
print(spam)
print(cheese) # The cheese variable refers to the same list.

new_list = ['a', 'b', 'c', 'd']
print(new_list[int(int('3' * 2) // 11)]) #imprime 0
print(new_list[-1]) #imprime 'd'
print(new_list[:2]) #imprime a,b
