# micrograd

A minimal, ground-up way to understand **backpropagation** in neural networks.

`micrograd` helps build intuition by breaking neural networks down to their basics. Instead of using large tensors or heavy frameworks, it works only with **scalar values** and builds a **Directed Acyclic Graph (DAG)** from simple mathematical expressions.

Each node in this graph stores a single value and the operation that created it. By moving through this graph step by step, you can clearly see how learning actually happens.

---

## What micrograd Does

At its core, `micrograd` implements the two main steps used in neural network training.

### 1. Forward Pass
- Evaluates mathematical expressions step by step  
- Computes output values from input values  
- Builds a computational graph (DAG) during computation  

### 2. Backward Pass (Backpropagation)
- Walks through the graph in reverse  
- Uses the chain rule to calculate gradients  
- Updates values so the model can improve  

This is the same idea used in modern deep learning libraries, just explained in a much simpler way.

---

## Why micrograd Matters

Backpropagation is the key algorithm behind modern AI and deep learning.

`micrograd` helps you understand:
- How gradients flow through a neural network  
- Why backpropagation is so important  
- How learning comes from basic math  
- What neural networks are really doing internally  

Since everything is scalar-based, nothing is hidden. Every calculation is visible and easy to follow.

---

## Key Concepts Covered

- Computational graphs (DAGs)  
- Automatic differentiation  
- Chain rule in action  
- Gradient-based learning  
- Core ideas behind neural networks  

---

## How to Implement and Use micrograd

This project is built to be:
- Easy to read  
- Easy to experiment with  
- Focused on learning, not performance  

You define mathematical expressions, run a forward pass to compute values, then run a backward pass to compute gradients. Using these gradients, you can apply gradient descent and observe how learning improves step by step.

The goal here is **clarity**, not speed or scale.

---

## Who Is This For?

- Engineers who want a solid understanding of backpropagation
- Anyone curious about how AI actually learns  
- People who prefer understanding over black-box tools

---

## Final Thought

Neural networks may seem complex, but at their core they are just graphs, numbers, and calculus keeping careful track of computations.

`micrograd` removes the mystery and lets you see learning happen—one scalar at a time.

---

## Credits

**Source:** Andrej Karpathy  
**Reference:** https://github.com/karpathy/micrograd  

This repository is created purely for learning purposes and is almost an exact replica of the original source mentioned above.
