# pragma version ^0.4.0
# @ license: MIT  

@external
@payable
def fund_me():

    assert msg.value >= as_wei_value(2_000_000, "wei"), "Fund amount at least 2.000.000 Wei" 
