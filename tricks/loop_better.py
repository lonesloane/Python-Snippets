__author__ = 'stephane'

# iteritems()
knights = {"Gallahad": "The Pure", "Robin": "The Brave"}
for k, v in knights.iteritems():
    print(k, v)

# enumerate
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# zip
questions = ["name", "quest", "favorite color"]
answers = ["Lancelot", "the search of the Holly Grail", "blue"]
for q, a in zip(questions, answers):
    print("What is your {0}? It is {1}.".format(q, a))

# reversed
for i in reversed(xrange(0, 20, 2)):
    print(i)

# sorted
basket = ["banana", "orange", "pear", "apple", "strawberry", "cranberry", "kiwi"]
for item in sorted(basket):
    print(item)