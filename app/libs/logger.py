import logging

# My logger configuration
class Logger:
    def __init__(self, LEVEL, TAG_MODULE=None):
        # Logger Configuration

        if TAG_MODULE is not None:
            self.TAG_MODULE = TAG_MODULE
        else: 
            self.TAG_MODULE = ''

        self.logger = logging.getLogger(__name__)
        self.logger_format = '%(asctime)s  : : %(levelname)s : : %(message)s'
        self.logger_date_format = '[%Y/%m/%d %H:%M:%S %Z]'

        if LEVEL == "DEBUG":
            logging.basicConfig(level=logging.DEBUG, format=self.logger_format, datefmt=self.logger_date_format)
        else:
            logging.basicConfig(level=logging.INFO,  format=self.logger_format, datefmt=self.logger_date_format)
    
    def info(self, message):
        self.logger.info(f'{self.TAG_MODULE}: {message}')
    
    def debug(self, message):
        self.logger.debug(f'{self.TAG_MODULE}: {message}')

    def warning(self, message):
        self.logger.warning(f'{self.TAG_MODULE}: {message}')
    
    def error(self, message):
        self.logger.error(f'{self.TAG_MODULE}: {message}')