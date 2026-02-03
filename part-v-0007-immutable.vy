# pragma version 0.4.0
# @license MIT

INITIAL_CAPITAL: public(immutable(uint32))

FOUNDER: public(immutable(String[20]))

@deploy
def __init__():

    INITIAL_CAPITAL = 150_000

    FOUNDER = "Mustafa Buyukdereli"
