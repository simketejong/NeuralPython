import numpy as np

X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
y = np.array([[0,1,1,0]]).T
syn0 = 2*np.random.random((3,5)) - 1
syn1 = 2*np.random.random((5,1)) - 1
print "x" + str(X)
print "y" + str(y)
print "syn0" + str(syn0)
print "syn1" + str(syn1)
#os.system("""bash -c 'read -s -n 1 -p "Press any key to continue..."'""")
#for j in xrange(6000000):
l2_error = 1
teller = 0
while (np.mean(np.abs(l2_error)) > 0.001):
    l1 = 1/(1+np.exp(-(np.dot(X,syn0))))
    l2 = 1/(1+np.exp(-(np.dot(l1,syn1))))
    l2_delta = (y - l2)*(l2*(1-l2))
    l1_delta = l2_delta.dot(syn1.T) * (l1 * (1-l1))
    syn1 += l1.T.dot(l2_delta)
    syn0 += X.T.dot(l1_delta)
    l2_error = y - l2
    print "x" + str(X)
    print "y = " + str(y)
    print "l2 = " + str(l2)
    print "Error:" + str(np.mean(np.abs(l2_error)))
    teller = teller + 1
    print "teller" + str(teller)
#    print "syn0" + str(syn0)
