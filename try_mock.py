import unittest
from unittest.mock import patch

from random_number import get_random_number_plus_one


class TestRandom(unittest.TestCase):
    @patch('random_number.random.randint')
    def test_it_should_call_randint_with_1_and_10(self, mock):
        get_random_number_plus_one()
        mock.assert_called_once_with(1, 10)

    @patch('random_number.random.randint')
    def test_it_should_get_4_when_random_get_3(self, mock):
        mock.return_value = 3
        result = get_random_number_plus_one()
        self.assertEqual(result, 4)

    def test_it_should_get_3(self):
        while True:
            result = get_random_number_plus_one()
            if result == 3:
                break

        self.assertEqual(result, 3)


# print(get_random_number_plus_one())
unittest.main()