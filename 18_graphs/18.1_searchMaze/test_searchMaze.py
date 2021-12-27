import unittest
import os
import numpy as np
from searchMaze import read_map_from_input

class TestMapReading(unittest.TestCase):
    def test_read_from_input(self):
        path = os.path.join(os.path.dirname(__file__), "maze1.txt")
        map, s, e = read_map_from_input(path)
        true_s = (7, 0) 
        true_e = (0, 7)
        true_map = np.array([[False,  True,  True,  True, False, False,  True,  True],
                                [False,  True, False,  True, False,  True,  True,  True],
                                [False,  True, False,  True,  True,  True, False, False],
                                [False,  True,  True, False, False,  True,  True, False],
                                [False,  True,  True,  True, False, False,  True,  True],
                                [False, False, False,  True,  True,  True,  True,  True],
                                [False,  True,  True,  True, False,  True,  True,  True],
                                [ True,  True, False, False, False,  True,  True,  True]])
        #check e and s
        self.assertEqual(s, true_s)
        self.assertEqual(e, true_e)
        #type check 
        self.assertIsInstance(map, np.ndarray)
        #shape check
        self.assertEqual(map.shape, true_map.shape)
        #content check
        self.assertTrue(np.all(map == true_map))



if __name__ == "__main__":
    unittest.main()