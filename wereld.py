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


ForwardArray = np.array([1,1,1])
a = np.random.randint(10, size = 100)
print "world = " + str(a)
teller = 0
while (teller < 99):
    if a[teller] == 0:
        ForwardArray[0] = 0
    else:
        ForwardArray[0] = 1

    if teller == 98:
        ForwardArray[2] = 0

    teller = teller + 1
    if a[teller] == 0:
        ForwardArray[1] = 0
    else:
        ForwardArray[1] = 1

    ForwardArray[2] = 1

#print "ForwardArray" + str(ForwardArray)
#print "return" + str(forward(ForwardArray))

    if forward(ForwardArray) > 0:
        teller = teller + 1
    else:
        if a[teller] == 0:
            ForwardArray[2] = 0
        else:
            teller = teller -1
            a[teller] = a[teller] - 1
    print "input" + str(ForwardArray)
    print "output" + str(forward(ForwardArray))
    print "teller" + str(teller)
    if ForwardArray[2] == 0:
        print "world = " + str(a)
        sys.exit()
