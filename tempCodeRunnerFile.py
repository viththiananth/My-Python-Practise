import numpy as np
import tensorflow as tf

z=0
for x in range(1,2016):
    for y in range(1,2016):
        z+=np.log2(1+np.exp((2*np.pi*1j*x*y)/2015))

np.set_printoptions(formatter={'complex_kind':'{:.2f}'.format})
print(z)