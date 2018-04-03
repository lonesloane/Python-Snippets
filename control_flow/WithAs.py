def with_as():
    with open("test.txt", "w") as wf:
        wf.write("La nature est un temple")
    with open("test.txt", "r") as rf:
        print(rf.read())
