import unittest
import requests_mock
from unittest.mock import patch, MagicMock

from src import charger_api_calls
from src import charger_poll
from src import charger_db_session
from src.charger_models import StatusPoll


def mock_db_write():
    return patch.object(charger_db_session.ChargerDbSession, "write")


def mock_status(mocker):
    freq: float = 50.01200104
    mocker.get(
        charger_api_calls.api_base,
        json={"eto": 1, "err": 2, "tma": [3, 4], "fhz": freq},
    )
    expected = StatusPoll(eto=1, err=2, tma=[3, 4], fhz=freq)
    return expected


class TestChargerApiCalls(unittest.TestCase):

    @patch("src.charger_db_session.create_engine")
    def test_polling_charger_data(self, mock_engine):
        mock_engine.return_value.connect.return_value = MagicMock()
        with requests_mock.Mocker() as m, mock_db_write() as mock_write:
            mock_status(m)
            db_sess = charger_db_session.ChargerDbSession(
                db_url="dummy", db_port="5432", db_user="u", db_pass="p", db_name="n"
            )
            charger_poll.ChargerPoll(db_session=db_sess).polling_charger_data()
            mock_write.assert_called_once()


if __name__ == "__main__":
    unittest.main()
