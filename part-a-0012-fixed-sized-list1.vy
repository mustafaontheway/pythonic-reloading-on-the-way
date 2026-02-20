# pragma version ^0.4.0

ages: public(uint8[5])

@deploy
def __init__():

    self.ages[0] = 17
    self.ages[1] = 27
    self.ages[2] = 37
    self.ages[3] = 47
    self.ages[4] = 57

    # update

    self.ages[0] = 7
