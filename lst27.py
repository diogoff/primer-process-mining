from lst26 import *

import pygraphviz as pgv

G = pgv.AGraph(strict=False, directed=False)

G.graph_attr['rankdir'] = 'LR'
G.node_attr['shape'] = 'circle'

U = sorted(UA.keys())
for i in range(0, len(U)-1):
    for j in range(i+1, len(U)):
        ui = U[i]
        uj = U[j]
        x = len(UA[ui] & UA[uj])
        if x > 0:
            G.add_edge(ui, uj, label=x)

G.draw('graph.png', prog='dot')
