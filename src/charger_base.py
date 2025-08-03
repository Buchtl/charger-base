import argparse
import logging
import threading
import time
import random


from src import logging_conf
from src import charger_api_calls as charger_api
from src import charger_models as cModel
from src import charger_models_db as dbModel
from src import charger_db_session as charger_db

logger: logging.Logger = logging_conf.config("charger_base")

polling_period = 10
stop_event = threading.Event()

def polling_charger_data():
    with charger_db.ChargerDbSession() as db:
        i = 0
        while True:
            data: cModel.StatusPoll = charger_api.status_polling()
            eto = str(int(data.eto) + i + random.randint(1, 9))
            i += 1
            data.eto = eto
            logger.info(f"trying to write {data}")
            db_data = dbModel.StatusPollEntity(eto=data.eto, err=data.err)
            db.write(db_data)
            time.sleep(polling_period)

def signal_handler(sig, frame):
    logger.info("Stopping...")
    stop_event.set()

if __name__ == "__main__":
    logger.info("######## start ###########")
    parser = argparse.ArgumentParser(
        description="asfasfdasfd"
    )

    thread = threading.Thread(target=polling_charger_data, daemon=True)
    thread.start()

    try:
      while not stop_event.is_set():
          time.sleep(1)
    except KeyboardInterrupt:
      logger.info("KeyboardInterrupt received. Exiting...")
      stop_event.set()

    logger.info("Exit application.")
