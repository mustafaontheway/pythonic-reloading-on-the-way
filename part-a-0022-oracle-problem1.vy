# pragma version ^0.4.0
# @ license: MIT  

MIN_FUND_AMOUNT_USD: public(immutable(uint8)) 

@deploy 
def __init__():

    MIN_FUND_AMOUNT_USD = 10

@external
@payable
def fund_me():

    assert msg.value >= MIN_FUND_AMOUNT_USD, "Fund amount at least $10" 


def withdraw_fund():

    pass


# Error => TypeMismatch:Cannot perform greater-or-equal between dislike types
