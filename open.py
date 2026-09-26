import numpy as np
import sympy as sp
from sympy import *
import main
import matplotlib.pyplot as plt
import pandas as pd

SHEET_ID = '14uUTtGzRia0h_RqW3b_-pteiOTv7BvnSBahgMe5E4kY'
SHEET_NAME = 'Sheet1'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
df = pd.read_csv(url)
b =

x = sp.Symbol('x')
fx = [413.13, 414.41, 405.86, 411.24, 408.79,
399.52,
401.56,
395.42,
399.87,
392.68,
405.05,
404.42]
xvals = [1, 2, 3, 5, 7, 10, 11, 12, 13, 16, 18, 19]
pn = main.cubspln(xvals, fx).tolist()
s1n = pn[2]
fp1 = lambdify(x, s1n)
print(fp1(4))
s2n = pn[3]
fp2 = lambdify(x, s2n)
print(fp2(6))
s3n = pn[4]
fp3 = lambdify(x, s3n)
print(fp3(8))
print(fp3(9))
s4n = pn[8]
fp4 = lambdify(x, s4n)
print(fp4(14))
print(fp4(15))
s5n = pn[9]
fp5 = lambdify(x, s5n)
print(fp5(17))
print(pn[9])
n = len(xvals)
prvals = np.zeros(n)
inter = np.zeros(n)
