import pandas as pd
import numpy as np

fake_date = pd.DataFrame(np.random.randint(0, 100, 20).reshape(5, 4), columns=["c1", "c2", "c3", "c4"])

fake_date.index = ["row1", "row2", "row3", "row4", "row5"]

print(fake_date)

cond_data1 = fake_date[(fake_date.c1 == 50) | (fake_date.c2 != 10)] # :) pitfall

print(cond_data1) 
