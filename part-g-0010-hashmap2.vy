# pragma version ^0.4.0

struct Employee:
    emp_id: uint8
    salary_usd: uint16

employees: public(HashMap[uint8, Employee])

@external
def set_employee(emp_id: uint8, salary_usd: uint16):

    assert emp_id > 0, "Employee ID must be non-zero"

    self.employees[emp_id] = Employee(emp_id=emp_id, salary_usd=salary_usd)
