# pragma version ^0.4.0

x: public(int8)

y: public(int8)

z: public(int8)

result1: public(bool)
result2: public(bool)
result3: public(bool)

@deploy
def __init__():

    self.x = 10

    self.y = 12

    self.z = -10

    self.result1 = self.x >= self.z

    self.result2 = self.x >= self.z and self.x == self.y

    self.result3 =self.x >= self.z or self.x == self.y
