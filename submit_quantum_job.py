# from qiskit import QuantumCircuit
# from qiskit_ibm_runtime import QiskitRuntimeService, Session, Sampler

# # Connect using your saved IBM Cloud credentials
# service = QiskitRuntimeService()
# backend = service.backend("ibm_brisbane")  # Or any backend from your instance

# # Create a simple Bell state circuit with measurement
# qc = QuantumCircuit(2, 2)
# qc.h(0)
# qc.cx(0, 1)
# qc.measure([0, 1], [0, 1])

# # Submit via session
# with Session(backend=backend) as session:
#     sampler = Sampler(session=session)
#     job = sampler.run([qc])
#     result = job.result()

# # Output the result
# print("Quasi-probabilities:", result.quasi_dists[0])


# from qiskit import QuantumCircuit
# from qiskit_ibm_runtime import QiskitRuntimeService, Sampler

# # Step 1: Load your IBM Cloud credentials (assumes you've already saved them)
# # You should have used QiskitRuntimeService.save_account() with:
# #   - token="your IBM Cloud API key"
# #   - channel="ibm_cloud"
# #   - instance="your-hub/your-group/your-project"

# service = QiskitRuntimeService()

# # Step 2: Define your quantum circuit (Bell state with measurement)
# qc = QuantumCircuit(2, 2)
# qc.h(0)
# qc.cx(0, 1)
# qc.measure([0, 1], [0, 1])

# # Step 3: Create a Sampler primitive (auto-binds to session/backend based on saved credentials)
# sampler = Sampler()

# # Step 4: Run the circuit
# job = sampler.run([qc])
# result = job.result()

# # Step 5: Print the quasi-probability distribution
# print("Quasi-probabilities:", result.quasi_dists[0])




from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, Session, Sampler

# Load the service (now successfully configured!)
service = QiskitRuntimeService()
backend = service.backend("ibm_brisbane")  # or "ibm_sherbrooke"

# Create Bell state circuit
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

# Submit job using a session
with Session(backend=backend) as session:
    sampler = Sampler(session=session)
    job = sampler.run([qc])
    result = job.result()

# Print the result
print("Quasi-probabilities:", result.quasi_dists[0])