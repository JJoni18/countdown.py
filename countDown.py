
import time
import datetime

x = datetime.datetime.now()
i = 20
while (i > 0):
    print 'Timer is =:', i
    i = i - 1
    time.sleep(1)
    if (i == 0):
        break
    else:
        continue
print("count down completed on " + str(x))
