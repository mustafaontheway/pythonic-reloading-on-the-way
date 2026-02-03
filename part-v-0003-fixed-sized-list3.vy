# pragma version 0.4.0
# @license MIT

voter_ages: public(uint8[5])

@deploy
def __init__():

    self.voter_ages = [77, 65, 42, 64, 19]

    self.voter_ages[1] = 20
