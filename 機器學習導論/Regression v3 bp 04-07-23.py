#  network structure
# 2 input unit (a bias plus one input data)
# 2 hidden layer units with sigmodal activaion function
# 1 output layer unit with linear activation function
#
# the desired output is an array r 
# use 2 dimensinal vector

# counting weight coefficients
# 2 v coefficient  coming from 2 hidden unit to output
#  v_1, v_2 
# 4 w coefficeint coming from 2 input unit to 2 hidden units
#  w_z1[m]  w_z2[m]    m running from 0 to 1 
# use sigmodal activation function for hidden unit
# the ouput unit is linear (no sigmodal function is used)

# choose learning rate to be 0.05
# in the end, the neural network fit the function well after 1000 epoch
# here I used 27 sample, so the total number of iteration = 27* number of epoch or 27000
# 
# I have masked v3 or z1 or w_z3
# if you want, you can go to these lines and unmask them
# from these lines, you can even add more neural by adding more varibles



import random
from random import randrange
from math import *

def sigmod(x):
    return 1/(1+exp(-x))
w_z1=[0,0]
w_z2=[0,0]
#w_z3=[0,0]

#initialize weight coefficients
for i in range(2):
    w_z1[i]=random.uniform(-0.1,0.1)
    w_z2[i]=random.uniform(-0.1,0.1)
   # w_z3[i]=random.uniform(-0.1,0.1) 
v_1=random.uniform(-0.1,0.1)
v_2=random.uniform(-0.1,0.1)
#v_3=random.uniform(-0.1,0.1)
v_0=random.uniform(-0.1,0.1) # adding bias term for v
              
eta=0.05 #define learning rate

# repurpose the input vector
# the first element is bias unit
# the second is the input x
# target function f(x)= sin 6x from Alpaydin'book 


# set the rest of element to be zero
x = [ [1,0.0], [1,0.0], [1,0.0], \
      [1,0.0], [1,0.0], [1,0.0], \
      [1,0.0], [1,0.0], [1,0.0],
      [1,0.0], [1,0.0], [1,0.0], \
      [1,0.0], [1,0.0], [1,0.0], \
      [1,0.0], [1,0.0], [1,0.0],
      [1,0.0], [1,0.0], [1,0.0], \
      [1,0.0], [1,0.0], [1,0.0], \
      [1,0.0], [1,0.0], [1,0.0]

      ]

# desired output array
r= [0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0, \
    0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0, \
    0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
    ]

for i in range(27):
    x1= random.uniform(-0.5,0.5)
    x[i][1]=x1
    y=sin(6*x1)+random.gauss(0,0.1)
    r[i]=y
    
for i in range(27000):
    j= randrange(27) #randomly pick sample vector of out of 8  
    desiredoutput=r[j]
    sum_w_z1=0
    sum_w_z2=0
    #sum_w_z3=0
    sum_v=0 
    for k in range(2): 
        sum_w_z1=sum_w_z1+ w_z1[k]*x[j][k]
        sum_w_z2=sum_w_z2+ w_z2[k]*x[j][k]
        #sum_w_z3=sum_w_z3+ w_z3[k]*x[j][k]
    z1_h=sigmod(sum_w_z1)
    z2_h=sigmod(sum_w_z2)
    #z3_h=sigmod(sum_w_z3)
    sum_v=v_1*z1_h+v_2*z2_h+v_0 #keep only two hidden unit
      
    output_y= sum_v  #use linear unit as output

    
#delta rule
    # weight update Ethm Alpaydin' pseudo code
    # update= learning rate*(Desired output - Actualouput)*input
    v_1=v_1-eta*(output_y-desiredoutput)*z1_h  
    v_2=v_2-eta*(output_y-desiredoutput)*z2_h
    #v_3=v_3-eta*(output_y-desiredoutput)*z3_h
    v_0=v_0-eta*(output_y-desiredoutput)*1
    
    for m in range(2):
        # weight update Ethm Alpaydin' pseudo code
        # update= learning rate *v*z(1-z)*(Desired output - Actualouput)*input
    
        w_z1[m]=w_z1[m]-eta*v_1*z1_h*(1-z1_h)*(output_y-desiredoutput)*x[j][m]
        w_z2[m]=w_z2[m]-eta*v_2*z2_h*(1-z2_h)*(output_y-desiredoutput)*x[j][m]
        #w_z3[m]=w_z3[m]-eta*v_3*z3_h*(1-z3_h)*(output_y-desiredoutput)*x[j][m]

for j in range(27):
    desiredoutput = r[j]
    sum_w_z1=0
    sum_w_z2=0
    #sum_w_z3=0
    sum_v=0 
    for k in range(2): 
        sum_w_z1=sum_w_z1+ w_z1[k]*x[j][k]
        sum_w_z2=sum_w_z2+ w_z2[k]*x[j][k]
      #  sum_w_z3=sum_w_z3+ w_z3[k]*x[j][k]
    z1_h=sigmod(sum_w_z1)
    z2_h=sigmod(sum_w_z2)
    #z3_h=sigmod(sum_w_z3)
   
    sum_v=v_1*z1_h+v_2*z2_h+v_0
    output_y= sum_v
    
    print('input x',round(x[j][1],3), 'desiredoutput', round(desiredoutput,3),'actualoutput', round(output_y,3))
# in total, this newtork has 7 coefficient, namely 3 v coefficents and 4 w cofficients 
print('v0', round(v_0,3), 'v1', round(v_1,3), 'v2', round(v_2,3))
print('wz1_0_bias', round(w_z1[0],3), 'wz1_1', round(w_z1[1],3), 'wz2_0_bias', round(w_z2[0],3),'wz2_1', round(w_z2[1],3))

