
import cirq
import random
import matplotlib.pyplot as plt
import numpy as np
from cirq import Simulator

def make_quantum_teleportation_circuit(gate):
    circuit = cirq.Circuit()
    
    # 3-qubitli teleportasyon protokolü 
    msg = cirq.NamedQubit('Message')
    alice = cirq.NamedQubit('Alice')
    bob = cirq.NamedQubit('Bob')
    
    #girdi kapısı-operatörü(gate) gönderilecek mesajı hazırlar.
    circuit.append(gate(msg))
    
    #Alice ve Bob un paylaştığı  dolanıklık-bell durumu
    circuit.append([cirq.H(alice),cirq.CNOT(alice,bob)])
    
    #Alice'in dolanık qubiti ve mesajın Bell ölçümü 
    circuit.append([cirq.CNOT(msg,alice),cirq.H(msg),cirq.measure(msg,alice)])
    
    #Bon'un dolanık qubitteki orijinal kuantum mesajını bulmak için
    #Bell ölçümündeki iki klasik biti kullanır 
    circuit.append([cirq.CNOT(alice,bob),cirq.CZ(msg,bob)])
    
    return circuit

#mesaj qubitini hazırlamak için gate oluşturulmalı 
gate = cirq.X**0.23

#Teleportasyon devresi :
circuit = make_quantum_teleportation_circuit(gate)
print(circuit)


message = cirq.Circuit(gate.on(cirq.NamedQubit("Message"))).final_state_vector()
message_bloch_vector = cirq.bloch_vector_from_state_vector(message , index=0)
print(np.round(message_bloch_vector ,3))
#print(message_bloch_vector )

sim = cirq.Simulator()

result = sim.simulate(circuit)

#Bob'un Bloch vectorü :
bobs_bloch_vector = cirq.bloch_vector_from_state_vector(result.final_state_vector,index =1)
print(np.round(bobs_bloch_vector,3))

np.testing.assert_allclose(bobs_bloch_vector, message_bloch_vector , atol= 1e-7)

