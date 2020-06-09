#  HARTMANN 6-DIMENSIONAL FUNCTION
#  Author: Arshad Afzal, IIT Kanpur, India
#  For Questions/ Comments, please email to arshad.afzal@gmail.com

# Applications (1) Test Problems for Optimization Algorithms
#              (2) Generate Labelled Data sets for Regression Analysis

import numpy as np
from math import *


def hartmann6(x1, x2, x3, x4, x5, x6):
    x = [x1, x2, x3, x4, x5, x6]
    alpha = [1, 1.2, 3.0, 3.2]
    a = [[10.0, 3.0, 17.0, 3.5, 1.7, 8.0], [0.05, 10.0, 17.0, 0.1, 8.0, 14.0],
         [3.0, 3.5, 1.7, 10.0, 17.0, 8.0], [17.0, 8.0, 0.05, 10.0, 0.1, 14.0]]
    p = np.dot(pow(10, -4), [[1312, 1696, 5569, 124, 8283, 5886], [2329, 4135, 8307, 3736, 1004, 9991],
                             [2348, 1451, 3522, 2883, 3047, 6650], [4047, 8828, 8732, 5743, 1091, 381]])
    outer_sum = 0
    for i in range(4):
        inner_sum = 0
        for j in range(6):
            inner_sum = inner_sum + a[i][j] * pow((x[j] - p[i][j]), 2)
            if j == 5:
                break
        new = alpha[i] * np.exp(-inner_sum)
        outer_sum = outer_sum + new
        if i == 3:
            break
    f = -outer_sum
    return f


print(hartmann6(0.5, 0.5, 0.5, 0.5, 0.5, 0.2))
