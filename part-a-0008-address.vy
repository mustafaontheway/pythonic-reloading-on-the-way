# pragma version ^0.4.0

seller: public(address)

not_real_addr: public(address)

is_true: public(bool)


@deploy
def __init__():

    self.seller = 0x668001289b9da5a23840A6D4fa195d977f23BB3b

    self.not_real_addr = 0x0000000000000000000000000000000000000000

    self.is_true = self.not_real_addr == empty(address) # true
