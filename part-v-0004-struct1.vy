# pragma version 0.4.0
# @license MIT

struct Employee:

    name: String[50]
    birth_year: uint16
    salary_usd: uint16

ceo_mustafa: public(Employee)

@deploy
def __init__():

    self.ceo_mustafa.name = "Mustafa Buyukdereli"
    self.ceo_mustafa.birth_year = 1923
    self.ceo_mustafa.salary_usd = 12_000


