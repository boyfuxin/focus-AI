import numpy as np
from numpy import matrix

def lesson02_01():
    print("Lesson01") 
    world_alcohol=np.genfromtxt("world_alcohol.txt", dtype=str, delimiter=",",skip_header=1)
    print(type(world_alcohol))
    print(world_alcohol)
    print(help(np.genfromtxt))

def lesson02_02():
    vector=np.array([5,10,15,20])
    matrix=np.array([[1,2,3],[4,5,6],[7,8,0]])
    v3=np.array(
        [
            [
                [[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9]],
                [[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9]]
            ],
            [
                [[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9]],
                [[1,2,3],[4,5,6],[7,8,9],[1,2,3],[4,5,6],[7,8,9]]
            ]
        ], dtype=np.float32)
    print(vector.shape)
    print(vector.dtype)
    print(matrix.shape)
    print(matrix.dtype)
    print(v3.shape)
    print(v3.dtype)
    pass
    
if __name__ == '__main__':
    lesson02_01()
    lesson02_02()
