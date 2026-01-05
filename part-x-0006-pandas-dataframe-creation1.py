import pandas as pd 
import numpy as np

years = np.array([2010, 2008, 2004, 1001, 2025, 2006])

df = pd.DataFrame(years, columns=["years"])

print(df)

# python main.py

#    years
# 0   2010
# 1   2008
# 2   2004
# 3   1001
# 4   2025
# 5   2006
