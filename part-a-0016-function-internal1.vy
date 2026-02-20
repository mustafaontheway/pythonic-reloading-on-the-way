# pragma version ^0.4.0

x: int256

y: int256

@internal
@view
def _sum_nums() -> int256:

    return self.x + self.y

@external
@view
def show_sum_result() -> int256:

    return self._sum_nums()


@deploy
def __init__(_x: int256, _y: int256):

    self.x = _x 
    self.y = _y



