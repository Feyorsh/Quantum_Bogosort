# 
# File:	  optimized_circuit.qasm
# Date:	  17-Nov-21
# Author: G. Huebner
#

    def ry,0,'\txt{R\textsubscript{y}}'
    def cry,1,'\txt{R\textsubscript{y}}'
    def cry2,2,'\txt{R\textsubscript{y}}'

    defbox chall,4,1,'\txt{H\textsubscript{ALL}}'
    defbox chall1,4,2,'\txt{H\textsubscript{ALL}}'
    def chall2,3,'\txt{H\textsubscript{ALL}}'

    qubit q0,0
    qubit q1,0
    qubit q2,0
    qubit q3,0

    ry q0
    chall q0,q1,q2,q3
    X q0

    cry q0,q1
    chall1 q0,q1,q2,q3
    X q1

    cry2 q0,q1,q2
    chall2 q0,q1,q2,q3
    X q2

     nop q0
     nop q1
     nop q3

    measure q0
    measure q1
    measure q2
    measure q3