""" Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с помощью рекурсии. """
#
# def exponention_a(a, b):
#     if b != 1:
#         return a * exponention_a(a, b - 1)
#     return a
#
#
# print(exponention_a(3, 5))

# solution 2 ===============================================

def recr(a,b,res = 1):
    if b == 0:
        return res
    return recr(a, b -1, res * a)

a = int(input("Введите число А : "))
b = int(input("Введите число B : "))
print(recr(a,b))