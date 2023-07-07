""" Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с помощью рекурсии. """

def exponention_a(a,b, c = 1):
    c = a // c
    if b != 1:
        return exponention_a(c * a, b - 1, c)
    return a


print(exponention_a(2,3))
