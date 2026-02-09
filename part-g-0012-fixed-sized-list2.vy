# pragma version ^0.4.0

ages: public(uint8[5])

@deploy
def __init__():

    self.ages = [17, 27, 37, 47, 97]

    # update

    self.ages[0] = 7
