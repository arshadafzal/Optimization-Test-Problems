#  HARTMANN 3-DIMENSIONAL FUNCTION
#  Author: Arshad Afzal, IIT Kanpur, India
#  For Questions/ Comments, please email to arshad.afzal@gmail.com

# Applications (1) Test Problems for Optimization Algorithms
#              (2) Generate Labelled Data sets for Regression Analysis

import numpy as np
from math import *


def hartmann3(x1, x2, x3):
    x = [x1, x2, x3]
    alpha = [1, 1.2, 3.0, 3.2]
    a = [[3.0, 10, 30], [0.1, 10, 35], [3.0, 10, 30], [0.1, 10, 35]]
    p = np.dot(pow(10, -4), [[3689, 1170, 2673], [4699, 4387, 7470], [1091, 8732, 5547], [381, 5743, 8828]])
    outer_sum = 0
    for i in range(4):
        inner_sum = 0
        for j in range(3):
            inner_sum = inner_sum + a[i][j] * pow((x[j] - p[i][j]), 2)
            if j == 2:
                break
        new = alpha[i] * np.exp(-inner_sum)
        outer_sum = outer_sum + new
        if i == 3:
            break
    f = -outer_sum
    return f


print(hartmann3(0.5, 0.5, 0.5))



