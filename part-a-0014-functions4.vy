# pragma version ^0.4.0

my_num: public(uint256)

@external
@view
def plus_my_num(num: uint256) -> uint256:

    return self.my_num + num


@deploy
def __init__():

    self.my_num = 5000



