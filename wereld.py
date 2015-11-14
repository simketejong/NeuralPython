import numpy as np
import array
import sys

def forward( X ):
    syn0 = np.load('syn0.npy')
    syn1 = np.load('syn1.npy')
    l1 = 1/(1+np.exp(-(np.dot(X,syn0))))
    l2 = 1/(1+np.exp(-(np.dot(l1,syn1))))
    end = round(l2)
    return(end)


ForwardArray = np.array([1,1,1]) # init
a = np.random.randint(10, size = 100) # Garden size with food
print "Voor = " + str(a)

teller = 0
Lifespan=0
Food = 0
while (teller < 99):
    Lifespan = Lifespan + 1

    if a[teller] == 0:
        ForwardArray[0] = 0
    else:
        ForwardArray[0] = 1

    teller2 = teller + 1
    if a[teller2] == 0:
        ForwardArray[1] = 0
    else:
        ForwardArray[1] = 1

    if teller == 98:
        ForwardArray[2] = 0 #die
    else:
        ForwardArray[2] = 1


    if forward(ForwardArray) > 0: 
        teller = teller + 1 # Neural network wants to go forward 
    else:
        if a[teller] == 0: # Stay put
            ForwardArray[2] = 0 #die
        else:
            Food = Food + a[teller]
            a[teller] = a[teller] - 1 # eat

    if ForwardArray[2] == 0:
        print "Na   = " + str(a)
        print "How Far " + str(teller)
        print "Lifespan " + str(Lifespan)
        print "Food " + str(Food)        
        sys.exit()
