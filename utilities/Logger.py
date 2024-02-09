import logging  # built in python


class LogGenerator:
    @staticmethod
    def loggen():
        # given path and file name
        logfile = logging.FileHandler(
            "D:\\Credence Class Notes\\CredenceBatches\\Credence_Automation_Jan 24\\Credkart_Pytest\\Logs\\CredKartAutomation.log")
        format = logging.Formatter("%(asctime)s - %(levelname)s - %(name)s  - %(funcName)s - %(lineno)s- %(message)s ")
        logfile.setFormatter(format)
        logger = logging.getLogger()
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger


# Warning
# info
# Debug
# Error
# Critical

# file info
# log format
# run log create
