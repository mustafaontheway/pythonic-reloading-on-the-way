# pragma version ^0.4.0

l1: public(int8[5])

l2: public(int8[5])

comparision: public(bool)


@deploy
def __init__():

    self.l1[2] = 100

    self.l2 = [0, 0, 100, 0, 0]

    self.comparision = self.l1[0] == self.l2[0] # true
