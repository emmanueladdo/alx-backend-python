#!/usr/bin/env python3
"""
Unitest module for tasks
"""

from unittest import TestCase
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(TestCase):
    """
    Test for AccessnestedMap
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        actual_result = access_nested_map(nested_map, path)
        self.assertEqual(actual_result, expected_result)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, wrong_output):
        """ Test method raises correct exception """
        with self.assertRaises(KeyError) as ex:
            access_nested_map(map, path)
            self.assertEqual(wrong_output, ex.exception)


class TestGetJson(TestCase):
    """
    Class that tests the get JSON function
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        # Configure the mock object
        mock_json = Mock(return_value=test_payload)
        mock_get.return_value.json = mock_json

        # Call the get_json function with the test_url
        result = get_json(test_url)

        """
        Assert that requests.get was
        called exactly once with the test_url as argument
        """
        mock_get.assert_called_once_with(test_url)

        # Assert that the output of get_json is equal to test_payload
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """Class for testing memoization"""

    class TestClass:
        """Test class"""

        def a_method(self):
            """Method to always return 42"""
            return 42

        @memoize
        def a_property(self):
            """Returns memoized property"""
            return self.a_method()

    def test_memoize(self):
        """Test memoization behavior"""

        # Create an instance of TestClass
        test = self.TestClass()

        # Mock the a_method using patch
        with patch.object(test, 'a_method', return_value=42) as patched:

            # Access the memoized property twice
            result1 = test.a_property
            result2 = test.a_property

            # Assert that the return value is correct
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Assert that the underlying method was only called once
            patched.assert_called_once()

            # Additional assertion:
            # Ensure that the method is not called again on the second access
            patched.reset_mock()  # Reset the call count for the mock
            result3 = test.a_property
            patched.assert_not_called()
            self.assertEqual(result3, 42)
