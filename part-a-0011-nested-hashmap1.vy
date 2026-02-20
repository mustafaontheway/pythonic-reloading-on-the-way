# pragma version ^0.4.0

# department name, employee ID and Ethereum salary

salaries_by_departments: public(HashMap[String[20], HashMap[uint8, uint8]])

@deploy
def __init__():

    self.salaries_by_departments["FinTech"][17] = 3
