# pragma version ^0.4.0

base_year: public(uint16)

@external
def set_year(_year: uint16):

    self.base_year = _year

@external
@view
def get_year() -> uint16:

    return self.base_year
