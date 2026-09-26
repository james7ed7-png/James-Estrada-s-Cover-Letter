import numpy as np
import sympy as sp
from sympy import *
import main
import matplotlib.pyplot as plt
import pandas as pd
from sympy import Piecewise
from sympy.testing.pytest import ignore_warnings

### create cubic spline polynomial ###
def natural_cubic_spline(datax, datay):
   ### find coefficients ###
   n = len(datax)
   a = datay
   h = np.zeros(n)
   for i in range(n-1):
       h[i] = datax[i+1] - datax[i]
   alpha = np.zeros(n)
   for i in range(1,n-1):
       alpha[i] = (3/h[i])*(a[i+1]-a[i]) - (3/h[i-1])*(a[i]-a[i-1])
   l = np.zeros(n)
   l[0] = 1
   u = np.zeros(n)
   u[0] = 0
   z = np.zeros(n)
   z[0] = 0
   for i in range(1, n-1):
       l[i] = 2*(datax[i+1]-datax[i-1]) - (h[i-1]*u[i-1])
       u[i] = h[i]/l[i]
       z[i] = (alpha[i]-h[i-1]*z[i-1])/l[i]
   l[n-1] = 1
   z[n-1] = 0
   c = np.zeros(n)
   c[n-1] = 0
   b = np.zeros(n)
   d = np.zeros(n)
   for j in reversed(range(n-1)):
       c[j] = z[j] - u[j]*c[j+1]
       b[j] = (a[j+1]-a[j])/h[j] - h[j]*(c[j+1]+2*c[j])/3
       d[j] = (c[j+1]-c[j])/(3*h[j])
   Q = np.zeros((n,n))
   Q[0] = a
   Q[1] = b
   Q[2] = c
   Q[3] = d
   ### create polynomials ###
   x = sp.Symbol('x')
   Sfunc = sp.MutableDenseNDimArray.zeros(n-1, 1)
   S = 0
   for k in range(n-1):
       for j in range(4):
           p = (x - datax[k])**j
           S += p * round(Q[j][k], 5)
       Sfunc[k] = simplify(S)
       S = 0
   return Sfunc


### find derivative and derivative values of cubic spline polynomial ###
def getderivative(func):
    x = sp.Symbol('x')
    n = len(func)
    fpvals = np.zeros(n)
    for i in range(n-1):
        dy = diff(func[i], x)
        fp = lambdify(x, dy)
        fpvals[i-1] = round(float(fp(i + .5)), 2)
    return fpvals


### find second derivative and second derivative values of cubic spline polynomial ###
def getsndderivative(funcp):
    x = sp.Symbol('x')
    n = len(funcp)
    fpvals = np.zeros(n)
    for i in range(n-1):
        dy = diff(funcp[i], x, 2)
        fp = lambdify(x, dy)
        fpvals[i] = round(float(fp(i + .5)), 2)
    return fpvals


### sum derivative values (positive and negative) and occurances ###
def derivativesums(vals):
    n = len(vals)
    sums = np.zeros((2, 2))
    for i in range(n):
        if vals[i] > 0:
            sums[0][0] += vals[i]
            sums[0][1] += 1
        elif vals[i] < 0:
            sums[1][0] += vals[i]
            sums[1][1] += 1
    return sums


def derivativeavg(vals):
    avg = np.zeros(2)
    avg[0] = vals[0][0]/vals[0][1]
    avg[1] = vals[1][0]/vals[1][1]
    return avg


def findbounds(points, values):
    n = len(values)
    bound = [values[0], values[0]]
    for i in range(n):
        if bound[0] > values[i]:
            bound[0] = values[i]
        elif bound[1] < values[i]:
            bound[1] = values[i]
    return bound

def ones(fpvals, fp2vals):
    n = len(fpvals)
    ones = np.zeros(n)
    for i in range(n):
        if fpvals[i] > 0 and fp2vals[i] > 0:
            ones[i] = 1
        if fpvals[i] < 0 and fp2vals[i] < 0:
            ones[i] = -1
    return ones
