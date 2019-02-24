import unittest
import history_machine
import arabic_to_roman


class TestStringMethods(unittest.TestCase):
    def test_roman_number_first_rule(self):
        self.assertEqual(history_machine.rule_one(history_machine.get_roman_number_one()), 3205)
        self.assertEqual(history_machine.rule_two(history_machine.get_roman_number_two()), 1994)

    def test_arabic_to_roman(self):
        self.assertEqual(arabic_to_roman.get_result_under_4000(2417), "MMCDXVII")
        self.assertEqual(arabic_to_roman.get_result_under_4000(999),  "CMXCIX")
        self.assertEqual(arabic_to_roman.get_result_under_4000(290),  "CCXC")
        self.assertEqual(arabic_to_roman.get_result_under_4000(1742), "MDCCXLII")
        self.assertEqual(arabic_to_roman.get_result_under_4000(3974), "MMMCMLXXIV")


if __name__ == '__main__':
    unittest.main()
