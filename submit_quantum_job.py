from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# Toggle this to True only when you want to run on real hardware
use_real_hardware = False

# Define a simple Bell state circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

if use_real_hardware:
    print("Hardware execution not yet enabled. Set to False to simulate locally.")
else:
    # Use local AerSimulator (Qiskit 2.0)
    sim = AerSimulator()
    transpiled = transpile(qc, sim)
    job = sim.run(transpiled)
    result = job.result()

    counts = result.get_counts()
    print("Counts (local simulator):", counts)
