import unittest
import os

class TestHTML(unittest.TestCase):
    def test_index_html_exists(self):
        self.assertTrue(os.path.exists("index.html"))

if __name__ == "__main__":
    unittest.main()