# docker build -t qbs .

FROM python:3.8-slim-buster

WORKDIR Quantum_Bogosort/

COPY qbs.py qbs.py
COPY testing.ipynb testing.ipynb

RUN pip3 install qiskit[visualization]

CMD ["/bin/bash"]