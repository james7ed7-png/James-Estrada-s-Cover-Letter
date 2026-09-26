import numpy as np
import sympy as sp
from sympy import *
import main
import matplotlib.pyplot as plt
import pandas as pd


# import stock market data and define variables
SHEET_ID = '1kTy1Vb76VPPWFaXgapaCtRvHezLtysXmEgfKkbz8_gk'
SHEET_NAME = 'Sheet1'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
df = pd.read_csv(url)
b = df['Close']
n = len(b)
fxvals = np.zeros(n)
xvals = np.zeros(n)
xax = np.zeros(n-1)
xvalsprime = np.zeros(n - 1)

for i in range(n):
    t = i
    xvals[i] = t
    fxvals[i] = b[i]
    if i != 0:
        xvalsprime[i-1] = t - .5

x = sp.Symbol('x')
sfunc = main.natural_cubic_spline(xvals, fxvals)
fpvals = main.getderivative(sfunc)
sums = main.derivativesums(fpvals)
fp2vals = main.getsndderivative(sfunc)
avg = main.derivativeavg(sums)
print(avg)
bound1 = main.findbounds(xvals, fp2vals)
bound2 = main.findbounds(xvals, fxvals)
derdata = main.ones(fpvals, fp2vals)
fig, axs = plt.subplots(2, sharex=True)
plt.xlabel('Days')
plt.ylabel('Values')

for i in range(n-1):
    axs[1].text(xvalsprime[i], xax[i] + bound1[1]*1.1, fpvals[i], horizontalalignment='center',
                verticalalignment='center', weight='bold', color="navy", size=6)
    axs[1].text(xvalsprime[i], xax[i] + bound1[0]*1.1, fp2vals[i], horizontalalignment='center',
                verticalalignment='center', weight='bold', color="darkgreen", size=6)
    if derdata[i] == 1:
        axs[1].text(xvalsprime[i], fp2vals[i], '1', horizontalalignment='center',
                    verticalalignment='center', weight='bold', color="g", size=6)
    if derdata[i] == -1:
        axs[1].text(xvalsprime[i], fp2vals[i], '-1', horizontalalignment='center',
                    verticalalignment='center', weight='bold', color="r", size=6)
    if derdata[i] == -2:
        axs[1].text(xvalsprime[i], fp2vals[i], '-1', horizontalalignment='center',
                    verticalalignment='center', weight='bold', color="r", size=6)
    if derdata[i] == 2:
        axs[1].text(xvalsprime[i], fp2vals[i], '2', horizontalalignment='center',
                    verticalalignment='center', weight='bold', color="g", size=6)
    axs[0].text(xvals[i], fxvals[i], fxvals[i], size=8)
plt.ylim(bound2[0] - 10, bound2[1] + 10)
axs[0].plot(xvals, fxvals, marker='o', linewidth=2.0, label="f(x)")
plt.ylim(bound1[0] * 1.3, bound1[1] * 1.3)
axs[1].plot(xvalsprime, fpvals, marker='o', linewidth=2.0, color="cornflowerblue", label="f\'(x)")
axs[1].plot(xvalsprime, fp2vals, marker='o', linewidth=2.0, color="limegreen", label="f\'\'(x)")
plt.xticks(np.arange(0, 1, n))
plt.xticks(np.arange(n))
plt.legend()
plt.grid()
plt.show()