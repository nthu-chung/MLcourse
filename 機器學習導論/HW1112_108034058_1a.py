#problem1 a
# this code is used to generate a trajectory using monte carlo or probability emthod
# with 2 trajectory storage capacity
# we first generate a random movement and check if the movement is legal by checking
# if it hits the wall or obstacle
# if it pass the test, we execute it by changing state variable

import random

width=10
length=10

def insidewindow(x,y):
    if x<width and x>=0:
        if y<length and y>=0:
            return True
    else:
        return False
def obstacle(x,y):
    if x==0 and y==3: 
        return False # hitting the obstacle 
    elif x==1 and y==3:
        return False
    elif x==2 and y==3:
        return False
    elif x==3 and y==3:
        return False
    elif x==4 and y==3:
        return False
    elif x==7 and y==3:
        return False
    elif x==8 and y==3:
        return False
    elif x==9 and y==3:
        return False
    else:
        return True

prev_trajectory= [0,0,0,0,0,0,0,0,0,0,0, \
                0,0,0,0,0,0,0,0,0,0,0,\
                     0,0,0,0,0,0,0,0,0,0,0,\
                     0,0,0,0,0,0,0,0,0,0,0,\
                     0,0,0,0,0,0,0,0,0,0,0,\
                     0,0,0,0,0,0,0,0,0,0,0,\
                     0,0,0,0,0,0,0,0,0,0,0,\
                     0,0,0,0,0,0,0,0,0,0,0,\
                     0,0,0,0,0,0,0,0,0,0,0,\
                     0,0,0,0,0,0,0,0,0,0,0]

current_trajectory= [0,0,0,0,0,0,0,0,0,0,0, \
                0,0,0,0,0,0,0,0,0,0,0,\
                     0,0,0,0,0,0,0,0,0,0,0,\
                     0,0,0,0,0,0,0,0,0,0,0,\
                     0,0,0,0,0,0,0,0,0,0,0,\
                     0,0,0,0,0,0,0,0,0,0,0,\
                     0,0,0,0,0,0,0,0,0,0,0,\
                     0,0,0,0,0,0,0,0,0,0,0,\
                     0,0,0,0,0,0,0,0,0,0,0,\
                     0,0,0,0,0,0,0,0,0,0,0]

PI= [0.6,0.2,0.2] #probability of moving up, moving right, and moving left

count_move=0  # counting of legal move
count_move_prev=100 # record of best move minimal no of move
for k in range(1000):
    state_x=0
    state_y=0
    count_move=0
    for l in range(100):
            current_trajectory[l]=0 #make all item to zero
    for i in range(100):  # the number 100 need to be fixed maximal number of trials
        p=random.uniform(0,1) #generate another random number
        if p>=0 and p<=PI[0]:
            state_y=state_y+1  # MOVE UP
            if insidewindow(state_x,state_y) and obstacle(state_x,state_y):
                current_trajectory[count_move]= 1
                count_move=count_move+1
            else:
                state_y=state_y-1
               
        elif p>PI[0] and p<=(PI[0]+PI[1]):
            state_x=state_x+1 #move right
            if insidewindow(state_x,state_y)and obstacle(state_x,state_y):
                current_trajectory[count_move]= 2
                count_move=count_move+1
            else:
                state_x=state_x-1
        else:
            state_x=state_x-1 #move left
            if insidewindow(state_x,state_y)and obstacle(state_x,state_y):
                current_trajectory[count_move]= 3
                count_move=count_move+1
            else:
                state_x=state_x+1
        #goal checking 
        if state_x==width-1 and state_y==length-1:
            # unmask the following line to check if goal is reached
            #print('iteration',k, 'move', count_move, 'goal reached')
            break
    if count_move<count_move_prev: #if the current move is better
        count_move_prev=count_move
        for j in range(100):
            prev_trajectory[j]=current_trajectory[j] #store the move history
    if k % 100==0:  #sampling result of improvement when 10000 iteration used change 100 to 1000
        
        print('iter', k, 'result', count_move_prev)
        
for i in range(100):
    if prev_trajectory[i] !=0:
        
        print('index', i, 'movement', prev_trajectory[i])