import pandas as pd 
import numpy as np

years = np.array([2000, 2001, 2002, 2003, 2004, 2005, 2006])

yearly_sales = np.array([45_000, 72_000, 54_300, 52_000, 47_400, 65_000, 60_000])

num_of_emps = np.array([45, 48, 50, 44, 49, 54, 50])

df = pd.DataFrame({"years": years, "yearly_sales_amounts": yearly_sales, "num_of_emps": num_of_emps})

df.index = ["year1", "year2", "year3", "year4", "year5", "year6", "year7"]

df.drop("num_of_emps", axis=1, inplace=True) # delete column

print(df)

"""
       years  yearly_sales_amounts
year1   2000                 45000
year2   2001                 72000
year3   2002                 54300
year4   2003                 52000
year5   2004                 47400
year6   2005                 65000
year7   2006                 60000
"""
