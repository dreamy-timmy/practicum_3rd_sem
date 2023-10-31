# 2
import scipy
import sympy
from sympy import *
import math
import numpy as np

print("--------------------------------------------------------------------------------------------------------")
print()

def f(x):
    return 2/(math.sin(x)+4)

def first():
    return (scipy.misc.derivative(f, 1),scipy.misc.derivative(f, 2))
# print(first())

def second():
    x = sympy.Symbol('x')
    expr = sympy.diff(2/(sympy.sin(x) + 4), x)
    print(expr)
# second()

def third():
    result = scipy.integrate.quad(f, 3, 6)
    print(result)
# third()

def fourth():
    x = sympy.Symbol('x')
    expr = sympy.integrate(2/(sympy.sin(x) + 4), x)
    print(expr)
# fourth()



def fifth():
    def f(x):
        x_1 = x[0]
        x_2 = x[1]
        return (x_1 - 4) ** 2 + (x_2 - 2) ** 2

    def constraint_1(x):
        x_1 = x[0]
        x_2 = x[1]
        return 4*x_1 + 2*x_2 - 11

    def constraint_2(x):
        x_1 = x[0]
        x_2 = x[1]
        return - 2 * x_1 - 7

    b = (0, np.inf)
    bnds = (b, b) # почему?
    con1 = {'type': 'ineq', 'fun': constraint_1}
    con2 = {'type': 'ineq', 'fun': constraint_2}
    cons = [con1, con2]

    x0 = (1, 2)
    
    sol = scipy.optimize.minimize(f, x0, method='SLSQP',
                               bounds=bnds, constraints=cons)

    print(sol)
    
# fifth()
