# pragma version ^0.4.0

years: public(DynArray[uint16, 5])

@deploy
def __init__():

    self.years = [1998, 2007, 2011, 2018, 2020]

    #self.years.append(2000) # revert runs when we deploy the code

    self.years[1] = 1000
