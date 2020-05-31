def collatz(number):
    while number > 1:
        if number % 2 == 0:
            number = number // 2
            print(number)
        else:
            number = (number * 3) +1
            print(number)

print("Esta funcion recibe un numero e imprime la serie de kollatz. Diigite un numero para empezar")
try:
    input = int(input())
    collatz(input)
except ValueError:
    print("Valor de entrada incorrecto")
