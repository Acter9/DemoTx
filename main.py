# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import numpy as np

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def ar():
    new_ar = np.array([1,3,4,6,8])
    print(new_ar)
    ar2 = np.array([1,'23', 124, False])
    print(ar2)
    print(ar2[[0,0,0]])
    print(ar2[[True, False, True, True]])

    ar3 = []
    for i in range(9): ar3.append(f'{i}'.format(i))
    ar4 = np.array(ar3).reshape(3,3)
    print(ar4)
    print(ar4[0])

    a = np.array([[[1,2], [3,4]],[[5,6],[7,8]],[[9,10],[11,12]]])
    print(a.shape)
    print(a.ndim)
    print(a.size)
if __name__ == '__main__':
    # print_hi('PyCharm')
    ar()



