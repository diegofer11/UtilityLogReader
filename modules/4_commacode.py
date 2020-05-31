def list_string(lista):
    cadena = ''
    if len(lista) == 0:
        return cadena
    else:
        lista[-1] = 'and '+lista[-1]
        cadena = ', '.join(lista)
    return cadena

spam = ['apples', 'bananas', 'tofu', 'cats']
print(list_string(spam))
