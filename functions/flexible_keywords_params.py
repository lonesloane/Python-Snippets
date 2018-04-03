import warnings


def rtd(distance=None, rate=None, time=None):

    if distance is None:
        distance = rate * time
    elif rate is None:
        rate = distance / time
    elif time is None:
        time = distance / rate
    else:
        warnings.warn('Nothing to solve for')
    return dict(distance=distance, rate=rate, time=time)


def rtd2(**keywords):
    rate = keywords.get('rate', None)
    time = keywords.get('time', None)
    distance = keywords.get('distance', None)
    return rtd(distance=distance, rate=rate, time=time)


template = 'At {rate} kt, it takes {time} hrs to cover {distance} nm'

result = rtd(distance=31.2, rate=6)
print(template.format_map(result))

result = rtd2(rate=6, time=10)
print(template.format_map(result))