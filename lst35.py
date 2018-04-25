from lst31 import *

import matplotlib.pyplot as plt

X = dict()
Y = dict()

caseids = sorted(log.keys(),
                       key=lambda caseid: log[caseid][0][-1])

for (y, caseid) in enumerate(caseids):
    for i in range(0, len(log[caseid])):
        (a, _, x) = log[caseid][i]
        if a not in X:
            X[a] = []
            Y[a] = []
        X[a].append(x)
        Y[a].append(y)

for a in sorted(X.keys()):
    plt.plot(X[a], Y[a], 'o', label=a,
                markersize=20, markeredgewidth=0., alpha=0.5)

axes = plt.gca()

axes.set_yticks(range(len(caseids)))
axes.set_ylim(-1, len(caseids))
axes.set_yticklabels(caseids)
axes.set_ylabel('case id')
axes.invert_yaxis()

axes.set_xlabel('timestamp')
axes.xaxis.tick_top()
axes.xaxis.set_label_position('top')

plt.grid(True)
plt.legend(numpoints=1)
plt.tight_layout()
plt.show()
