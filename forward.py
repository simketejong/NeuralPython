import numpy as np
import sys

X = map(int, sys.argv[1:])

syn0 = np.load('syn0.npy')
syn1 = np.load('syn1.npy')

l1 = 1/(1+np.exp(-(np.dot(X,syn0))))
l2 = 1/(1+np.exp(-(np.dot(l1,syn1))))
end = round(l2)
print "end" + str(end)