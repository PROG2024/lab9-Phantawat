"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""

import unittest
from counter import Counter


class TestCounter(unittest.TestCase):
    """Test for singleton counter"""
    def test_count_object_is_singleton(self):
        """Test for a count's object is always the same when it's called"""
        c1 = Counter()
        c2 = Counter()
        self.assertEqual(id(c1), id(c2))
