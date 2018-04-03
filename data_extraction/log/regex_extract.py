from pathlib import Path
from pprint import pprint
import re
import csv


pattern_text = (r'\[(?P<date>\d+-\d+-\d+ \d+:\d+:\d+.\d+)\]'
                r'\s+(?P<level>\w+)'
                r'\s+in\s+(?P<module>[\w_ \.]+):'
                r'\s+(?P<message>.*)')
pattern = re.compile(pattern_text)


def log_parser(source_line):
    match = pattern.match(source_line)
    if match is None:
        raise ValueError(
            "Unexpected input {0!r}".format(source_line))
    return match.groupdict()


def read_log_file():
    data_path = Path('web.log')
    with data_path.open('r') as data_file:
        data_reader = map(log_parser, data_file)
        for row in data_reader:
            pprint(row)


def convert_to_csv():
    data_path = Path('web.log')
    target_path = data_path.with_suffix('.csv')
    with target_path.open('w', newline='') as target_file:
        writer = csv.DictWriter(
            target_file,
            ['date', 'level', 'module', 'message']
        )
        writer.writeheader()
        with data_path.open() as data_file:
            reader = map(log_parser, data_file)
            writer.writerows(reader)

convert_to_csv()