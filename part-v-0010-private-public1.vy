# pragma version 0.4.0
# @license MIT


year: public(uint16)

age: uint8 # private


@deploy
def __init__():

    self.year = 2000

    self.age = 17

