import numpy as np
import sympy as sp
from sympy import *
import main

x = sp.Symbol('x')
fx = [np.exp(0), np.exp(1), np.exp(2), np.exp(3)]
xvals = [0, 1, 2, 3]
pn = main.cubspln(xvals, fx).tolist()
s1n = pn[2]
fp1 = lambdify(x, s1n)
print(pn)