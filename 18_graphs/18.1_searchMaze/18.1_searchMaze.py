"""
    Concernants indexation:
        the maze mape is index as the following (row, col), (0,0) is the top left corner and (n-1, m-1) is the bottom right corner
"""
import numpy as np

def input_mapper(x : str) -> bool:
    """
    Returns if we can walk on x
    """
    if x == ".":
        return True
    elif x == "#":
        return False
    else:
        raise ValueError("Unknown value in the input : " + x)

def read_map_from_input() -> np.ndarray:
    """
    reads the input map of the maze, like "maze1" in the folder
    Returns:
        np.ndarray: the map array in 2 dim
    """
    n, m = [int(x) for x in input().split()]
    s = tuple(map(int, input().split()))
    e = tuple(map(int, input().split()))
    lignes = []
    for _ in range(n):
        raw_ligne = list(input())
        lignes.append(list(map(input_mapper, raw_ligne)))
    
    return np.array(lignes), s, e        


if __name__ == "__main__":
    # s represents the start position, e represents the end position
    maze_map, s, e = read_map_from_input()
    