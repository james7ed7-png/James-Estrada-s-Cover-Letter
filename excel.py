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
b = df['Open']
print(b[1])

