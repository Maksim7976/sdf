#
# number = int(input("Введите число: "))
# if number % 2 == 0:
#     print(number, "Even number" )
# else:
#     print(number, "Odd number")
#
# num = int(input("Введите число: "))
# if num % 7 == 0:
#     print(num, "Number is multiple 7")
# else:
#     print(num, "Number is not multiple")
#
#
# num1 = int(input("Введите число: "))
# num2 = int(input("Введите число: "))
# if num1 > num2:
#     print(num1)
# else:
#     print(num2)
#
#
# num1 = int(input("Введите число: "))
# num2 = int(input("Введите число: "))
# op = input("")
# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "*":
#     print(num1 * num2)

# num1 = int(input("Введите число: "))
# num2 = int(input("Введите число: "))
# num3 = int(input("Введите число: "))
# op = input("")
# op2 = input("")
# if op == "+":
#     if op2 == "+":
#         print(num1 + num2 + num3)
#     else:
#         print(num1 + num2 - num3)
# else:
#     if op2 == "+":
#         print(num1 - num2 + num3)
#     else:
#         print(num1 - num2 - num3)

# number = int(input("Введите любое число"))
# s = 0
# for x in range(number + 1):
#     s+=x
# print(s)
# number = int(input())
# a = 1
# b = 1
# for x in range(number):
#     x = a + b
#     print(x)
# Задание первое
# a = int(input(""))
# b = int(input(""))
# c = 0
# for x in range(a,b+1):
#     c+=x
# print(c)

# # Задание второе
# a = int(input(""))
# f = 1
# for x in range(1,a + 1):
#     f = f * x
#     print(f)

# # Задание третье
# a = int(input(""))
#
# print("*" * a)

# a = int(input(""))
# for x in range(1,10):
#     print(a, "*", x, "=", a * x )
# a = int(input("Укажите сумму для конвертации валюты"))
# b = int(input("Укажите вашу валюту , 1 - Usd, 2 - Euro"))
# c = int(input("В какую валюту хотите конвертировать, 1 - Usd, 2 - Euro"))
# if b == 1 and c == 2:
#     print(a * 0.92783)
# elif b == 2 and c == 1:
#     print(a * 1.08)
# else:
#     print(input("Укажите верную валюту"))

# left = int(input("Введите первое число диапозона"))
# right = int(input("Введите второе число диапозона"))
# num = int(input("Введите число для проверки диапозона"))
# while num<left or num>right:
#     print("Введите повторно")
#     num = int(input("Введите число для проверки диапозона"))
# else:
#     for x in range(left,right):
#         print(x, end=" ")

# num = int(input("Введите 1 - определить количество цифр, 2 - Посчитать их сумму, 3 - Среднеарифмитическое, 4 - Узнать количество нулей в числе"))
# num1 = int(input("Введите цифры"))
# a = 0
# b = 0
#
# if num == 1:
#     while num1 > 0:
#         num1 = num1 // 10
#         a += 1
#     print("Количество цифр", a)
#
# if num == 2:
#     while num1 > 0:
#         a += num1 % 10
#         num1 = num1 // 10
#     print("Сумма чисел", a)
# if num == 3:
#     while num1 > 0:
#         a += num1 % 10
#         b += 1
#         num1 = num1 // 10
#     print(a / b)
# if num == 4:
#     while num1 > 0:
#         a += num1 % 10
#         if num1 % 10 == 0:
#             b += 1
#         num1 = num1 // 10
#     print(b)

# c = 0
# for x in range(10):
#     a = randint(1, 10)
#     b = randint(1, 10)
#     print(a, "*", b, "=")
#     if a * b == int(input("Введите произведение двух чисел")):
#         c += 1
#         print("Верно")
#         print("Ваш набранный балл",c)
#     else:
#         print("Неверно")
#
#

# size = 3
# for x in range(size):
#     print(x * "*")


# a = input("Введите строку")
# print(a[::-1])

# a = input("Введите строку")
# print(len(a))

# a = input("Введите строку")
# b = 0
# c = 0
# for x in range(len(a)):
#     if a[x].isdigit():
#         b += 1
#     elif a[x].isalpha():
#         c += 1
# print(b,"цифра")
# print(c, "Буква")
#

# a = input("Введите строку: ")
# b = input("Введите символ для поиска: ")
# c = 0
# for x in range(len(a)):
#     if b == a[x]:
#         c += 1
# print(c)

# a = input("Введите строку: ")
# b = input("Введите слово для поиска: ")
# с = 0
# print(a.count(b))

# string = "Привет всем, меня зовут Максим 123.как у вас дела.хорошего занятия, 123 привет"
# string = list(string)
# for x in string:
#     if string[x] == ".":


# negative = [random.randint(-100, 100) for x in range(100)]
# print(sum(negative))
# even = [random.randint(0,10) for x in range(10)]
# print(sum(even))
# a = [random.randint(0,10) for _ in range(10)]
#
# c = [a[x] if a[x] % 2 == 0 else 0 for x in range(len(a))]
# print((c))

# com = [random.randint(0,10) if x % 3 == 0 else 1 for x in range(10)]
# print(com)



# def func(to_print: str, name: str):
#     print(to_print, name)
# func("Priv",'medem')

# def sum(a:int,b:int):
#     return a+b
# print(sum(2,2))


# def func(text: str):
#     print(text)
#
#
# func(f"Dont let the noise of others options\n drown out your own inner voice\n Steve Jobs")
#
# def func(a: int, b: int):
#     for x in range(a,b):
#         if x % 2 != 0:
#             print(x)
# func(1,10)

# def func(a:int, b:int, c:int, d:int):
#     if a > b and a > c and a > d:
#         print(a,"Самое большое число")
#     elif b > a and b > c and b > d:
#         print(b,"Самое большое число")
#     elif c > a and c > b and c>d:
#         print(c,"Самое большое число")
#     elif d > a and d > b and d > c:
#         print(d,"Самое большое число")
# func(1,2,3,4)


# def func(nubmer):
#     c = 0
#     for x in range(nubmer):
#         c += x
#     return c
#
#
# print(func(10))
#


# def func(number: int):
#     a = [int(i) for i in str(number)]
#     if a[0] + a[1] + a[2] == a[3] + a[4] + a[5]:
#         return True
#     else:
#         return False
# print(func(123420))
#

#


# def func (number):
#     if number <= 1:
#         return False
#     for x in range(2, number):
#         if number % 2 == 0:
#             return False
#     return True
#
#
# print(func(17))



# # Написать рекурсивную функцию нахождения степени числа
# def pow (x, n):
#     if n == 0:
#         return 1
#     else:
#         return pow(x, n - 1) * x
# print(pow(10,2))


# Написать рекурсивную функцию, которая вычесляет сумму всех чисел в диапозоне от a до b. Пользователь вводит  a и b

# def sum(a,b):
#     if a > b:
#         return 0
#     else:
#         return sum(a + 1, b) + a
#
# a = int(input("Введите начало диапозона: "))
# b = int(input("Введите конец диапозона: "))
# print(sum(a,b))

# Написать рекурсивную функцию, которая выводит N звезд в ряд, число N задает пользователь
# # def star(n):
# #     if n == 0:
# #         return
# #     else:
# #         print("*", end="")
# #         star(n - 1)
# # n = int(input("Введи число N: "))
# # star(n)


# basketball_gamer = {
#     "name" : "Govno",
#     "surname" : "Privet",
#     "height" : 2
#
# }

# def func ():
#     print(basketball_gamer)
#     ask_user = int(input("У нас есть фамилия, имя и рост великого баскетболиста.\nВы можете добавить, удалить, искать или заменять данные.\nНажмите:\n1 - Добавить возвраст баскетболиста\n2 - Удалять\n3 - Искать\n4 - Замена данных\nВведите цифру: "))
#     if ask_user == 1:
#         pass
#     if ask_user == 2:
#         replace_name = input("Введите названия поля, которое хотите удалить: ")
#         del basketball_gamer[replace_name]
#     if ask_user == 3:
#         ask_user_find = int(input("Что вы хотите найти?\nНажмите:\n1 - Найти имя\n2 - Найти фамилию\n3 - Найти рост\nВведите цифру: "))
#         if ask_user_find == 1:
#             pass
#
#     if ask_user == 4:
#         replace = input("Введите название поля, которое хотите поменять: ")
#         new = input("Введите новое значение: ")
#         basketball_gamer[replace] = new
#
#     print(basketball_gamer)
# func()\

# with open("text", mode="r") as output_file:
#     lines = output_file.readlines()
#     print(lines)
# with open("text2", mode="w") as input_file:
#     for line in lines:
#         if len(line) >= 7:
#             input_file.write(line)

# with open("text", mode="r") as output_file:
#     line = output_file.readlines()
#     print(line)
# with open("text2", mode="w") as input_file:
#     for lines in reversed(line):
#         input_file.write(lines)


# class Human:
#     def __init__(self):

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        return int((self.x ** 2 + self.y ** 2) ** 0.5)

    def __imul__(self, other):
        self.x *= other
        self.y *= other
        return self

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)


    def normilize(self):
        self.x = self.x / len(self)
        self.y = self.y / len(self)


a = Vector(2, 10)
b = Vector(2, 10)
# a *= 2
print(len(a))
print(len(a + b))
a.normilize()
print(len(a))


