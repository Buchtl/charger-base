import unittest
from src import charger_api_calls


class TestChargerApiCalls(unittest.TestCase):

    def test_status_err(self):
        expected = 0
        actual = charger_api_calls.status_err()
        self.assertEqual(actual, expected)

    def test_status_energy_total_wh(self):
        expected = 4
        actual = charger_api_calls.status_energy_total_wh()
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
