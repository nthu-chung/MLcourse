#HW7_2
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import cos

# Generate 5 data sets, each with 20 data points

df = pd.DataFrame(columns=['set', 'x', 'y'])
for i in range(5):
  for j in range(20):
    x = random.uniform(-2, 2)
    y = cos(1.5*x) + random.gauss(0, 1)
    df = df.append({"set": i+1 , "x":round(x, 4), "y":round(y, 4)},ignore_index=True)

df.to_csv('/content/drive/MyDrive/HW7_2.csv', index=False)