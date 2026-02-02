# pragma version 0.4.0
# @license MIT

# from int8 to int256
# from uint8 to uint256

age: public(uint8)

diff: public(int16)

first_year: public(uint16)

profit_or_loss: public(int64)

yearly_sales: public(uint128)

@deploy
def __init__():

    self.age = 17

    self.diff = -10

    self.first_year = 2018

    self.profit_or_loss = 4_714_310

    self.yearly_sales = 300_412_654


