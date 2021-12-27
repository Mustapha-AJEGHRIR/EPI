"""
    Input : 
        The input file should be a text file with the following format :
            "number of rows" "number of columns"
            "start row" "start column"
            "end row" "end column"
            "rows of the map, each row is a string of '.' and '#' characters, "." is walkable, "#" is not"
    Concernants indexation:
        the maze mape is index as the following (row, col), (0,0) is the top left corner and (n-1, m-1) is the bottom right corner
"""
import numpy as np
import os

def char_mapper(x : str) -> bool:
    """
    Returns if we can walk on x
    """
    if x == ".":
        return True
    elif x == "#":
        return False
    else:
        raise ValueError("Unknown value in the input : " + x)

def read_map_from_input(path = os.path.join(os.path.dirname(__file__), "maze1.txt") ) -> np.ndarray:
    """
    reads the input map of the maze, like "maze1" in the folder
    Returns:
        np.ndarray: the map array in 2 dim
    """
    with open(path, "r") as f:
        n, m = [int(x) for x in f.readline().split()]
        s = tuple(map(int, f.readline().split()))
        e = tuple(map(int, f.readline().split()))
        lignes = []
        for _ in range(n):
            raw_ligne = list(f.readline().strip())
            lignes.append(list(map(char_mapper, raw_ligne)))
    return np.array(lignes), s, e        


if __name__ == "__main__":
    # s represents the start position, e represents the end position
    maze_map, s, e = read_map_from_input()
    print(maze_map)
    