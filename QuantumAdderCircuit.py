#!/usr/bin/env python
# coding: utf-8

try:
    import cirq
except ImportError:
    print("installing cirq...")
    get_ipython().system('pip install --pre cirq --quiet')
    print("installed cirq.")
    import cirq

import matplotlib.pyplot as plt
import numpy as np
from cirq import Simulator


q0, q1, q2 ,q3= cirq.LineQubit.range(4)


ops = [cirq.X(q0),cirq.X(q2),cirq.CCX(q0,q1,q3),cirq.CNOT(q1,q2),cirq.CCX(q0,q2,q3)]

 
circuit = cirq.Circuit(ops,cirq.measure(q3, key='result'))

print("Circuit:\n")
print(circuit)


results = cirq.sample(circuit, repetitions=10)
print("Measurement results:")
print(results)


simulator = Simulator()
result = simulator.run(circuit)

print(result)





