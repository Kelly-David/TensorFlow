# Simple House Price Predictio using Tensorflow
#
# A very simple model to predict house price based on size. 
# Implemented in TensorFlow
#

import tensorflow as tf 
import numpy as np 
import math 
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Generate houses
num_house = 160
np.random.seed(42)
house_size = np.random.randint(low = 1000, high = 3500, size = num_house )


# Generate prices
np.random.seed(42)
house_price = house_size * 100.0 + np.random.randint(low = 20000, high = 70000, size = num_house )

# Plot the generated house and size
plt.plot(house_size, house_price, 'bx') # bx = blue
plt.xlabel('Price')
plt.ylabel('Size')
plt.show()
