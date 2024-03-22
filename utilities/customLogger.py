import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="/home/mubashar4603/PycharmProjects/lahebo-prodTest/Logs/automation.log", format='%(asctime)s: %(message)s',
                            datefmt='%m/%d/%y %i:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
