# pragma version ^0.4.0

yearly_sales: public(uint128)

@external
def calculate_age(birth_year: uint16):

    pass

@external
@view
def get_yearly_sales() -> uint128:

    return self.yearly_sales

@deploy
def __init__():

    self.yearly_sales = 412_6375_900

