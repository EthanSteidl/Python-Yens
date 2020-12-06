# K-Shortest-Paths
Uses Python to implement Yen's K shortest path weighted graph algorithm

## Algoirthm
Utilizes Yens K shortest path algorithm to run in worst case K*L*N^2 time where
The N^2 is the runtime of the shortest path algorithm used to calculate 1 path.
K is the K paths desired
L is the amount of nodes along the shortest path from start to end
N is the amound of nodes in the graph
The algorithm could be reduced down to K * L * (M + N lg2 N) where
M is the edge count in the graph
This reduction would come from moving away from Dijkstras shortest path algorithm and switch
to a Fibonacci heap. This can be easily swapped out in this code.

## Usage
See main.py
