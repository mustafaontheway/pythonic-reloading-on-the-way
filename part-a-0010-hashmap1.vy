# pragma version ^0.4.0

# employee ID and Ethereum salary

salary_ethereum_by_id: public(HashMap[uint8, uint8])

@deploy
def __init__():

    self.salary_ethereum_by_id[97] = 3

    self.salary_ethereum_by_id[65] = 5
