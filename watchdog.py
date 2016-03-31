import thread
import time


time.sleep(600)
target = open("/websites/secure/www/status.txt", 'w')
target.write('0')
