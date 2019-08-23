# supress FutureWarning from numpy
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
# supress AVX2 CPU warning
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf

x = tf.constant(35, name='x')
y = tf.Variable(x + 5, name='y')

print(y)
print(tf.__version__)