# pragma version ^0.4.0

years: public(DynArray[uint16, 5])

@deploy
def __init__():

    self.years.append(2018)
    self.years.append(2020)
    self.years.append(2026)

    self.years.pop()

    #self.years = []
