# pragma version ^0.4.0

@internal
@pure
def _sum_nums(x: int256, y: int256) -> int256:

    return x + y

@external
@pure
def show_sum_result(a: int256, b: int256) -> int256:

    return self._sum_nums(a, b)
