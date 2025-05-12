# from qiskit_ibm_provider import IBMProvider
# IBMProvider.save_account(token='9171cc79cb2f7d05b528bc94979ff382732db088922f45430cbca0114d7ba74656cc4ba693efab1a6508d5b866917f8f902f294ef077f9bfc87707b930736682', overwrite=True)

# print("Token saved successfully.")



# from qiskit_ibm_runtime import QiskitRuntimeService

# QiskitRuntimeService.save_account(
#     token="7dbf0bd573f13a28e4244666ff95b54ca6f94a7a7fb42e639b1ae159a68a94b60deec7afc4062e30df5590d87bfde11505ea878a4ecd7521a7f6fe0daf199af1",
#     channel="ibm_quantum",
#     instance="ibm-q/open/main",
#     overwrite=True
# )

# print("done")

from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService()
print([b.name for b in service.backends()])
