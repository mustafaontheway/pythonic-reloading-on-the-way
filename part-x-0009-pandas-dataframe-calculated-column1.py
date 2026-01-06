import pandas as pd 
import numpy as np

years = np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006])

yearly_sales = np.array([45_000, 72_000, 54_300, 52_000, 47_400, 65_000, 60_000])

num_of_emps = np.array([45, 48, 50, 44, 49, 54, 50])

df = pd.DataFrame({"years": years, "yearly_sales_amounts": yearly_sales, "num_of_emps": num_of_emps})

df.index = ["year1", "year2", "year3", "year4", "year5", "year6", "year7"]

df["sales_per_emp"] = df["yearly_sales_amounts"] / df["num_of_emps"]

print(df)

"""
       years  yearly_sales_amounts  num_of_emps  sales_per_emp
year1   2000                 45000           45    1000.000000
year2   2001                 72000           48    1500.000000
year3   2002                 54300           50    1086.000000
year4   2003                 52000           44    1181.818182
year5   2004                 47400           49     967.346939
year6   2005                 65000           54    1203.703704
year7   2006                 60000           50    1200.000000
"""
