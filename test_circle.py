"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import unittest
from circle import Circle


class TestCircle(unittest.TestCase):

    def setUp(self) -> None:
        """Set up a circle object."""
        self.c1 = Circle(1)
        self.c2 = Circle(2)

    def test_positive_radii(self):
        """Typical case: Test add_area with two circles having positive radii."""
        self.assertTrue(self.c1.get_radius() >= 0)
        self.assertTrue(self.c2.get_radius() >= 0)

    def test_one_circle_has_zero_radius(self):
        """Edge case: Test add_area when one of the circles has radius 0,
         the other has non-zero radius."""
        c3 = Circle(0)
        added_area = c3.get_area() + self.c2.get_area()
        added_circle1 = c3.add_area(self.c2)
        added_circle2 = self.c2.add_area(c3)
        self.assertEqual(added_circle1.get_area(), added_area)
        self.assertEqual(added_circle2.get_area(), added_area)

    def test_negative_radius(self):
        """Circle constructor raises exception if the radius is negative."""
        with self.assertRaises(Exception):
            Circle(-1)
