import datetime
from pprint import pprint


data = [
    ('2016-04-24 1:05:01.425', 'INFO', 'module 1', 'sample message 1'),
    ('2016-04-24 1:06:01.425', 'INFO', 'module 2', 'sample message 2'),
    ('2016-04-24 1:07:01.425', 'WARNING', 'module 1', 'sample message 1'),
    ('2016-04-24 1:08:01.425', 'INFO', 'module 2', 'sample message 2'),
    ('2016-04-24 1:09:01.425', 'INFO', 'module 1', 'sample message 1'),
    ('2016-04-24 1:10:01.425', 'WARNING', 'module 1', 'sample message 1'),
    ('2016-04-24 1:15:01.425', 'INFO', 'module 1', 'sample message 1'),
    ('2016-04-24 1:25:01.425', 'ERROR', 'module 3', 'sample message 3'),
    ('2016-04-24 1:35:01.425', 'INFO', 'module 1', 'sample message 1'),
    ('2016-04-24 1:45:01.425', 'INFO', 'module 2', 'sample message 2'),
]


def parse_date(item):
    date = datetime.datetime.strptime(item[0],"%Y-%m-%d %H:%M:%S.%f")
    new_item = (date,)+item[1:]
    return new_item


# use built-in map() to apply a "transformation" to a collection of items
for item in map(parse_date, data):
    pprint(item)