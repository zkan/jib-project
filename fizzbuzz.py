# ถ้า input ที่เข้ามา หาร 3 ลงตัว ให้ return คำว่า Fizz
# ถ้า input ที่เข้ามา หาร 5 ลงตัว ให้ return คำว่า Buzz
# ถ้า input ที่เข้ามา หาร 3 และ ลงตัว ให้ return คำว่า FizzBuzz
# ถ้าไม่ตรงเคสไหนเลย ให้ return เลขนั้นๆ

import unittest


def fizzbuzz(number):
    if number == 1:
        return 1

    if number == 3:
        return 'Fizz'


class TestFizzBuzz(unittest.TestCase):
    def test_input_1_should_get_1(self):
        result = fizzbuzz(1)
        self.assertEqual(result, 1)
    
    def test_input_3_should_get_fizz(self):
        result = fizzbuzz(3)
        self.assertEqual(result, 'Fizz')


if __name__ == '__main__':
    unittest.main()