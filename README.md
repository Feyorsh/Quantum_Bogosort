# About
This was my project that went from QED 2021 to the Chicago STEM fair and finally all the way to (virtual) ISEF. Everything is in the [paper](paper.pdf) and you might even want to take a look at the [slides](slides.pdf), but if you have questions you can email me at [ghuebner@cps.edu](#). There's also a [video presentation](https://youtu.be/x92kzpsrkio) from city fair if you want to hear me stutter through a mediocre explanation of quantum mechanics. (The video on the ISEF website is pretty bad, if you actually want to learn more about the project I suggest this video.)

## Wait... what the heck is quantum bogosort?
Long story short, I decided to take a joke algorithm (originally proposed in [2009](https://mathnews.uwaterloo.ca/wp-content/uploads/2014/08/v111i3-compressed.pdf#page=13)) and actually implement it for a quantum computer. At it's core, I suppose one could call it an exercise in quantum software development and algorithmic design.

## How is this different from other Quantum Random Number Generators (QRNGs)?
The main algorithim I developed for quantum bogosort is basically a QRNG, which creates $n \in \mathbb{Z}$ states in the range $[0, n)$, big endian; each of those states has amplitude $\frac{1}{\sqrt{n}}$ (and therefore $\frac{1}{n}$ chance of being measured). Every QRNG I've seen only works with $n$ values that are powers of $2$, because they just apply Hadamard to each qubit once and call it a day.

My algorithm, on the other hand, uses a bunch of cool stuff like arbitrary rotation gates, control gates, and 'divide-and-conquer' strategies to actually achieve a novel result (our friend $n$ can be any positive integer). **Of course, for purposes of strictly RNG, my method is significantly more computationally complex and therefore less feasible. It's not meant to be useful or efficient.**

## How do you know this works?
I didn't do any statistical analysis of my findings, because I didn't have to; quantum circuits are just matrices. My algorithm can be mathematically verified as producing the correct output (although I don't  know if this is the most *efficient* way to generate the correct output).

## Where can I learn more?
1. Read the [paper](paper.pdf) and/or [slides](slides.pdf).
2. [Qiskit](https://qiskit.org/textbook/what-is-quantum.html) has some good educational material, in addition to being a really solid SDK (used in this project).
3. My personal recommendation for a starting textbook would be Chuang & Nielson's [*Quantum Computation and Quantum Information*](https://www.worldcat.org/title/43641333).

# Setup

Note that you'll probably need to mess around with the code in [testing.ipynb](testing.ipynb), especially if you're trying to get LaTeX to behave on your machine (I personally just used Overleaf). I used a really hacky implementation of [qasm2circ](https://www.media.mit.edu/quanta/qasm2circ/) and consequently my actual project structure looked a bit different from what you see.

# Installation
## Docker:
```bash
docker build -t <IMAGE_NAME> https://github.com/Borris-the-real-OG/Quantum_Bogosort.git
docker run --name <CONTAINER_NAME> -it <IMAGE_NAME>
```
Better yet, use a VSCode Dev Environment by using `Remote-Containers: Clone Repository in Container Volume` and plugging in this repo. If you already have a container up and running, you can attach to it with `Remote-Containers: Attach to Running Container`.

## Docker? Humbug!
If you want to go at it the old-fashioned way, just make sure to install `qiskit[visualization]` for that quantum goodness.