import os
import sys
d = os.path.dirname(os.getcwd())+'/utils'
sys.path.append(d)
from graphs import *
from ibmqx_ising_qubo_qaoa import *
from qubo_ising_generators import *
from classical_solvers import *
import networkx as nx
import numpy as np
import time
import warnings
warnings.filterwarnings("ignore")


def ibqmx_qaoa(G, optimizer, func, r):
        app_ratio = 0
        qubo_main = []
        counter = 0
        for avg in range(0, 100):
            counter += 1
            result_out = solve_ibmqx_ising_qubo(G, func, optimizer, r)
            result2 = []
            for i in result_out:
                  if i == 0:
                        result2.append(1)
                  if i == 1:
                        result2.append(0)
            H = G.subgraph(result2)
            if is_vertex_cover(H) == True:
              qubo_main.append(len(H))
              app_ratio += len(H)
            else:
              qubo_main.append(len(G))
              app_ratio += len(G)
            print(float(app_ratio)/float(counter))
print('min vc')
out = []
for r in range(1, 20):
    G = nx.gnp_random_graph(7, 0.5, 101)
    res = ibqmx_qaoa(G, SLSQP(), minimum_vertex_cover_qubo_matrix_ibmqx, r)
    out.append(res)
    print(out)
        
