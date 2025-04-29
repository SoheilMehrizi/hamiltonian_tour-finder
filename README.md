# 🔁 Hamiltonian Tour Finder with Visualization
This Python project finds the minimum-cost Hamiltonian tour in a fully connected graph using a backtracking algorithm and visualizes the resulting tour with networkx and matplotlib.

It is a brute-force solution to the Traveling Salesman Problem (TSP) for small graphs (n ≤ 10).

## 📦 Features
✅ Computes optimal Hamiltonian cycle using recursive backtracking

🧠 Tracks the minimum cost path visiting each node once

🎨 Visualizes the resulting tour with nodes, edges, weights, and highlighted paths

🧪 Easy to modify and expand

## 🧠 Algorithm Overview
Uses a brute-force recursive search to explore all permutations of nodes

Checks if the complete cycle returns to the starting node

Compares total cost to store the best (minimal-cost) tour

The graph is represented by a 2D adjacency matrix

## 🚀 How to Use
Clone or download this repository.

Install the required libraries:

```
pip install networkx matplotlib
```
Run the Python script:

```python hamiltonian_tour.py
🔢 Example
Input
python
Copy code
adj_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
start_element = (0, 1)
```

Output (in console)
```Optimal Tour: [(0, 1), (1, 3), (3, 2), (2, 0)]```


The visualization clearly shows:

Optimal path (red)

Node labels and edge weights

A spring layout for better spacing

## 🛠 Code Structure
```
hamiltonian_tour.py       # Main logic and visualization
README.md                 # Project documentation
```
## ⚠️ Limitations
This solution has factorial time complexity: O(n!)

**Suitable only for small graphs (recommended: ≤ 9 nodes)**

## 👨‍💻 Author
Soheil Mehrizi
📧 mehrizisoheil@gmail.com

