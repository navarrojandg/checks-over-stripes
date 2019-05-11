import csv
import random

class RandomNames:
    def __init__(self):
        self.names = []
        self.build_names_list()

    def build_names_list(self):
        print('building list of names...')
        with open('Names_2010Census.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar="|")
            for row in reader:
                self.names.append(row[0])
    
    def get_random(self):
        first = ''
        last = ''
        while first == last:
            first = random.choice(self.names).lower().capitalize()
            last = random.choice(self.names).lower().capitalize()
        return (first,last)
