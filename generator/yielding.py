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


# Build the generator with a function which yields results 1 by 1
# instead of returning the entire collection in a single result
def parse_date_iter(source):
    for item in source:
        date = datetime.datetime.strptime(item[0],"%Y-%m-%d %H:%M:%S.%f")
        new_item = (date,) + item[1:]
        yield new_item


# Consume the generator to process the collection
for elem in parse_date_iter(data):
    pprint(elem)