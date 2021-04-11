
'''EPR - Bell States '''
try:
    import cirq
except ImportError:
    print("installing cirq...")
    get_ipython().system('pip install --quiet cirq')
    print("installed cirq.")


# Hadamard Gate : Bir kuantum durumu eşit olasılıklı iki alt duruma getirir.(Süperpozisyon Durumu)




#Kubitlerin başlangış durumu :|0> 
# q1 -> Not.q1==|1> 
# q0 =|0> & q1 =|1>



def create_bell_state(x,y):
    q0 ,q1 = cirq.LineQubit.range(2)
    if x == 1 and y == 1 :
        bell_circuit = cirq.Circuit()
        bell_circuit.append(cirq.X(q0))
        bell_circuit.append(cirq.X(q1))
        bell_circuit.append(cirq.H(q0))
        bell_circuit.append(cirq.CNOT(q0,q1))
        
    elif x == 1 and y == 0 :
        
        bell_circuit = cirq.Circuit()
        bell_circuit.append(cirq.X(q0))
        bell_circuit.append(cirq.H(q0))
        bell_circuit.append(cirq.CNOT(q0,q1))
        
    elif x == 0 and y== 1:
        bell_circuit = cirq.Circuit()
        bell_circuit.append(cirq.X(q1))
        bell_circuit.append(cirq.H(q0))
        bell_circuit.append(cirq.CNOT(q0,q1))

        
    else :
        bell_circuit = cirq.Circuit()
        bell_circuit.append(cirq.H(q0))
        bell_circuit.append(cirq.CNOT(q0,q1))
        

    return bell_circuit 





def bell_state_test():
    from cirq import Simulator
    #x ,y = cirq.LineQubit.range(2)
    bell_s_circuit = create_bell_state(0,1)
    s = cirq.Simulator()
    result= s.simulate(bell_s_circuit)
 
    print(result)





bell_state_test()







