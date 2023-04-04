import logging
import time
import os
import colorlog

level_relations = {
    'debug':logging.DEBUG,
    'info':logging.INFO,
    'warning':logging.WARNING,
    'error':logging.ERROR,
    'critical':logging.CRITICAL
}

log_colors_config = {
    'DEBUG':"white",
    "INFO":"green",
    "WARNING":"yellow",
    "ERROR":"red",
    "CRITICAL":"bold_red"
}

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
console_handler = logging.StreamHandler()

rq = time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time()))
curPath = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
log_path = curPath + '\\logs\\'
log_name = log_path +"/"+ rq + '.log'
logfile = log_name
fh = logging.FileHandler(logfile,mode='w',encoding='UTF-8')
fh.setLevel(logging.INFO)
# ch = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
console_formatter = colorlog.ColoredFormatter("%(log_color)s%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
console_handler.setFormatter(console_formatter)
fh.setFormatter(formatter)
logger.addHandler(fh)
# ch.setFormatter(formatter)
# logger.addHandler(ch)
logger.addHandler(console_handler)

if __name__ == '__main__':
    logger.debug('this is a logger debug message')
    logger.info('this is a logger info message')
    logger.warning('this is a logger warning message')
    logger.error('this is a logger error message')
    logger.critical('this is a logger critical message')