import argparse
import logging
import threading
import time
import signal


from src import logging_conf

logger = logging.getLogger("charger_base")

polling_period = 1
stop_event = threading.Event()

def periodic_task():
    while True:
        print("Running periodic task")
        time.sleep(polling_period)

def signal_handler(sig, frame):
    print("Stopping...")
    stop_event.set()

if __name__ == "__main__":
    logging_conf.config()
    parser = argparse.ArgumentParser(
        description="asfasfdasfd"
    )

    thread = threading.Thread(target=periodic_task, daemon=True)
    thread.start()

    try:
      while not stop_event.is_set():
          time.sleep(1)
    except KeyboardInterrupt:
      logger.info("KeyboardInterrupt received. Exiting...")
      stop_event.set()

    print("Exit application.")
