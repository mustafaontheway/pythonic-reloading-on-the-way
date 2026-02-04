# pragma version 0.4.0
# @license MIT

@external
@pure
def sum_or_mult(x: uint256, y: uint256, z: uint256) -> (uint256, uint256):

    return (x + y + z, x * y * z)
