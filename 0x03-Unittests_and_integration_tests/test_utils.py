#!/usr/bin/env python3
""" Test utils module """
import unittest
import utils
from utils import get_json, access_nested_map, memoize
from unittest.mock import patch, Mock
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
        TestAccessNestedMap - Test the accessnestedmap method
    """

    @parameterized.expand([({"a": 1}, ("a",), 1),
                           ({"a": {"b": 2}}, ("a",), {"b": 2}),
                           ({"a": {"b": 2}}, ("a", "b"), 2)])
    def test_access_nested_map(self, arg1, arg2, expected):
        """ test access nested map to return the right response """
        self.assertEqual(access_nested_map(arg1, arg2), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, arg1, arg2):
        """ test access nested map exception to raise exceptions """
        with self.assertRaises(KeyError):
            access_nested_map(arg1, arg2)


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


class TestMemoize(unittest.TestCase):
    """
        TestMemoize - Test memoize decorator
    """

    def test_memoize(self):
        """ test memoize """
        class TestClass:
            """ TestClass """
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_a_method:
            response = TestClass()
            response.a_property()
            response.a_property()
            mock_a_method.assert_called_once()
            mock_a_method.return_value = 42
            self.assertEqual(mock_a_method(), 42)
