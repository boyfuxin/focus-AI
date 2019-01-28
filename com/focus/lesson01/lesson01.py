# -*- coding:utf-8 -*-
# /usr/bin/python

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import math

import tensorflow as tf

def tensorflow_tdemo():
    print("HelloWorld")
    
def example01():
    x = [float(i) /100 for i in range(1, 300)]
    y = [math.log(i) for i in x]
    plt.plot(x,y,'r-',linewidth=3)
    a=[x[20], x[175]]
    b=[y[20], y[175]]
    plt.plot(a,b,'g-',linewidth=2)
    
    
    plt.xlabel('X')
    plt.ylabel('ln(x)')
    
    plt.show()
    
def example02():
    print()

if __name__ == '__main__':
    example01()
    
    
    
    
    
