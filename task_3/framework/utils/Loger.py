import logging


class Loger:
    def __init__(self):
        logging.basicConfig(
            filename="sample.log", filemode="w", level=logging.INFO
        )
        logging.getLogger("sample.log").propagate = False

    def log(self, message):

        logging.info(message)

    def warning(self, message):
        logging.warning(message)

    def error(self, message):
        logging.error(message)

    def critical(self, message):
        logging.critical(message)
