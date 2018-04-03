with open('sample.txt') as file:
	content = file.readlines()
	content = [int(i.rstrip().split(' ')[1]) for i in content]
	for i in content:
		print(i)
