from qiskit import *
qc1 = QuantumCircuit(2,2)
qc2 = QuantumCircuit(2,2)
qc1.x(0)
qc1.y(0)
qc1.cx(0,1)
qc2.h(0)
qc2.h(0)
qc2.h(1)
qc2.cx(0,1)
print(qc1)
print(qc2)
