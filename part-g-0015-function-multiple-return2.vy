# pragma version ^0.4.0

x: public(int256)

y: public(int256)

@external
def set_nums(_x: int256, _y: int256):

    self.x = _x 
    self.y = _y

@external
@view
def sum_or_subtract() -> (int256, int256):

    return (self.x + self.y, self.x - self.y)
