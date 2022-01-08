from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit import IBMQ
from qiskit.compiler import transpile

from time import perf_counter
from math import ceil, log

import qbs


import numpy as np
import matplotlib.pyplot as plt

def constructionTime(i):
    length = ceil(log(i, 2))
    register = QuantumRegister(length)
    measurement = ClassicalRegister(length)
    ancilla = QuantumRegister(1)
    circuit = QuantumCircuit(register, ancilla, measurement)

    #building
    start = perf_counter()

    qbs.even_superpositon(circuit, register, [], ancilla, i)
    circuit.measure(register, measurement)

    end = perf_counter()

    print(f"Created QRNG circuit in {end-start} seconds.")
    return circuit

def compileTime(circuit, backend_name):
    if not IBMQ.active_account():
        global provider
        provider = IBMQ.load_account()
    backend = provider.get_backend(backend_name)

    start = perf_counter()
    new_circ = transpile(circuit, backend=backend, optimization_level=1)
    end = perf_counter()

    print(f"Transpiling QRNG for {backend_name} took {end - start} seconds.")
    return new_circ


def gateCount(circuit):
    d = circuit.count_ops()
    if "barrier" in d:
        del d["barrier"]
    if "snapshot" in d:
        del d["snapshot"]

    count = 0
    tl = []
    for k, v in d.items():
        count += v
        if k[0] == 'c':
            tl.append((k, v))

    print(f"Gate count: {count}")
    if tl:
        print(f"Additionally, there are ", end='')
        it = iter(tl)
        t = next(it)
        if len(tl) == 1:
            print(f"{t[1]} {t[0]} gates.")
        else:
            for k, v in it:
                print(f"{v} {k} gates, ", end='')
            print(f"& {t[1]} {t[0]} gates.")

    return count
    

def metrics(i, sim_name):
    print(f"Analyzing QRNG circuit with i = {i}.\n")

    print("Metrics for original circuit:\n")
    circ = constructionTime(i)
    print(f"Depth: {circ.depth()}")
    print(f"Width: {circ.width()}")
    gateCount(circ)

    print(f"\nMetrics for transpiling circuit to {sim_name}:\n")
    new_circ = compileTime(circ, sim_name)
    print(f"Depth: {new_circ.depth()}")
    print(f"Width: {new_circ.width()}")
    gateCount(new_circ)

    print("\n")

def depthGrapher(upper):
    depths = []
    widths = []
    counts = []
    for i in range(2, upper):
        c = constructionTime(i)
        depths.append(c.depth())
        widths.append(c.width())
        counts.append(gateCount(c))
        del c

    x = np.arange(2, upper)
    plt.plot(x, depths)
    plt.plot(x, widths)
    plt.plot(x, counts)
    plt.legend((r"Depth", r"Width", r"Total"))
    plt.xlabel("Parts")
    plt.ylabel("Gates")
    plt.savefig("resources.png")


def main():
    metrics(256, "ibmq_qasm_simulator")
    depthGrapher(256)


if __name__ == "__main__":
    main()