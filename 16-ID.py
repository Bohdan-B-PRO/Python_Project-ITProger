# КОНСТРУКТОРЫ В ООП

class Cat:
    name = None
    age = None
    isHappy = None

    def __init__(self, name = None, age = None, isHappy = None):
        self.set_data(name, age, isHappy)
        self.get_data()

    def set_data(self, name = None, age = None, isHappy = None):  # None - используется когда нужно
        self.name = name    # переопределение методов (а разница между методом и функциией в том что
        self.age = age      # функция в не class, а метод в нём) для того чтобы можнно было не передавать
        self.isHappy = isHappy  # то или иное значение

    def get_data(self):
        print(self.name, "age", self.age, ". Happy:", self.isHappy)

cat_1 = Cat("Barsik", 3, True)  # Так передаются данные через коструктор
# cat_1.set_data("Barsik", 3, True)
cat_1.set_data()

cat_2 = Cat("Jopen", 2, False)  # Так передаются данные через коструктор
# cat_2.set_data("Jopen", 2, False)

# cat_1.get_data()
# cat_2.get_data()