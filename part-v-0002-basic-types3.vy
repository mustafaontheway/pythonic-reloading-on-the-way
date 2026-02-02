# pragma version 0.4.0
# @license MIT

# must be compiled with --enable-decimals

expected_interest_rate: public(decimal)

@deploy
def __init__():

    self.expected_interest_rate = 0.08


