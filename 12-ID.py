# Обработчик исключений. Конструкция "try - except"

# x = 0
# while x == 0:
#     try:
#         x = int(input("Ввидите число: "))
#         x += 5
#         print("Ура, вы ввили число", x)
#     except ValueError:
#         print("Ввидите лучше число!")

# 2

try:
    y = 5 / 1
    y = int(input())
except ZeroDivisionError:
    print("Деление на ноль!")
except ValueError:
    print("Вы ввели что-то не так")
else:
    print("else")
finally:
    print("Finally")






