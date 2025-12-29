import pandas as pd 

weekly_sales_by_employee = {"aysel": 15_000, "hakan": 22_400, "kağan": 12_700}

ws = pd.Series(weekly_sales_by_employee)

print("aygün" in ws)

print("aysel" in ws)

# False
# True
