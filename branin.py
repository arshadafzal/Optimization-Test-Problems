#  BRANIN-Hoo FUNCTION
#  Author: Arshad Afzal, GIST, South Korea
#  For Questions/ Comments, please email to arshad.afzal@gmail.com

# Applications (1) Test Problems for Optimization Algorithms
#              (2) Generate Labelled Data sets for Regression Analysis

from math import *


def branin(x1, x2):
    f = pow((x2 - 5.1 * (pow(x1, 2)/(4 * pow(pi, 2))) + ((5 / pi) * x1 - 6)), 2) + 10 * (1 - 1 / (8 * pi)) * cos(x1)+10
    return f


print(branin(0.5, 0.5))
