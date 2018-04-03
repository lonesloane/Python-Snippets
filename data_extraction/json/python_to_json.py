import json
import random
import datetime
from collections import Counter


random.seed(1)
colors = (["red"]*18)+(["black"]*18)+(["green"]*2)
data = Counter(random.choice(colors) for _ in range(100))
# Because this data is - effectively - a dict, we can serialie this very easily into JSON:
print(json.dumps(data, sort_keys=True, indent=2))


# use object_hooks to tell json module how to map json structure to complex python data structure
def as_date(object):
    if 'date' in object:
        return datetime.datetime.strptime(object['date'], '%Y-%m-%dT%H:%M:%S')
    return object

source= '{"date": "2014-06-07T08:09:10"}'
loaded = json.loads(source, object_hook=as_date)
print(loaded)