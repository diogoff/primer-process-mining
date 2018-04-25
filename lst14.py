from lst11 import *

import pygraphviz as pgv

G = pgv.AGraph(strict=False, directed=True)

G.graph_attr['rankdir'] = 'LR'
G.node_attr['shape'] = 'box'

for ai in F:
    for aj in F[ai]:
        G.add_edge(ai, aj, label=F[ai][aj])

G.draw('graph.png', prog='dot')
