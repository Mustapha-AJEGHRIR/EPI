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
import collections
import matplotlib.pyplot as plt
from numpy.lib.shape_base import dsplit

# Some constents
UP = np.array([-1, 0])
DOWN = np.array([1, 0])
LEFT = np.array([0, -1])
RIGHT = np.array([0, 1])



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

def read_map_from_input(path = os.path.join(os.path.dirname(__file__), "maze1.txt") ) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    reads the input map of the maze, like "maze1" in the folder
    Returns:
        np.ndarray: the map array in 2 dim
    """
    with open(path, "r") as f:
        n, m = [int(x) for x in f.readline().split()]
        s = np.array(tuple(map(int, f.readline().split())))
        e = np.array(tuple(map(int, f.readline().split())))
        lignes = []
        for _ in range(n):
            raw_ligne = list(f.readline().strip())
            lignes.append(list(map(char_mapper, raw_ligne)))
    return np.array(lignes), s, e        

def get_neighbors_raw_map(pos : np.ndarray, maze_map : np.ndarray) -> list[tuple[np.ndarray, np.ndarray,np.ndarray]]: #new_pos, parent,  direction
    """
    Returns the neighbors of pos in the maze_map
    """
    neighbors = []
    for d in [UP, DOWN, LEFT, RIGHT]:
        new_pos = pos + d
        if new_pos[0] >= 0 and new_pos[1] >= 0 and new_pos[0] < maze_map.shape[0] and new_pos[1] < maze_map.shape[1]:
            if maze_map[new_pos[0], new_pos[1]]:
                neighbors.append((new_pos, pos, d))
    return neighbors

def make_node(pos: np.ndarray, maze_map: np.ndarray) -> bool:
    """
        Returns if this position is simple (straight line) or complex
    """
    neighbors = get_neighbors_raw_map(pos, maze_map)
    if len(neighbors) != 2:
        return True
    if len(neighbors) == 2:
        n1, n2 = neighbors
        if np.all(n1[2] == -n2[2]):
            return False
        else:
            return True
        
def build_graph(maze_map : np.ndarray, s : np.ndarray, e : np.ndarray) -> tuple[np.ndarray, set[tuple]]:
    V = np.zeros(maze_map.shape, dtype = bool)
    V[tuple(s)] = True
    V[tuple(e)] = True
    E = set()
    n, m = maze_map.shape
    for i in range (n):
        for j in range(m):
            if maze_map[i, j]:
                pos = np.array([i, j])
                if make_node(pos, maze_map):
                    V[tuple(pos)] = True
    for i in range(n):
        for j in range(m):
            if maze_map[i, j]:
                pos = np.array([i, j])
                if make_node(pos, maze_map):
                    directions = map( lambda x: x[2], get_neighbors_raw_map(pos, maze_map))
                    for d in directions:
                        index = 1
                        while not V[tuple(pos + index * d)]:
                            index += 1
                        E.add((tuple(pos), tuple(pos + index * d), index))
                        E.add((tuple(pos + index * d), tuple(pos), index))
    return V, E

def graph_connexion(E: set[tuple]) -> dict[tuple, set[tuple]]:
    """
    Returns the connexion graph from the set E
    """
    graph = collections.defaultdict(set)
    for (u, v, d) in E:
        graph[u].add((v, d))
        graph[v].add((u, d))
    return graph

def djisktra(V : np.ndarray, E_set : set[tuple], s : np.ndarray, e : np.ndarray):
    """
    Returns the shortest path from s to e in the maze_map
    """
    E = graph_connexion(E_set)
    node = tuple(s)
    distances = {node: (0, None)}
    frontier = {node}
    while frontier:
        node = min(frontier, key = lambda x: distances[x][0])
        frontier.remove(node)
        current_dist = distances[node][0]
        neighbors = E[node]
        for neighbor in neighbors:
            new_dist = current_dist + neighbor[1]
            if neighbor[0] not in distances or new_dist < distances[neighbor[0]][0]:
                distances[neighbor[0]] = (new_dist, node)
                frontier.add(neighbor[0])
    return distances

def build_path(distances : dict[tuple, tuple], e : np.ndarray) -> list[tuple]:
    """
    Returns the shortest path from s to e in the maze_map
    """
    path = []
    node = tuple(e)
    while node != None:
        path.append(node)
        node = distances[node][1]
    path.reverse()
    return path

def plot_path_save(path : list[tuple], maze_map : np.ndarray, name="maze_shortest_path.png", dpi =300):
    """
    Plots the path in the maze_map
    """
    n, m = maze_map.shape
    plt.imshow(~maze_map, cmap = "Greys", interpolation = "none")
    plt.plot(path[0][1], path[0][0], "o", color = "red")
    plt.plot(path[-1][1], path[-1][0], "o", color = "red")
    for i in range(1, len(path)):
        plt.plot([path[i-1][1], path[i][1]], [path[i-1][0], path[i][0]], color = "red")
    plt.savefig(name, dpi=dpi)
    plt.show()

def execute(path = os.path.join(os.path.dirname(__file__), "maze1.txt"), name = "maze_shortest_path.png", dpi = 300):
    maze_map, s, e = read_map_from_input(path)
    V, E = build_graph(maze_map, s, e)
    path = build_path(djisktra(V, E, s, e), e)
    plot_path_save(path, maze_map, name, dpi)

if __name__ == "__main__":
    # s represents the start position, e represents the end position
    execute(os.path.join(os.path.dirname(__file__), "maze2.txt"), "maze_shortest_path2.png", 300)


    
    
    