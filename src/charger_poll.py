import threading
import time
import random

from src import logging_conf
from src import charger_api_calls as charger_api
from src import charger_models as cModel
from src import charger_models_db as dbModel
from src import charger_db_session as charger_db


class ChargerPoll:
    logger = logging_conf.config("ChargerPoll")
    db_url: str
    db_port: str
    db_user: str
    db_pass: str
    db_name: str
    polling_period: int
    stop_event: threading.Event

    def __init__(
        self,
        db_url: str = None,
        db_port: str = None,
        db_user: str = None,
        db_pass: str = None,
        db_name: str = None,
        polling_period: int = 1,
        stop_event=threading.Event,
    ):
        self.db_url = db_url
        self.db_port = db_port
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_name = db_name
        self.polling_period = polling_period
        self.stop_event = stop_event

    def polling_charger_data(self):
        with charger_db.ChargerDbSession(
            db_url=self.db_url,
            db_port=self.db_port,
            db_user=self.db_user,
            db_pass=self.db_pass,
            db_name=self.db_name,
        ) as db:
            i = 0
            while True:
                data: cModel.StatusPoll = charger_api.status_polling()
                eto = str(int(data.eto) + i + random.randint(1, 9))
                i += 1
                data.eto = eto
                self.logger.info(f"trying to write {data}")
                db_data = dbModel.StatusPollEntity(eto=data.eto, err=data.err)
                db.write(db_data)
                time.sleep(self.polling_period)

    def signal_handler(self, sig, frame):
        self.logger.info("Stopping...")
        self.stop_event.set()
