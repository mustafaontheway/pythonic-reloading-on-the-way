# pragma version ^0.4.0

@external
@pure
def sum_or_subtract(x: int256, y: int256) -> (int256, int256):

    return (x + y, x - y)
