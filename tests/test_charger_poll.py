import unittest
import requests_mock
from unittest.mock import patch, MagicMock

from src import charger_api_calls
from src import charger_poll
from src import charger_db_session
from src.charger_models import StatusPoll


def mock_db_write():
    return patch.object(charger_db_session.ChargerDbSession, "write", autospec=True)


def mock_status(mocker):
    freq: float = 50.01200104
    mocker.get(
        charger_api_calls.api_base,
        json={"eto": 1, "err": 2, "tma": [3, 4], "fhz": freq},
    )
    expected = StatusPoll(eto=1, err=2, tma=[3, 4], fhz=freq)
    return expected


class TestChargerApiCalls(unittest.TestCase):
    def test_polling_charger_data(self):
        with requests_mock.Mocker() as m:
            mock_status(m)
            mock_db = MagicMock()
            charger_poll.ChargerPoll(db_session=mock_db).polling_charger_data()
            mock_db.write.assert_called_once()


if __name__ == "__main__":
    unittest.main()
