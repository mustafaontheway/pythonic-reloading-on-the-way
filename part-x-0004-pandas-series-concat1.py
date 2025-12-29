import pandas as pd 

weekly_sales_by_employee1 = {"aysel": 15_000, "hakan": 22_400, "kağan": 12_700}

weekly_sales_by_employee2 = {"aygül": 14_200.25, "hakan": 32_400.40, "kağan": 15_700.87}

ws1 = pd.Series(weekly_sales_by_employee1)

ws2 = pd.Series(weekly_sales_by_employee2)

ws = pd.concat([ws1, ws2])

print(ws)

"""
aysel    15000.00
hakan    22400.00
kağan    12700.00
aygül    14200.25
hakan    32400.40
kağan    15700.87
dtype: float64   

"""
