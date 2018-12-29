from quil2qasm import *
from ibmqx_ising_qubo_qaoa import *
from rigetti_ising_qubo_qaoa import *
from qubo_ising_generators import *
from pyquil.api import get_qc
import networkx as nx
import numpy as np
from dwave_qbsolv import QBSolv
import dimod
from graphs import *
#from dwave.system.samplers import DWaveSampler
from qiskit import *
from qiskit_aqua.components.optimizers import *
from qiskit_aqua import QuantumInstance
from classical_solvers import *

def combined_test2():
#        G = nx.algorithms.operators.unary.complement(melbourne())
        G = nx.gnp_random_graph(10, 0.5, 101)
        top = '10q-noisy-qvm'
        opt = 'POWELL'
        x = []
        ising = []
        qubo = []
        print('Powell, gnp topology, maximum clique, 10q rigetti qvm noise')
        print(maximum_clique(G))
        for a in range(1, 50):
                x.append(a)
                result_out = rigetti_ising_qubo(G, maximum_clique_qubo_rigetti, opt, top, a)
                ref = subg_is_clique(result_out, G)
                if ref == True:
                         qubo.append(result_out.count(1))
                else:
                         qubo.append(0)
                print(x, qubo)
print(combined_test2())


