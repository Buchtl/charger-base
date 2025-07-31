import argparse
import logging
from src import logging_conf

logger = logging.getLogger("charger_base")

if __name__ == "__main__":
    logging_conf.config()
    parser = argparse.ArgumentParser(
        description="Watch XML files, decode <Body> if <type> matches"
    )