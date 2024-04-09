# BFS Implementation in Python

This repository contains a Python implementation to understand how Breadth-First Search (BFS) works.

## Overview

BFS is a fundamental algorithm used in graph traversal and pathfinding. This implementation demonstrates BFS in the context of a maze-solving problem.

## Files

This repository includes the following Python files:

1. **playerMoves.py**: This script allows the user to manually move the Pacman character within a maze to reach the goal tile.
2. **pathByBFS.py**: This script demonstrates Pacman moving from the initial tile to the final tile through the optimal path obtained by BFS, if it is possible.
3. **BFS_Visualization.py**: This script visualizes the working of BFS. It displays which tiles are explored and ultimately shows Pacman moving on the found path.

Note: The maze is randomly generated each time, providing a dynamic environment for experimentation and learning.

## Usage

To run any of the scripts, simply execute them using Python:

```bash
python playerMoves.py
```

Replace `playerMoves.py` with the name of the script you want to run.

## Requirements

Ensure you have Python installed on your system with pygame and numpy libraries.
