# -*- coding: utf-8 -*-
"""mlhw1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12ZRFfkd9Nr43Ni4KrYZlnZlgiTMrpj3p
"""

#HW1
#1
import random
import math
import numpy as np
import pandas as pd

numNeedles=1000000
piGuess=0.0

def throwNeedles(numNeedles):
    inCircle = 0
    for Needles in range(1, numNeedles + 1) :
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if y - x*x <= 0:
          inCircle+=1
    return inCircle/numNeedles
piGuess = throwNeedles(numNeedles)
print('y=x^2 area = ', piGuess)

#2
import random
import math
import numpy as np
import pandas as pd

numNeedles=1000000
piGuess=0.0

def throwNeedles(numNeedles):
    inCircle = 0
    for Needles in range(1, numNeedles + 1) :
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        z = random.uniform(0, 1)
        if x*x + y*y + z*z < 1:
          inCircle+=1
    return inCircle/numNeedles
piGuess = throwNeedles(numNeedles)
print('1/8 ball\'s volumn = ', piGuess)

#3
import random
import pandas as pd
sd = 0.1
w2 = 2.0
w1 = 0.5
w0 = 0.3
num_sample = 30

df = pd.DataFrame(columns=['x', 'r'])
for i in range(0, num_sample):
  x = random.uniform(0, 1)
  r = w2*x*x + w1*x + w0 +random.gauss(0, sd)
  df = df.append({"x":round(x,3), "r":round(r,3)},ignore_index=True)
  print("x",round(x,3), "r",round(r,3))
df
df.to_csv('/content/drive/MyDrive/HW1_3.csv', index=False)

output.to_csv('/content/drive/MyDrive/Report_of_0005.HK.csv')