import os
import time
from tools.logger import logger

def get_screenshot(driver,dirPath):

    picture_time = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))
    try:
        picPath = dirPath + '\\'+picture_time+'.png'
        driver.save_screenshot(picPath)
        logger.info('截图成功：%s'%picPath)

    except BaseException as msg:
        logger.error('截图失败：%s'%msg)











if __name__ == '__main__':
    get_screenshot(1)