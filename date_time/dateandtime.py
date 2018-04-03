import datetime

now = datetime.datetime.now()

print('now: {}'.format(now))

yesterday = datetime.datetime(2018, 1, 1, 0, 0, 0)

diff = now - yesterday

print('difference: {}'.format(diff))

after = now + datetime.timedelta(days=2)

print('plus 2 days: {}'.format(after))