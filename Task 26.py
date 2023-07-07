""" Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с помощью рекурсии. """
#
def exponention_a(a, c, b ):
    if b != 1:
        return exponention_a(c * a, c,  b - 1)
    return a


print(exponention_a(3, 3, 5))

