# PBL Task 2 - A Knight's Tour
## Team Members
* Patrick Wright
* Devin Jayasinghe
* Ricky Dodd
* Dominic Butterss

## Problem Statement
Given an N x N chessboard, a knight (the game piece) performs a sequence of moves which results in the knight visiting **every** square **exactly once**. This program simulates this, using both the DFS and Warnsdorff's Rule searches to, separately, solve this problem.

## Dependencies
* Python3
* NetworkX (available via pip)
* MatPlotLib (available via pip) (this dependency is **not** necessary right now, and hasn't been, but has been left here for now just incase)

## Differences in Gameboards
### Depth-First-Search
Our execution of depth-first-search applies to a 6x6 (0 through 5) gameboard, with the knight piece beginning at 0x0.

### Warnsdorff's Rule
Our execution of Warnsdorff's Rule applies to an 8x8 (0 through 7) gameboard, with the knight piece beginning at 0x0.

## How To Run
### Executing Depth-First-Search
#### Full Scale, on a 6x6 Gameboard
**THIS ACTION IS NOT RECOMMENDED!** Run *Execute_DFS_Implementation.py*, via *python Execute_DFS_Implementation.py* from the directory (*python* may be *python3* depending on your environment).
```console
foo@bar:~$ python Execute_DFS_Implementation.py
```

#### Partial Scale, Determined, Finite Number of Steps That Do Not Give the Goal State
Run *Partial_DFS_Implementation.py*, via *python Partial_DFS_Implementation.py* from the directory (*python* may be *python3* depending on your environment).
```console
foo@bar:~$ python Partial_DFS_Implementation.py
```

### Executing Warndorff's Rule
#### Full Scale, on an 8x8 Gameboard
Run *Execute_Warnsdorff_Implementation.py*, via *python Execute_Warnsdorff_Implementation.py* from the directory (*python* may be *python3* depending on your environment).
```console
foo@bar:~$ python Execute_Warnsdorff_Implementation.py
```
