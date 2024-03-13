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

    def setUp(self) -> None:
        """Set up a counter object"""
        self.c1 = Counter()
        self.c2 = Counter()

    def test_count_object_is_singleton(self):
        """Test for a count's object is always the same when it's called"""
        self.assertEqual(id(self.c1), id(self.c2))

    def test_increment(self):
        """Test for complete increment"""
        # check for the start value
        self.assertEqual(self.c1.count, 0)
        # add c1 with increment
        self.c1.increment()
        self.assertEqual(self.c1.count, 1)

    def test_both_increment(self):
        """Test for both c1 and c2 are increment"""
        self.assertEqual(self.c1.count, self.c2.count)
        self.c1.increment()
        self.assertEqual(self.c1.count, 1)
        self.assertEqual(self.c2.count, 1)
        self.c2.increment()
        self.assertEqual(self.c1.count, 2)
        self.assertEqual(self.c2.count, 2)
        self.assertEqual(self.c1, self.c2)

    def test_create_object_after_increment(self):
        """Test for edge case: Counter object is created after increment"""
        a = Counter()
        a.increment()
        b = Counter()
        self.assertEqual(b.count, 1)
