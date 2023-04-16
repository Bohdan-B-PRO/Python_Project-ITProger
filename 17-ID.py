# НАСЛЕДОВАНИЕ, ИНКАПСУЛЯЦИЯ, ПОЛИМОРФИЗМ

class Building:
    __year = None
    __city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print("Year", self.year, "City", self.city)

class School(Building):
    pupils = 0

    def __init__(self, pipils, year, city):
        super(School, self).__init__(year, city)
        self.pupils = pipils

    def get_info(self):
        super().get_info()
        print("Pupils:", self.pupils)

class House(School):
    pass

class Shop(House):
    pass


school = School(100, 2000, "Moscow")
school.get_info()
houses = House(20,2000, "Moscow")
shops = Shop(2,2000, "Moscow")
shops.get_info()


















