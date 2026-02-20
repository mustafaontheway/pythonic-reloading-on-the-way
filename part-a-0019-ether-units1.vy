# pragma version ^0.4.0

ether_to_wei: public(bool)

gwei_to_wei: public(bool)


@deploy
def __init__():

    self.ether_to_wei =  as_wei_value(1, "ether") == 10 ** 18

    self.gwei_to_wei = as_wei_value(1, "gwei") == 10 ** 9
