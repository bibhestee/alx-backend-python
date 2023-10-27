#!/usr/bin/env python3
""" Test utils module """
import unittest
import utils
from utils import get_json, access_nested_map as anp
from unittest.mock import patch, Mock
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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ test access nested map exception to raise exceptions """
        self.assertRaises(KeyError, anp(nested_map, path))

    
class TestGetJson(unittest.TestCase):
    """
        TestGetJson - Test the get json method
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, expected):
        """ test get json method """
        with patch('utils.requests') as mock_request:
            response = Mock()
            mock_request.get.return_value = response
            response.json.return_value = expected
            self.assertEqual(get_json(url), response.json.return_value)