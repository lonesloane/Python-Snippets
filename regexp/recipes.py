import re

recipee = "Kumquat: 2 cups"

# use raw string to tell python not to interpret the \
# use named groups to easily manipulate in the match results
pattern_text = r'(?P<ingredient>\w+):\s+(?P<amount>\d+)\s+(?P<unit>\w+)'

pattern = re.compile(pattern_text)

match = pattern.match(recipee)

print(match.groups())

# extract individual group from match results

print('ingredient: {}'.format(match.group('ingredient')))
print('quantity: {}'.format(match.group('amount')))
print('unit: {}'.format(match.group('unit')))

ingredient_pattern = re.compile(
    r'(?P<ingredient>\w+):\s+' # name of the ingredient up to the ":"
    r'(?P<amount>\d+)\s+' # amount, all digits up to a space
    r'(?P<unit>\w+)' # units, alphanumeric characters
)