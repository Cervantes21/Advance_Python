import random

class Borracho:
    
    def __ini__(self, name):
        self.name = name
        

class BorrachoTradicional(Borracho):
    
    def __init__(self, name):
        super().__init__(name)
        
    def camina():
        return random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])

