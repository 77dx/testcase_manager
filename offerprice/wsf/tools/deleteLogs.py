import os


curPath = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
def deleteFiles():
    log_path = curPath + '\\logs\\'
    listdir = os.listdir(log_path)
    leng = len(listdir)
    if leng > 5:
        for i in listdir[:leng-5:1]:
            os.remove(log_path + i)
    print("Done!")


def delete_screenshot():
    screenshot_path = curPath + '\\screenshot\\'
    listdir = os.listdir(screenshot_path)
    if len(listdir) > 5:
        for i in listdir:
            pass



if __name__ == '__main__':
    deleteFiles()
    # delete_screenshot()