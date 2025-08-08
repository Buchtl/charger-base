import unittest
import json
from src import charger_api_calls
from src.charger_models import StatusPoll, Cdi


class TestChargerApiCalls(unittest.TestCase):

    def test_status_err(self):
        expected = 0
        actual = charger_api_calls.status_err()
        self.assertEqual(actual, expected)

    def test_status_energy_total_wh(self):
        expected = 4
        actual = charger_api_calls.status_energy_total_wh()
        self.assertEqual(actual, expected)

    def test_status_polling(self):
        expected = StatusPoll(eto=4, err=0, tma={0,0})
        actual = charger_api_calls.status_polling()
        self.assertEqual(actual.eto, expected.eto)
        self.assertEqual(actual.err, expected.err)


if __name__ == "__main__":
    unittest.main()
