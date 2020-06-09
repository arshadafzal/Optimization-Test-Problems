#  BOOTH FUNCTION
#  Author: Arshad Afzal, IIT Kanpur, India
#  For Questions/ Comments, please email to arshad.afzal@gmail.com

# Applications (1) Test Problems for Optimization Algorithms
#              (2) Generate Labelled Data sets for Regression Analysis

from math import *


def booth(x1, x2):
    f = pow((x1+2*x2-7), 2)+pow((2*x1+x2-5), 2)
    return f


print(booth(0.5, 0.5))
