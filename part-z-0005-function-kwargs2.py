def emp_data(**kwargs):

    print(kwargs)


emp_data(name ="ayhan bilir", department = "hr")

emp_data(name ="kağan bilir", department = "hr", married = False)

emp_data(name ="bengü bilir", department = "hr", married = False, salary = 65_000)

# {'name': 'ayhan bilir', 'department': 'hr'}
# {'name': 'kağan bilir', 'department': 'hr', 'married': False}
# {'name': 'bengü bilir', 'department': 'hr', 'married': False, 'salary': 65000}
