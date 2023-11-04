import random

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_rapair()
            return
        self.job = Job(job_list)

    # def eat(self):
    #     if self.home.foot <= 0:
    #         self.shoping("food")

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def clean_home(self):
        self.home.mess = 0
        self.gladness -= 5

    def chill(self):
        self.home.mess += 5
        self.gladness += 10

class House:
    def __init__(self):
        self.mess = 0
        self.food = 0

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move!")
            return False


class Job:
    def __init__(self):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladnesss_less = job_list[self.job]['gladness_less']

job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "c++ developer": {"salary": 60, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 15}
}

brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumpition": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumpition": 10},
    "Volvo": {"fuel": 80, "strength": 150, "consumpition": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14}
}