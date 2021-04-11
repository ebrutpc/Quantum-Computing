 '''Quantum Teleportation '''
try:
    import cirq
except ImportError:
    print("installing cirq...")
    get_ipython().system('pip install --quiet cirq')
    print("installed cirq.")


 


from cirq import Simulator
 
a = cirq.NamedQubit('a')
b = cirq.NamedQubit('b')
c = cirq.NamedQubit('c')

 

ops=[cirq.X(b),cirq.X(c),cirq.H(b),cirq.CNOT(b,c),cirq.CNOT(a,b),cirq.H(a)] # b,c qubitleri dolanık hale geldi 


teleportation_circuit=cirq.Circuit(ops,cirq.measure(a,b,key='result'))

 


#Samples oluştur
#Simülatorü başlat
s=cirq.Simulator()
results=s.simulate(teleportation_circuit)
print(results)

#sample:
samples=s.run(teleportation_circuit,repetitions=2)
print(samples)
print(samples.histogram(key='result'))


 




 




