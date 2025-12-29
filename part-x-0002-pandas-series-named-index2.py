import pandas as pd 

ages = pd.Series([17, 99, 85, 62, 64, 44], index=["age1", "age2", "age3", "age4", "age5", "age6"])

print(ages["age3"])

print(ages["age2": "age4"])

"""
85

age2    99  
age3    85  
age4    62  
dtype: int64

"""
