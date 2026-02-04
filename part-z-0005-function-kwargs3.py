def emp_data(**kwargs):

    for k, v in kwargs.items():

        print(f"{k}: {v}")


emp_data(name ="ayhan bilir", department = "hr")

print("----------------------------------------")

emp_data(name ="kağan bilir", department = "hr", married = False)

print("----------------------------------------")

emp_data(name ="bengü bilir", department = "hr", married = False, salary = 65_000)

# name: ayhan bilir
# department: hr
# ----------------------------------------
# name: kağan bilir
# department: hr
# married: False
# ----------------------------------------
# name: bengü bilir
# department: hr
# married: False
# salary: 65000
