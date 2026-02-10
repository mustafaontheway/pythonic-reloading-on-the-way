# pragma version ^0.4.0

my_num: public(uint256)

@external
def change_and_add(add_num: uint256, new_num: uint256) -> uint256:

    self.my_num = new_num

    return self.my_num + add_num
