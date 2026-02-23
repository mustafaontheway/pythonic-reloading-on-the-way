# pragma version ^0.4.0
# @ license: MIT  

my_age: public(uint16)

@deploy
def __init__():

    self.my_age = 100

@external 
def plus(a: uint16) -> uint16:

    assert 100 > 22, "100 > 22"

    self.my_age += a

    return self.my_age 


