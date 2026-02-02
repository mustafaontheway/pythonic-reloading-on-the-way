# pragma version 0.4.0
# @license MIT

is_completed: public(bool)

ready: public(bool)

comparision_1: public(bool)

comparision_2: public(bool)

comparision_3: public(bool)

comparision_4: public(bool)

@deploy
def __init__():

    self.is_completed = False

    self.ready = True

    self.comparision_1 = 5 > 2

    self.comparision_2 = 5 != 5

    self.comparision_3 = (5 > 2) and True

    self.comparision_4 = False or True
