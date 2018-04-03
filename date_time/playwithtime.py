import time
import datetime

lst = []

for i in range(5):
	lst.append(datetime.datetime.now())
	time.sleep(2)

print(lst)