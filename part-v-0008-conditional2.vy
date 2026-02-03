# pragma version 0.4.0
# @license MIT

# not e real func! 

@external
@pure
def calculate_sales_premium(sales: uint64) -> uint64:

    if sales > 1_000_000 and sales < 5_000_000:

        return 10_000

    elif sales < 1_000_000 and sales > 500_000:

        return 2_000

    else:

        return 0
