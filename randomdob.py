import random

class RandomBirthday:
    def __init__(self):
        print('building random birthdays...')
        self.months = [1,2,3,4,5,6,7,8,9,10,11,12]
        self.days = []
        self.years = []
        self.build_days()
        self.build_years()

    def build_days(self):
        for i in range(28):
            self.days.append(i+1)
    
    def build_years(self):
        for i in range(1990,2001):
            self.years.append(i)
    
    def get_random(self):
        month = random.choice(self.months)
        day = random.choice(self.days)
        year = random.choice(self.years)
        return (month,day,year)
