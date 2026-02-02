import pandas as pd
import numpy as np

fake_date = pd.DataFrame(np.random.randint(0, 100, 20).reshape(5, 4), columns=["c1", "c2", "c3", "c4"])

fake_date.index = ["row1", "row2", "row3", "row4", "row5"]

print(fake_date)

"""
      c1  c2  c3  c4
row1  45  58  97  53
row2  79  37  62  89
row3  24  45  88  21
row4  72  20  50  45
row5  17  39  42  37
"""

cond_data1 = fake_date[(fake_date.c1 < 50) & (fake_date.c2 > 10)]

print(cond_data1)

"""
      c1  c2  c3  c4
row1  45  58  97  53
row3  24  45  88  21
row5  17  39  42  37

"""
