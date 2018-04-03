from collections import Counter


# module global variable
_global_counter = Counter()


# class level static variable
class EventCounter:
    _counts = Counter()

    def event_count(self, key, increment=1):
        EventCounter._counts[key] += increment

    def event_counts(self):
        return EventCounter._counts.most_common()


def count(key, increment=1):
    _global_counter[key] += increment


def counts():
    return _global_counter.most_common()
