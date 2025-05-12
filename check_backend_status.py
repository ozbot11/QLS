from qiskit_ibm_provider import IBMProvider

provider = IBMProvider()
backend = provider.get_backend('ibm_brisbane')

status = backend.status()
print(f"Backend: {backend.name}")
print(f"Operational: {status.operational}")
print(f"Pending jobs: {status.pending_jobs}")
print(f"Status message: {status.status_msg}")