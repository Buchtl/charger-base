import argparse
import logging
import threading
import time


from src import logging_conf
from src import charger_api_calls as charger_api
from src import charger_models as cModel
from src import charger_models_db as dbModel
from src import charger_db_session as charger_db

logger = logging.getLogger("charger_base")

polling_period = 10
stop_event = threading.Event()

def polling_charger_data():
    with charger_db.ChargerDbSession() as db:
        while True:
            data: cModel.StatusPoll = charger_api.status_polling()
            logger.info(f"trying to write {data}")
            db_data = dbModel.StatusPollEntity(eto=data.eto, err=data.err)
            db.write(db_data)
            time.sleep(polling_period)

def signal_handler(sig, frame):
    print("Stopping...")
    stop_event.set()

if __name__ == "__main__":
    logging_conf.config()
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

    print("Exit application.")
