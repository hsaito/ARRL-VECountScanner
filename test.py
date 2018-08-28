import unittest
from get_state import get_state, parse_call_name
from state_list import get_state_list


class TestVecMethods(unittest.TestCase):
    def test_get_state_list(self):
        get_state_list()

    def test_get_state(self):
        get_state("WA", "Washington")

    def test_call_parse(self):
        input = "WU7J (Hideki Saito)"
        result = parse_call_name(input)
        expected = ("WU7J", "Hideki Saito")
        self.assertTrue(result == expected)


if __name__ == '__main__':
    unittest.main()
