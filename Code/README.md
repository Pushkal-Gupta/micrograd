# Code

This folder contains the core implementation of a **micrograd-style automatic differentiation engine** and a simple **neural network library built from scratch**.

It defines the fundamental data structures used throughout the project, including scalar values with gradients and neural network components.

---

## Directory Structure

```text
Code/
├── README.md
├── __init__.py
├── valueClass.py     # Scalar Value class with autograd support
├── neuralNet.py      # Neural network primitives (Neuron, Layer, MLP)
```

---

## Files Overview

### valueClass.py

Implements the `Value` class, which represents a scalar value in a computation graph.

**Features:**

- Operator overloading (`+`, `-`, `*`, `/`, `**`)
- Activation functions (`tanh`, `ReLU`, `exp`)
- Automatic differentiation via reverse-mode backpropagation
- Explicit computation graph construction

This is the core engine powering all gradient computation.

---

### neuralNet.py

Builds higher-level neural network abstractions using the `Value` class.

**Includes:**

- `Neuron`: single neuron with learnable weights and bias
- `Layer`: collection of neurons
- `MLP`: multi-layer perceptron

All parameters are `Value` objects, enabling end-to-end automatic differentiation.

---

## Usage

These modules are intended to be **imported**, not executed directly.

Example:

```python
from Code.valueClass import Value
from Code.neuralNet import MLP

x = Value(2.0)
y = Value(-1.0)

z = (x * y).tanh()
z.backward()
```

---

## Notes

- This folder contains **no visualization code**
- Visualization utilities are located in the `Visualize/` folder

This folder forms the **computational core** of the project.
