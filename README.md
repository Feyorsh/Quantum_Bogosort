# Quantum Bogosort
This was my project for QED 2021 and ~~(potentially?)~~ my submission for the Chicago STEM fair. Everything is in the [paper](paper.pdf) and you might even want to take a look at the [slides](slides.pdf), but if you have questions you can email me at [ghuebner@cps.edu](#). There's also a [video presentation](https://youtu.be/x92kzpsrkio) if you want to hear me stutter through a mediocre explanation of quantum mechanics.

Note that you ~~might~~will need to mess around with the code in [testing.ipynb](testing.ipynb), especially if you're trying to get LaTeX to behave on your machine (I personally just used Overleaf). I used a really hacky implementation of [qasm2circ](https://www.media.mit.edu/quanta/qasm2circ/) and consequently my actual project structure looked a bit different from what you see.

# Installation
## Docker:
```bash
docker build -t <IMAGE_NAME> https://github.com/Borris-the-real-OG/Quantum_Bogosort.git
docker run --name <CONTAINER_NAME> -it <IMAGE_NAME>
```
Better yet, use a VSCode Dev Environment by using `Remote-Containers: Clone Repository in Container Volume` and plugging in this repo. If you already have a container up and running, you can attach to it with `Remote-Containers: Attach to Running Container`.

## Docker? Humbug!
If you want to go at it the old-fashioned way, just make sure to install `qiskit[visualization]` for that quantum goodness.