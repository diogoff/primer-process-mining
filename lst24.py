from lst22 import *

import pygraphviz as pgv

G = pgv.AGraph(strict=False, directed=False)

G.graph_attr['rankdir'] = 'LR'
G.node_attr['shape'] = 'circle'

for ui in W:
    for uj in W[ui]:
        G.add_edge(ui, uj, label=W[ui][uj])

G.draw('graph.png', prog='dot')
