#1. Logical Operators
def even(n):
    if n%2 != 0:
        print("Weird")
    if n%2 == 0: 
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif n >= 20:
            print("Not Weird")

#2. Arithmetic Operators
def numbers(a, b):
    print(a+b)
    print(a-b)
    print(a*b)

#3. Python Division
def pydiv(a, b):
    if b != 0:
        print(a // b)
        print(a / b)

#4. Loops
def loop(n):
    for i in range(n):
        print(i*i)

#5. Write a function
def is_leap(year):
    leap = False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap = True
    return leap

#6. Print Function
def sequence(n):
    i = 1
    while i <= n:
        #por defecto la función print tiene end=\n
        print(i, end="")
        i += 1

#8. List Comprehensions
def list_comp(x, y, z, n):
    lista = []
    for i in range( x + 1): 
        for j in range( y + 1): 
            for k in range(z + 1):
                if ( ( i + j + k) != n ):
                    lista.append([i, j, k])        
    print(lista)

#9. Find the Runner-Up Score!
def runnerup(n, arr):
    list = []
    for elem in arr:
        if elem not in list:
            list.append(elem)
    list.sort(reverse=True)
    print(list[1])

#10. Nested Lists
    

#1
#even(16)
#2
#numbers(3, 2)
#3
#pydiv(4, 3)
#4
#loop(5)
#5
#print(is_leap(2100))        
#6
#sequence(5)
#8
##x = int(input())
##y = int(input())
##z = int(input())
##n = int(input())
##list_comp(x,y,z, n)
#9
#runnerup(5, [2,3,6,6,5])
#10
