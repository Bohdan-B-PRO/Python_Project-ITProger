# СЛОВАРИ

# 1

# counrty = {(5, 6): 3}
# print(counrty[(5,6)]) # В словарях обращение к элемнту идёт через ключи, в качестве ключа может быть
#                       # любой тип данных в том числе картеж

# 2

# country_1 = {"code": "RU", "name": "Russia", "population": 144}
# country_2 = dict(code="RU", name="Russia")
# print(country_1["name"])
# print(country_1.items())
# for key, value in country_1.items(): # .items - добовляется если нужно перебрать значения
#     print(key, " - ", value)

# 3

# country_3 = {"code": "RU", "name": "Russia", "population": 144}

# print(country_3.get("name")) # .get - позваляет получить определённое значение
# country_3.clear()
# country_3.pop("name") # .pop - удаляет определённый элемент
# country_3.popitem() # .popitem - удаляет последний элемент

# print(country_3.keys()) # .keys - позволяет получить только ключи
# print(country_3.values()) # .values - позволяет получить только знаяения
# country_3["code"] ="None" # таким образом можно менять значения в ключах
# print(country_3.items()) # .items - позволяет получить и элемент и ключи

# 4

# person = {
#     'user_1':{
#         "first_name ": "John",
#         "last_name": "Marley",
#         "age": 45,
#         "address": ["г. Москва", "ул. Какая-то", "45"],
#         "grades": {"math": 5, "physics": 3}
#     },
#     "user_2":{
#         "first_name ": "Bohdan",
#         "last_name": "Big_BOSS",
#         "age": 25,
#         "address": ["г. Москва", "ул. Какая-то", 45],
#         "grades": {"math": 5, "physics": 3}
#
#     }
# }
#
# print(person["user_1"]["address"][1]) # так можно вытянуть вложеность с кортежа
# print(person['user_2']["last_name"])





