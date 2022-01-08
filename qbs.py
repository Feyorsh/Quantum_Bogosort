from qiskit import *
from math import acos, sqrt, ceil, log
from itertools import permutations
from time import perf_counter

def even_superpositon(circuit, register, controls, ancilla, P):
    if P <= pow(2, len(register)) / 2: # skip this iteration
        even_superpositon(circuit, register[1:], controls, ancilla, P)
        return
    if P == pow(2, len(register)): # reduced to H_ALL; base case
        if controls == []:
            for qb in register:
                circuit.h(qb)
        elif len(register) > 0:
            circuit.mcx(controls, ancilla) # mcx to ancilla used in lieu of mch
            for qb in register:
                circuit.ch(ancilla, qb)
            circuit.mcx(controls, ancilla)
        return


    extra_parts = P - pow(2, len(register) - 1)
    # this is the inverse of what we want, but saves us an X for ch
    theta = 2 * acos(sqrt(extra_parts / P))

    if controls == []:
        circuit.ry(theta, register[0])

        for i in range(1, len(register)):
            circuit.ch(register[0], register[i])
        controls += [register[0]]
    else:
        circuit.mcry(theta, controls, register[0])

        controls += [register[0]]
        circuit.mcx(controls + [], ancilla)
        for i in range(1, len(register)):
            circuit.ch(ancilla, register[i])
        circuit.mcx(controls, ancilla)

    circuit.x(register[0])


    even_superpositon(circuit, register[1:], controls, ancilla, extra_parts)


if __name__ == "__main__":
    set = [6, 10, 2589, 0, 47, 178, 324]
    possibilities = list(permutations(set))
    set.sort()

    sorted = tuple(set)

    parts = len(possibilities)
    length = ceil(log(parts, 2))
    register = QuantumRegister(length)
    measurement = ClassicalRegister(length)
    ancilla = QuantumRegister(1)
    circuit = QuantumCircuit(register, ancilla, measurement)

    even_superpositon(circuit, register, [], ancilla, parts)
    circuit.measure(register, measurement)

    start = perf_counter()
    while True:
        counts = execute(circuit, Aer.get_backend("aer_simulator"), shots=500).result().get_counts(circuit)

        max_count = 0
        index = None
        for num, count in counts.items():
            if count > max_count:
                max_count = count
                index = int(num[::-1], 2)

        if index is not None:
            if possibilities[index] == sorted:
                break
    end = perf_counter()

    print(f"Finished Quantum Bogosort in {end-start} seconds on list of length {len(set)}")
