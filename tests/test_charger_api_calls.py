import unittest
import requests_mock

from src import charger_api_calls
from src.charger_models import StatusPoll


def mock_status(mocker):
    freq: float = 50.01200104
    mocker.get(
        charger_api_calls.api_base,
        json={"eto": 1, "err": 2, "tma": [3, 4], "fhz": freq},
    )
    expected = StatusPoll(eto=1, err=2, tma=[3, 4], fhz=freq)
    return expected


class TestChargerApiCalls(unittest.TestCase):

    def test_status_polling(self):
        with requests_mock.Mocker() as m:
            expected = mock_status(m)
            actual = charger_api_calls.status_polling()
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
