import pandas as pd
import numpy as np

fake_date = pd.DataFrame(np.random.randint(0, 100, 20).reshape(5, 4), columns=["c1", "c2", "c3", "c4"])

fake_date.index = ["row1", "row2", "row3", "row4", "row5"]

data1 = fake_date.loc["row1": "row3"]

print(data1)

#       c1  c2  c3  c4
# row1  41  34  93  42
# row2  88  64  40  56
# row3  42  54  38  35


# python main.py
