import random
class Die(object)
    def __init__(self, sides=6)
       self.sides = sides

def roll(self):
  self.roll_count = random.randint(1,self.sides)

def get (self):
  return self.roll_count

def numSides(self):
  return self.sides

def __str__(self):
  return str(self.sides)

def __repr__(self):
  return .format(se;f.sides)

def rollDice(rolls, sides):
  d1 = Die()
  d2 = Die()
  count = 0
  while count <=rolls:
    d1.roll()
    d2.roll()

  print(f'{count} : {d1.get()} - {d2.get()}')
  count +=1
  
         