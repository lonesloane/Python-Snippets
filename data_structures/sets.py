# a set contains elements without precise position
valid_inputs = {'yes', 'y', 'no', 'n'}

answer = None

while answer not in valid_inputs:
    answer = input('Continue? [yes/no] ').lower()

print(valid_inputs)

valid_inputs.add('yes')
print(valid_inputs)

valid_inputs.add('dunno')
print(valid_inputs)