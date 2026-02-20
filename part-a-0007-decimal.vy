# pragma version ^0.4.0

# must be compiled with --enable-decimals

interest_rate: public(decimal)


@deploy
def __init__():

    self.interest_rate = 0.12
