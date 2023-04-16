# Менеджер "With...as"

try:
    with open("Test/text.txt", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("Файл не найден!")















