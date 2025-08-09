import threading
import time

from src import logging_conf
from src import charger_api_calls as charger_api
from src import charger_models as cModel
from src import charger_models_db as dbModel
from src import charger_db_session as charger_db


class ChargerPoll:
    logger = logging_conf.config("ChargerPoll")
    db_session: charger_db.ChargerDbSession
    polling_period: int
    stop_event: threading.Event

    def __init__(
        self,
        db_session: charger_db.ChargerDbSession,
        polling_period: int = 1,
        stop_event=threading.Event,
    ):
        self.db_session = db_session
        self.polling_period = polling_period
        self.stop_event = stop_event

    def polling_charger_data(self, endless=False):
        while True:
            data: cModel.StatusPoll = charger_api.status_polling()
            self.logger.info(f"trying to write {data}")
            db_data = dbModel.StatusPollEntity(
                eto=data.eto, err=data.err, tma_0=data.tma[0], tma_1=data.tma[1]
            )
            self.db_session.write(db_data)
            if endless != True:
                return
            time.sleep(self.polling_period)

    def signal_handler(self, sig, frame):
        self.logger.info("Stopping...")
        self.stop_event.set()
