from lst32 import *

import pygraphviz as pgv

G = pgv.AGraph(strict=False, directed=True)

G.graph_attr['rankdir'] = 'TB'
G.node_attr['shape'] = 'box'

values = [D[ai][aj].total_seconds() for ai in D for aj in D[ai]]
x_min = min(values)
x_max = max(values)

y_min = 1.0
y_max = 5.0

for ai in D:
    for aj in D[ai]:
        x = D[ai][aj].total_seconds()
        y = y_min + (y_max-y_min) * float(x-x_min) / float(x_max-x_min)
        G.add_edge(ai, aj, label=D[ai][aj], penwidth=y)

G.draw('graph.png', prog='dot')
