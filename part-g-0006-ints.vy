# pragma version ^0.4.0

# from uint8 to uint256
# positive, negative or zero

age: public(int8)

profit_or_loss: public(int16)

total_yearly_export: public(int256)

@deploy
def __init__():

    self.age = 0
    self.profit_or_loss = -2025
    self.total_yearly_export = 22_621_4654_900
