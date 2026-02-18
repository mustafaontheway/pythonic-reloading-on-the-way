import numpy as np 

sales = np.array([
    [500, 400, 650, 700],
    [480, 620, 490, 500],
    [520, 550, 470, 685],
    [650, 400, 540, 990],
])

premiums1 = np.zeros((4, 4))

for i in range(4):
   for j in range(4):
      if sales[i][j] >= 500:
         premiums1[i][j] += sales[i][j] * 0.08
      
      # else:
      #    premiums[i][j] += 0

print(premiums1)

premiums2 = np.where(sales >= 500, sales * 0.08, 0)

print(premiums1 == premiums2)

# [[40.   0.  52.  56. ]
#  [ 0.  49.6  0.  40. ]
#  [41.6 44.   0.  54.8]
#  [52.   0.  43.2 79.2]]

# python main.py
