import unittest
import history_machine

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_roman_number_first_rule(self):
        self.assertEqual(history_machine.rule_one(history_machine.get_roman_number_one()), 3205)
        self.assertEqual(history_machine.rule_two(history_machine.get_roman_number_two()), 1994)


if __name__ == '__main__':
    unittest.main()