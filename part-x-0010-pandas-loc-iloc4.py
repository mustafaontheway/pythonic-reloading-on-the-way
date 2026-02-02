import pandas as pd
import numpy as np

fake_date = pd.DataFrame(np.random.randint(0, 100, 20).reshape(5, 4), columns=["c1", "c2", "c3", "c4"])

fake_date.index = ["row1", "row2", "row3", "row4", "row5"]

data1 = fake_date.iloc[:2, :3]

print(data1)

#       c1  c2  c3
# row1  29  61  91
# row2  99   1   2
