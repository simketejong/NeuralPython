import numpy as np
import sys

syn0 = 2*np.random.random((3,5)) - 1
syn1 = 2*np.random.random((5,1)) - 1
np.save('./syn0', syn0)
np.save('./syn1', syn1)
