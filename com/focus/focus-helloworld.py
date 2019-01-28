import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
import numpy as np
import sympy as sp

def tensorflow_demo():
    a = 2
    b = 3
    c = a + b
    print("a+b=", c)
    
#     图结构
    
    a_t = tf.constant(1)
    b_t = tf.constant(2)
    c_t = a_t + b_t
    print("", c_t, "\n   type=", type(c_t))

#     sess = tf.Session()
#     c_t_value=sess.run(c_t)
#     print("c_t_value=", c_t_value)
    
    with tf.device("/gpu:0"):

        with tf.Session() as sess:
            c_t_value = sess.run(c_t)
            print("c_t_value=", c_t_value)

    
def numpy_demo01():#矩阵特征值 特征向量
    X = [[-1, 1, 0],
         [-4, 3, 0],
         [1, 0, 2]]

    x=np.matrix(X)
    print(np.linalg.eig(x))
    pass

        
if __name__ == '__main__':

    tensorflow_demo()
    numpy_demo01()
    
