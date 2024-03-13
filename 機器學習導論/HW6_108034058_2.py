#HW5
#2
import math
import random
import numpy
from math import *

eta = 0.1
w_x = random.uniform(-0.1,0.1)
w_y = random.uniform(-0.1,0.1)
theta = random.uniform(-0.1,0.1)

HIGH = 0.9
LOW = 0.1

def logistic(w_x, w_y, theta, x, y):
  return 1/(1 + exp(-w_x*x - w_y*y -theta))





#Design AND gate
for i in range (1000):
#setup
  x00 = random.gauss(0, 0.1)
  y00 = random.gauss(0, 0.1)
  output_cal = logistic(w_x, w_y, theta, x00, y00)
#delta rule
  w_x = w_x - eta*(output_cal - LOW)*x00
  w_y = w_y - eta*(output_cal - LOW)*y00
  theta = theta - eta*(output_cal - LOW)*1
#setup
  x10 = random.gauss(1, 0.1)
  y10 = random.gauss(0, 0.1)
  output_cal = logistic(w_x, w_y, theta, x10, y10)
#delta rule
  w_x = w_x - eta*(output_cal - LOW)*x10
  w_y = w_y - eta*(output_cal - LOW)*y10
  theta = theta - eta*(output_cal - LOW)*1
#setup
  x01 = random.gauss(0, 0.1)
  y01 = random.gauss(1, 0.1)
  output_cal = logistic(w_x, w_y, theta, x01, y01)
#delta rule
  w_x = w_x - eta*(output_cal - LOW)*x01
  w_y = w_y - eta*(output_cal - LOW)*y01
  theta = theta - eta*(output_cal - LOW)*1
#setup
  x11 = random.gauss(1, 0.1)
  y11 = random.gauss(1, 0.1)
  output_cal = logistic(w_x, w_y, theta, x11, y11)
#delta rule
  w_x = w_x - eta*(output_cal - HIGH)*x11
  w_y = w_y - eta*(output_cal - HIGH)*y11
  theta = theta - eta*(output_cal - HIGH)*1
#sampling the error every 100 sample
  if i % 100 == 0:
    error = 0 #error cal
    x_test = 0
    y_test = 0
    error = error + (logistic(w_x, w_y, theta, x_test, y_test) - LOW)**2

    x_test = 1
    y_test = 0
    error = error + (logistic(w_x, w_y, theta, x_test, y_test) - LOW)**2
    
    x_test = 0
    y_test = 1
    error = error + (logistic(w_x, w_y, theta, x_test, y_test) - LOW)**2
    
    x_test = 1
    y_test = 1
    error = error + (logistic(w_x, w_y, theta, x_test, y_test) - HIGH)**2
    print("iteration", i , "error", error)
print('wx', w_x, 'wy', w_y, 'theta', theta)
x_test = 0.1
y_test = 0.1
test_output = logistic(w_x, w_y, theta, x_test, y_test)
print('x', x_test,'y', y_test, 'output', test_output)
x_test = 0.9
y_test = 0.1
test_output = logistic(w_x, w_y, theta, x_test, y_test)
print('x', x_test,'y', y_test, 'output', test_output)
x_test = 0.1
y_test = 0.9
test_output = logistic(w_x, w_y, theta, x_test, y_test)
print('x', x_test,'y', y_test, 'output', test_output)
x_test = 0.9
y_test = 0.9
test_output = logistic(w_x, w_y, theta, x_test, y_test)
print('x', x_test,'y', y_test, 'output', test_output)