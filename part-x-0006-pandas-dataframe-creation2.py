import pandas as pd 
import numpy as np

years = np.array([2010, 2008, 2004])

yearly_sales = np.array([45_000, 72_000, 54_300])

df = pd.DataFrame({"years": years, "yearly_sales_amounts": yearly_sales})

print(df)

#    years  yearly_sales_amounts
# 0   2010                 45000
# 1   2008                 72000
# 2   2004                 54300
