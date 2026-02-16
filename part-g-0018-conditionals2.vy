# pragma version ^0.4.0

@external
@pure
def calculate_premium(sales: uint256) -> uint16:

    if sales >= 5_000_000:

        return 10_000 

    elif sales >= 1_000_000:

        return 2_500 

    else:

        return 0
