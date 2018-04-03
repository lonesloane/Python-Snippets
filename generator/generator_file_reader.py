def read(filename):
    for line in open(filename):
        yield line


for entry in read('annotated_function.py'):
    print(entry)
