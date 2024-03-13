#HW5
#1
import random
import math
import numpy as np
import matplotlib.pyplot as plt

w1_set = 1.2
w0_set = 0
outcome = 0
w1 = 0.01
w0 = 0.01
eta = 0.01
x_record = []
r_record = []
sum_EN = []

def Y(x):
  if x < 1:
    return 0 
  if x>=1 and x<3:
    return 0.5 * (x - 1)
  if x >= 3:
    return 1

def sigmod(x,w1,w0):
  return 1/(1 + math.exp(-w1*x-w0))

for iteration in range(30):
  x = random.uniform(-4,4)
  zeta = random.uniform(0,1)
  y = Y(x)
  if zeta <= y:
    outcome = 1
    x_record.append(float(x))
    r_record.append(int(outcome))
    print("iteratoin", iteration, 'x', round(x,2),' ',outcome)

  else:
    outcome = 0
    x_record.append(float(x))
    r_record.append(int(outcome))
    print("iteratoin", iteration, 'x', round(x,2),' ',outcome)
plt.plot(x_record)
plt.show()

epoch = 100
sum1 = 0.0
sum2 = 0.0

sum_en = 0.0
print('sum1',sum1,'sum2',sum2)

for iteration2 in range(epoch):
  sum1 = 0.0
  sum2 = 0.0
  sum_en = 0.0
  for i in range(30):
    y = sigmod(x_record[i],w1,w0)
    sum1 = sum1 + (r_record[i] - y) * x_record[i]
    sum2 = sum2 + (r_record[i] - y)
    #compute cross entropy

    sum_en = sum_en - (r_record[i] * math.log(y) + (1 - r_record[i]) * math.log(1 - y))
    
  w1=w1+eta*sum1
  w0=w0+eta*sum2
  if iteration2 % 10 == 0:
    sum_EN.append(float(sum_en))
    print('iteration', iteration2, 'error', sum_en)
plt.plot(sum_EN)
plt.show()
print('final result',"w1:",w1,' ',"w0:",w0)

