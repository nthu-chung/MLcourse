#HW5
#2
import random
import math
import numpy as np


x1_record = []
x2_record = []
error2_record = []
x1 = 0.0
x2 = 0.0
y1 = 0.0
y2 = 0.0
count1_error = 0
count2_error = 0
#decision boundary

for i in range(1000):
  x1 = random.gauss(0,1)  # mean(0,0) sigma=1
  x2 = random.gauss(0,1)

  if (x1 + 1.5)**2 +(x2 + 2)**2 > 2.91**2:
    count1_error += 1
  else: pass
ce1_percent = count1_error/1000*100
print('error rate 1 in ', round(ce1_percent,2),"%")
for experiment in range(10):
  for i in range (1000):
    y1 = 3.0 + random.gauss(0,3)  # mean(3,4) sigma=3
    y2 = 4.0 + random.gauss(0,3)

    if (y1 + 1.5)**2 + (y2 + 2)**2 < 2.91**2:
      count2_error += 1
    else: pass
  ce2_percent = count2_error/1000*100
  error2_record.append(ce2_percent)

mean = np.mean(error2_record)
std = np.std(error2_record)
print('error rate 2')
print('mean = ',round(mean,2),'%','std = ',round(std,2),"%")