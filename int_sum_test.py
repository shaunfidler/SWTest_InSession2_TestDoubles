from int_sum import int_sum
from unittest import mock
import unittest

class SumTest(unittest.TestCase):
    #mock
    def test_file_mock_happy_path(self):
        fake_path = "data.txt"
        data = "1\n2\n3"
        expectedSum = 6
        with mock.patch('int_sum.open', mock.mock_open(read_data=data)) as m:
            self.assertEqual(int_sum(fake_path), expectedSum)
            m().readlines.assert_called_once()
            m().write.assert_called_once_with("\n" + str(expectedSum))

    #mock
    def test_file_mock_happy_path_multi_digits(self):
        fake_path = "data.txt"
        data = "154\n2504\n30"
        expectedSum = 2688
        with mock.patch('int_sum.open', mock.mock_open(read_data=data)) as m:
            self.assertEqual(int_sum(fake_path), expectedSum)
            m().readlines.assert_called_once()
            m().write.assert_called_once_with("\n" + str(expectedSum))

    #mock
    def test_file_mock_happy_path_signs_included(self):
        fake_path = "data.txt"
        data = "+1\n-2\n+1"
        expectedSum = 0
        with mock.patch('int_sum.open', mock.mock_open(read_data=data)) as m:
            self.assertEqual(int_sum(fake_path), expectedSum)
            m().readlines.assert_called_once()
            m().write.assert_called_once_with("\n" + str(expectedSum))      

    #stub
    def test_file_mock_non_integer(self):
        fake_path = "data.txt"
        data = "+1s\n-2\n+1"
        with mock.patch('int_sum.open', mock.mock_open(read_data=data)) as m:
            self.assertRaises(TypeError, int_sum, fake_path)

    #stub
    def test_file_mock_empty_file(self):
        fake_path = "data.txt"
        data = ""
        with mock.patch('int_sum.open', mock.mock_open(read_data=data)) as m:
            self.assertRaises(ValueError, int_sum, fake_path)

    #mock
    def test_file_mock_one_entry(self):
        fake_path = "data.txt"
        data = "1"
        expectedSum = 1
        with mock.patch('int_sum.open', mock.mock_open(read_data=data)) as m:
            self.assertEqual(int_sum(fake_path), expectedSum)
            m().readlines.assert_called_once()
            m().write.assert_called_once_with("\n" + str(expectedSum))


if __name__ == '__main__':
    unittest.main()