# use named space to avoid referencing list elements by index
# which can be confusing (what does row[4] stand for?)
from types import SimpleNamespace

row = ['elem 1', 'elem 2', 'elem 3', 'elem 4', 'elem 5']

named_space = SimpleNamespace(
    x = row[0],
    y = row[1],
    z = row[2],
    abs = row[3],
    ord = row[4]
)

print("named_space.x: {}".format(named_space.x))
print("named_space.abs: {}".format(named_space.abs))
print("named_space.ord: {}".format(named_space.ord))