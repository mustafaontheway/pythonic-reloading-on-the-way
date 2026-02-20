# pragma version ^0.4.0

struct Employee:

    full_name: String[75]
    department: String[50]
    salary_ethereum: uint8

emp_ayhan: public(Employee)

@deploy
def __init__():

    self.emp_ayhan.full_name = "Ayhan Bilir"

    self.emp_ayhan.department = "Marketing"

    self.emp_ayhan.salary_ethereum = 2
