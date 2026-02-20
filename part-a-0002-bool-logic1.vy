# pragma version ^0.4.0

x: public(bool)

y: public(bool)

result1: public(bool)
result2: public(bool)
result3: public(bool)

@deploy
def __init__():

    self.x = True

    self.y = False

    self.result1 = self.x and self.y

    self.result2 = self.x or self.y

    self.result3 = not self.x
