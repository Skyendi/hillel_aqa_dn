import unittest
import pytest
from homeworks.homeworks_funcs import sum_calc, average_value, evens_sum, check_email, check_age


class Test_SumCalcTest(unittest.TestCase):

    def test_calc_positive(self):
        self.assertEqual(sum_calc(8, 3), 11, msg="actual sum is not equal expected sum")

    def test_calc_negative(self):
        self.assertNotEqual(sum_calc(8, 3), 7, msg="actual sum is equal expected sum")

    def test_average_func_positive(self):
        self.assertEqual(average_value([5, 6, 7, 3, 4, 9, 2.5, 9, 7]), 5.833333333333333, )

    def test_average_func_negative(self):
        assert average_value([5, 6, 7, 3, 4, 9, 2.5, 9, 7]) != 4

    def test_evens_sum_func_positive(self):
        assert evens_sum([68, 1, 18, 79, 29, 76, 89, 87, 81, 1, 5, 9, 24, 4, 19, 75, 20, 32, 22, 47]) == 264

    def test_evens_sum_func_negative(self):
        assert evens_sum([68, 1, 18, 79, 29, 76, 89, 87, 81, 1, 5, 9, 24, 4, 19, 75, 20, 32, 22]) != 300

    def test_check_email_positive(self):
        self.assertTrue(check_email("ddd@gmail.com"), msg="@ or . is not in email")

    def test_check_email_negative(self):
        self.assertFalse(check_email("dddgmail.com"), msg="email is correct")

    def test_check_age_funk_less_18(self):
        self.assertEqual(check_age(17), "You are not allowed!", msg="age is more or equal 18")

    def test_check_age_funk_18(self):
        self.assertEqual(check_age(18), "You are allowed!!!", msg="age is less than 18")

    def test_check_age_funk_more_18(self):
        self.assertEqual(check_age(19), "You are allowed!!!", msg="age is less than 18")


if __name__ == "__main__":
    unittest.main()
