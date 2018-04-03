import datetime
import os

files = os.listdir('')
files = [file for file in files if file.startswith('file') and file.endswith('.txt')]

now = datetime.datetime.now()
output_file = now.strftime('%Y-%m-%d-%H-%M-%f') + '.txt'
with open(output_file, 'w') as o_file:
    for input_file in files:
        with open(input_file, 'r') as i_file:
            o_file.write(i_file.read() + '\n')
