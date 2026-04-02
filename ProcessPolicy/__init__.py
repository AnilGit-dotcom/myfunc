import time
import logging

def main(msg):
    logging.info("Started processing message...")

    time.sleep(20)  # ⬅️ ADD THIS (simulate long processing)

    logging.info("Finished processing message.")