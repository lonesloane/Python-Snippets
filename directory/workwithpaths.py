from pathlib import Path
from argparse import Namespace
import os

source_path = Path(os.path.expanduser('~/Documents'))

for source_path_file in source_path.glob('*.*'):  # glob uses regular expression to retrieve files matching the pattern
    source_file_details = source_path_file.relative_to(source_path)
    print(source_file_details)

print('='*15)

options = Namespace(
    input='/path/to/some/file.csv',
    file1='/Users/slott/Documents/Writing/PythonCookbook/code/ch08_r09.py',
    file2='/Users/slott/Documents/Writing/PythonCookbook/code/ch08_r10.py')

input_path = Path(options.input)
print("input path: {} - type: {}".format(input_path, type(input_path)))
output_path = input_path.with_suffix('.out')
print("output path: {} - type: {}".format(output_path, type(output_path)))

input_directory = input_path.parent
input_stem = input_path.stem

output_stem_pass = input_stem+"_pass"
output_path = (input_directory / output_stem_pass).with_suffix(".out")
print("output path: {} - type: {}".format(output_path, type(output_path)))
