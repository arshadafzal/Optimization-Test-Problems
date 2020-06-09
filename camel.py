#  SIX HUMP CAMEL FUNCTION
#  Author: Arshad Afzal, IIT Kanpur, India
#  For Questions/ Comments, please email to arshad.afzal@gmail.com

# Applications (1) Test Problems for Optimization Algorithms
#              (2) Generate Labelled Data sets for Regression Analysis

from math import *


def camel(x1, x2):
    f = 4*pow(x1, 2) - 2.1*pow(x1, 4)+(1/3)*pow(x1, 6)+x1 * x2 - 4 * pow(x2, 2) + 4 * pow(x2, 4)
    return f


print(camel(1, 2))