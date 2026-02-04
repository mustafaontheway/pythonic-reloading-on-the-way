def emp_data(full_name: str, department: str, salary: int) -> str:

    return f"Employee full-name: {full_name}, department: {department}, salary: {salary}"


emp_ayhan = emp_data(department="Sales", full_name="Ayhan Bilir", salary=74_000)

print(emp_ayhan) # Employee full-name: Ayhan Bilir, department: Sales, salary: 74000

emp_bengu = emp_data(salary=65_000, department="Marketing", full_name="Bengü Burada")

print(emp_bengu) # Employee full-name: Bengü Burada, department: Marketing, salary: 65000
