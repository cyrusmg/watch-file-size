#!/usr/bin/env python
"""watch.py tests"""

import watch
import unittest

class TestWatchModule(unittest.TestCase):
    def test_convert_size(self):
        self.assertEqual(watch.convert_size( 0),    "0 B")
        self.assertEqual(watch.convert_size(-1),    "0 B")
        self.assertEqual(watch.convert_size( 1),    "1.0 B")
        self.assertEqual(watch.convert_size( 2),    "2.0 B")

        self.assertEqual(watch.convert_size(1024), "1.0 KB")
        self.assertEqual(watch.convert_size(1024 * 1024), "1.0 MB")
        self.assertEqual(watch.convert_size(1024 * 1024 * 1024), "1.0 GB")
        self.assertEqual(watch.convert_size(1024 * 1024 * 1024 * 1024), "1.0 TB")

        self.assertEqual(watch.convert_size(1024 * 1024 + 1), "1.0 MB")
        self.assertEqual(watch.convert_size(1024 * 1024 - 1), "1024.0 KB")
        self.assertEqual(watch.convert_size(2 * 1024), "2.0 KB")
        self.assertEqual(watch.convert_size(1.5 * 1024), "1.5 KB")

if __name__ == '__main__':
    unittest.main()
