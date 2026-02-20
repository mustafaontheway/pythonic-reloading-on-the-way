# pragma version ^0.4.0

# from uint8 to uint256
# positive or zero

age: public(uint8)

year: public(uint16)

sales: public(uint64)

total_yearly_export: public(uint256)

@deploy
def __init__():

    self.age = 17
    self.year = 2020
    self.sales = 312_625_000
    self.total_yearly_export = 22_621_4654_900
