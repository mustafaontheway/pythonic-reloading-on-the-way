import pandas as pd
import numpy as np

fake_date = pd.DataFrame(np.random.randint(0, 100, 20).reshape(5, 4), columns=["c1", "c2", "c3", "c4"])

print(fake_date)

"""
   c1  c2  c3  c4
0  41  44  17  18
1  36  25  27  28
2  80  31  66  98
3  25  50  16  21
4  13  38  24  57

"""

fake_date.index = ["row1", "row2", "row3", "row4", "row5"]

print(fake_date)


#       c1  c2  c3  c4
# row1  81   4  80  41
# row2  71   0  63  44
# row3  75  77  87   8
# row4  49  51  42   7
# row5  86  44  21  74


# python main.py
