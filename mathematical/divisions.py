# know when to choose between "div-mod" (i.e. floor), "true" (i.e. floating point)
# and "fractional" divisions

total_seconds = 7385

print('='*15)
print('divmod')
print('='*15)
hours = total_seconds // 3600 # floor division
remaining_seconds = total_seconds % 3600 # modulo division
minutes = remaining_seconds // 60
remaining_seconds = remaining_seconds % 60

print('{} hours, {} minutes, {} seconds'.format(hours, minutes, remaining_seconds))

# alternatively, use the divmod function to get the same results

hours, remaining_seconds = divmod(total_seconds, 3600)
minutes, remaining_seconds = divmod(remaining_seconds, 60)

print('{} hours, {} minutes, {} seconds'.format(hours, minutes, remaining_seconds))

print('='*15)
print('true')
print('='*15)

hours = total_seconds / 3600
print('hours: {}'.format(round(hours, 4)))

print('='*15)
print('fractional')
print('='*15)
from fractions import Fraction
total_seconds = Fraction(7385)
hours = total_seconds / 3600
print('hours (fractional): {}'.format(hours))