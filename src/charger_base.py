import argparse
import logging
import threading
import time
import sys
import os

from src import logging_conf
from src.charger_poll import ChargerPoll

logger: logging.Logger = logging_conf.config("charger_base")
stop_event = threading.Event()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Polling data from the charger and write to database"
    )
    parser.add_argument("--dburl", default="pi4b", help="URL with of the database")
    parser.add_argument("--dbport", default="5432", help="Port of the database")
    parser.add_argument(
        "--dbuser", default="charger", help="Username of the target databse"
    )
    parser.add_argument(
        "--dbpass",
        default="charger",
        help="Password for --dbuser of the target databse",
    )
    parser.add_argument(
        "--dbname", default="charger", help="Database name of the target databse"
    )
    parser.add_argument("--ptime", default="1", help="Polling interval in seconds")

    args = parser.parse_args()
    db_url = args.dburl
    db_port = args.dbport
    db_user = args.dbuser
    db_pass = args.dbpass
    db_name = args.dbname

    if args.ptime.isdecimal():
        polling_period = int(args.ptime)
    else:
        logger.error(f"Invalid ptime. Given={args.ptime} must be a number")
        sys.exit(os.EX_USAGE)

    logger.info("######## start ###########")
    logger.info(
        f"dburl={db_url}, dbport={db_port} dbuser={db_user}, dbname={db_name}, ptime={polling_period}"
    )

    poller = ChargerPoll(
        db_url=db_url,
        db_port=db_port,
        db_user=db_user,
        db_pass=db_pass,
        db_name=db_name,
        polling_period=polling_period,
        stop_event=stop_event,
    )
    thread = threading.Thread(target=poller.polling_charger_data, daemon=True)
    thread.start()

    try:
        while not stop_event.is_set():
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("KeyboardInterrupt received. Exiting...")
        stop_event.set()

    logger.info("Exit application.")
