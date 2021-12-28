from types import BuiltinFunctionType
import unittest
import os
import numpy as np
from searchMaze import read_map_from_input, build_graph

class TestMapReading(unittest.TestCase):
    def test_read_from_input(self):
        path = os.path.join(os.path.dirname(__file__), "maze1.txt")
        map, s, e = read_map_from_input(path)
        true_s = np.array((7, 0)) 
        true_e = np.array((0, 7))
        true_map = np.array([[False,  True,  True,  True, False, False,  True,  True],
                                [False,  True, False,  True, False,  True,  True,  True],
                                [False,  True, False,  True,  True,  True, False, False],
                                [False,  True,  True, False, False,  True,  True, False],
                                [False,  True,  True,  True, False, False,  True,  True],
                                [False, False, False,  True,  True,  True,  True,  True],
                                [False,  True,  True,  True, False,  True,  True,  True],
                                [ True,  True, False, False, False,  True,  True,  True]])
        #check e and s
        self.assertIsInstance(s, np.ndarray)
        self.assertIsInstance(e, np.ndarray)
        self.assertTrue(np.all(s == true_s))
        self.assertTrue(np.all(e == true_e))
        #type check 
        self.assertIsInstance(map, np.ndarray)
        #shape check
        self.assertEqual(map.shape, true_map.shape)
        #content check
        self.assertTrue(np.all(map == true_map))


class TestGraphBuilding(unittest.TestCase):
    def test_graph(self):
        path = os.path.join(os.path.dirname(__file__), "maze1.txt")
        map, s, e = read_map_from_input(path)
        V, E = build_graph(map, s, e)
        true_V = np.array([[False,  True, False,  True, False, False,  True,  True],
                                [False, False, False, False, False,  True,  True,  True],
                                [False, False, False,  True, False,  True, False, False],
                                [False,  True,  True, False, False,  True,  True, False],
                                [False,  True,  True,  True, False, False,  True,  True],
                                [False, False, False,  True, False,  True,  True,  True],
                                [False,  True, False,  True, False,  True,  True,  True],
                                [ True,  True, False, False, False,  True,  True,  True]])
        true_E = np.array({((6, 7), (7, 7), 1), ((4, 6), (4, 7), 1), ((6, 3), (6, 1), 2),
                            ((5, 7), (4, 7), 1), ((0, 6), (1, 6), 1), ((1, 5), (2, 5), 1),
                            ((6, 6), (5, 6), 1), ((6, 5), (7, 5), 1), ((6, 1), (6, 3), 2),
                            ((7, 0), (7, 1), 1), ((1, 6), (1, 5), 1), ((4, 1), (3, 1), 1),
                            ((1, 6), (1, 7), 1), ((4, 7), (4, 6), 1), ((5, 5), (5, 6), 1),
                            ((0, 1), (3, 1), 3), ((5, 3), (5, 5), 2), ((6, 5), (6, 6), 1),
                            ((2, 3), (2, 5), 2), ((0, 7), (1, 7), 1), ((4, 6), (5, 6), 1),
                            ((4, 2), (3, 2), 1), ((1, 7), (1, 6), 1), ((5, 7), (5, 6), 1),
                            ((3, 1), (3, 2), 1), ((2, 5), (2, 3), 2), ((7, 7), (6, 7), 1), 
                            ((4, 3), (4, 2), 1), ((3, 1), (4, 1), 1), ((3, 5), (2, 5), 1),
                            ((7, 5), (7, 6), 1), ((2, 3), (0, 3), 2), ((3, 1), (0, 1), 3),
                            ((6, 7), (5, 7), 1), ((4, 1), (4, 2), 1), ((3, 2), (4, 2), 1),
                            ((7, 1), (6, 1), 1), ((5, 6), (5, 5), 1), ((4, 2), (4, 3), 1),
                            ((6, 6), (6, 5), 1), ((0, 6), (0, 7), 1), ((2, 5), (3, 5), 1),
                            ((6, 1), (7, 1), 1), ((6, 3), (5, 3), 1), ((7, 1), (7, 0), 1),
                            ((7, 6), (6, 6), 1), ((0, 3), (2, 3), 2), ((6, 6), (6, 7), 1),
                            ((5, 7), (6, 7), 1), ((2, 5), (1, 5), 1), ((4, 2), (4, 1), 1),
                            ((4, 7), (5, 7), 1), ((5, 3), (6, 3), 1), ((6, 7), (6, 6), 1),
                            ((7, 7), (7, 6), 1), ((5, 5), (5, 3), 2), ((0, 1), (0, 3), 2),
                            ((7, 6), (7, 7), 1), ((5, 6), (5, 7), 1), ((1, 5), (1, 6), 1),
                            ((5, 6), (4, 6), 1), ((6, 5), (5, 5), 1), ((3, 2), (3, 1), 1),
                            ((0, 3), (0, 1), 2), ((1, 6), (0, 6), 1), ((4, 6), (3, 6), 1),
                            ((3, 5), (3, 6), 1), ((5, 5), (6, 5), 1), ((5, 3), (4, 3), 1),
                            ((3, 6), (3, 5), 1), ((1, 7), (0, 7), 1), ((0, 7), (0, 6), 1),
                            ((7, 6), (7, 5), 1), ((7, 5), (6, 5), 1), ((5, 6), (6, 6), 1),
                            ((4, 3), (5, 3), 1), ((3, 6), (4, 6), 1), ((6, 6), (7, 6), 1)})
        #check e and s
        self.assertIsInstance(V, np.ndarray)
        self.assertIsInstance(E, set)
        self.assertTrue(np.all(V == true_V))
        self.assertTrue(E == true_E)


if __name__ == "__main__":
    unittest.main()