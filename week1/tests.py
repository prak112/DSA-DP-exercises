import unittest
from candies import count
from repeat import find

class TestCandiesCount(unittest.TestCase):
    def test_base_case(self):
        result = count(3, 4, 13)
        expected_output = 4
        self.assertEqual(result, expected_output)

    def test_edge_case(self):
        result = count(10, 20, 55.5)
        expected_output = 5
        self.assertEqual(result, expected_output)

    def test_error_case(self):
        with self.assertRaises(TypeError):
            count('a', 'v', 10)


class TestRepeatedPatternsCount(unittest.TestCase):
    def test_base_case(self):
        result = find('abcabcabc')
        expected_output = 3
        self.assertEqual(result, expected_output)

    def test_edge_case(self):
        result = find('pikpikapikapikpikapika')
        expected_output = 11
        self.assertEqual(result, expected_output)

    def test_error_case(self):
        with self.assertRaises(TypeError):
            find(12312343)

if __name__ == "__main__":
    unittest.main()