# pragma version 0.4.0
# @license MIT

birth_years: public(DynArray[uint16, 5])


@deploy
def __init__():

    self.birth_years = [2000, 1990, 1980, 1970, 1960]

    #self.birth_years.append(1950) # revert
