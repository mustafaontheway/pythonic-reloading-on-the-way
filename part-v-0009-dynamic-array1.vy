# pragma version 0.4.0
# @license MIT

birth_years: public(DynArray[uint16, 5])


@deploy
def __init__():

    self.birth_years.append(2000)
    self.birth_years.append(1970)
