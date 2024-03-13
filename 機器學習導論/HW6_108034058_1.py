#HW5
#1
import math
import random
import numpy
from math import *

eta = 0.1
w_x = random.uniform(-0.1,0.1)
theta = random.uniform(-0.1,0.1)

HIGH = 0.9
LOW = 0.1

def logistic(w_x, theta, x):
  return 1/(1 + exp(-w_x*x -theta))





#Design NOT gate
for i in range (1000):
#setup
  x0 = random.gauss(0, 0.1)
  output_cal = logistic(w_x, theta, x0)
#delta rule
  w_x = w_x - eta*(output_cal - HIGH)*x0
  theta = theta - eta*(output_cal - HIGH)*1
#setup
  x1 = random.gauss(1, 0.1)
  output_cal = logistic(w_x, theta, x1)
#delta rule
  w_x = w_x - eta*(output_cal - LOW)*x1

  theta = theta - eta*(output_cal - LOW)*1

#sampling the error every 100 sample
  if i % 100 == 0:
    error = 0 #error cal
    x_test = 0
    error = error + (logistic(w_x, theta, x_test) - LOW)**2

    x_test = 1
    error = error + (logistic(w_x, theta, x_test) - HIGH)**2
   
    print("iteration", i , "error", error)
print('wx', w_x, 'theta', theta)
x_test = 0.1
test_output = logistic(w_x, theta, x_test)
print('x', x_test, 'output y', test_output)
x_test = 0.9
test_output = logistic(w_x, theta, x_test)
print('x', x_test, 'output y', test_output)