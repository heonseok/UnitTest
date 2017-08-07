import unittest
import os

class PythonTestCase(unittest.TestCase):
    def test_os_path_join(self):
        path_a = 'a'
        path_b = 'b'
        path_c = 'c'

        self.assertEquals(os.path.join(path_a, path_b), 'a/b')
        self.assertEquals(os.path.join(*[path_a, path_b]), 'a/b')
        self.assertEquals(os.path.join(*[path_a, path_b, path_c]), 'a/b/c')


if __name__ == '__main__':
    unittest.main()
