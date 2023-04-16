# НЕМНОГО ООП

class Cat:
    name = None
    age = None
    isHappy = None

    def set_data(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, "age", self.age, ". Happy:", self.isHappy)

# Обращение через метод
cat_1 = Cat()
cat_1.set_data("Barsik", 3, True)

# Оращение без метода
# cat_1.name ="Barsik"
# cat_1.age = 3
# cat_1.isHappy = True

# Обращение через метод
cat_2 = Cat()
cat_2.set_data("Jopen", 2, False)


# Оращение без метода
# cat_2.name = "Jopen"
# cat_2.age = 2
# cat_2.isHappy = False

cat_1.get_data()
cat_2.get_data()










