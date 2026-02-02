import pandas as pd
import numpy as np

fake_date = pd.DataFrame(np.random.randint(0, 100, 20).reshape(5, 4), columns=["c1", "c2", "c3", "c4"])

fake_date.index = ["row1", "row2", "row3", "row4", "row5"]

#data1 = fake_date.iloc["row1": "row3"] # TypeError: cannot do positional indexing on Index with these indexers [row1] of type str

data1 = fake_date.iloc[0:2]

print(data1)

#       c1  c2  c3  c4
# row1  57  81  53  21
# row2  26  10  50  33

data2 = fake_date.iloc[0:3]

print(data2)

#       c1  c2  c3  c4
# row1  62  78   9  78
# row2  32  55  37  85
# row3  39   6  17  66

# python main.py
