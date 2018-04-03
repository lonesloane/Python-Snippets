# take a look at module counter to see 2 possible ways to define a global singleton
# available to all modules which import it
from counter.counter import count, counts
from counter.counter import EventCounter
# Of course, the magic is that this could be imported in many different modules
# and it would all point to the same global singleton


for i in range(100):
    if i % 2 == 0:
        count('even')
    else:
        count('odd')

print(counts())

c1 = EventCounter()
c1.event_count('input')
c2 = EventCounter()
c2.event_count('input')
c3 = EventCounter()
print(c3.event_counts())