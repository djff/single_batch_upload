__author__ = 'djff'

from pywikibot.specialbots import UploadRobot

def upload_to_commons(url, description, filename):
    bot = UploadRobot(url, description=description, useFilename=filename, keepFilename=True, verifyDescription=False, aborts=True)
    try:
        bot.run()
    except Exception as e:
        print('[*] Upload Failed ....')
        print(e)
    print('Upload Completed...')
