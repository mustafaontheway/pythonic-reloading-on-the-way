# pragma version 0.4.0
# @license MIT

voter_ages: public(uint8[5])

@deploy
def __init__():

    self.voter_ages[0] = 40
    self.voter_ages[1] = 26
    self.voter_ages[2] = 68
    self.voter_ages[3] = 54
    self.voter_ages[4] = 37
