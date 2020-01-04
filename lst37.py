from lst31 import *

import numpy as np
import matplotlib.pyplot as plt

D = dict()

for caseid in log:
    for i in range(0, len(log[caseid])):
        (a, _, t) = log[caseid][i]
        if i > 0:
            (_, _, t0) = log[caseid][i-1]
            d = (t-t0).total_seconds()/(24*3600)
        else:
            d = 0.
        if a not in D:
            D[a] = []
        D[a].append(d)

nrows = 4
ncols = 2

fig, ax = plt.subplots(nrows, ncols)

i = 0
j = 0
for a in sorted(D.keys()):
    print('%s: mean=%.2f std=%.2f days' % (a, np.mean(D[a]), np.std(D[a])))
    ax[i,j].hist(D[a], bins=[0.1*k for k in range(100)])
    ax[i,j].set_title(a)
    ax[i,j].set_xticks(range(10))
    ax[i,j].grid(True)
    if i == nrows-1:
        ax[i,j].set_xlabel('days')
    j += 1
    if j == ncols:
        i += 1
        j = 0

plt.tight_layout()
plt.show()
