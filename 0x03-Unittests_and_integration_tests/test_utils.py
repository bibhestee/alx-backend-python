#!/usr/bin/env python3
""" Test utils module """
import unittest
from utils import access_nested_map as anp
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
        TestAccessNestedMap - Test the accessnestedmap method
    """
    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, nested_map, path, expected):
        """ test access nested map to return the right response """
        self.assertEqual(anp(nested_map, path), expected)