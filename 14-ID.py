# Модули в языке Python

# 1

# import datetime as d, sys, os, platform  # as d - добовляет псевдоним в данном случае это d
# from math import sqrt as s, ceil  # as s - as d - добовляет псевдоним в данном случае это s
# Если прописывать только import... в таком случае импортируется модуль целяком
# Если прописывать from...import... в таком случае вытягиваются отдельные функции

# print(d.datetime.now().time())
# print(d.datetime.now().time().hour)
# print(d.datetime.now().date())
# print(sys.path)
# print(platform.system())
# print(ceil(s(625)))

# 2 Создания своего модуля

# import MyModule as my
#
# print(my.name)
# my.hello()

# from MyModule import add_three_numbers as add
#
# print(add(5, 3, 0))

# 3

# import cowsay as c
# # c.cow("Hi man")
# c.dragon("Если что я тоже тмогу вам тут такого на тестировать XD, XD, XD...")











