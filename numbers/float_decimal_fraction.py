# for currency, always use decimal

from decimal import Decimal

print()
print('='*15)
print('Decimal calculations')
print('='*15)

tax_rate_1 = 7.25/100
print('tax rate (float): {}'.format(tax_rate_1))
print('-'*15)
tax_rate_2 = Decimal('7.25')/Decimal(100)
print('tax rate (decimal): {}'.format(tax_rate_2))
print('-'*15)

purchase_amount_1 = 2.95
purchase_amount_2 = Decimal('2.95')

result_1 = purchase_amount_1 + tax_rate_1 * purchase_amount_1
result_2 = purchase_amount_2 + tax_rate_2 * purchase_amount_2

penny = Decimal('0.01')

print('result (float): {}'.format(result_1))
print('-'*15)
print('result (decimal): {}'.format(result_2))
print('-'*15)

print('rounded result (float): {}'.format(round(result_1, 2)))
print('-'*15)
result_2 = result_2.quantize(penny)
print('rounded result (decimal): {}'.format(result_2))
print('-'*15)

# Use the fraction module when fractional results needed

from fractions import Fraction

print()
print('='*15)
print('Fraction calculations')
print('='*15)
sugar_cups = Fraction('2.5')
scale_factor = Fraction(5/8)
required_cups = scale_factor * sugar_cups
print('required_cups (fraction): {}'.format(required_cups))

# Floating point calculation invovle some rounding approximations!!!
# Be aware of this and always avoid comparison of floats!!!

print()
print('='*15)
print('Floating point number calculations')
print('='*15)
print('result should be 1: (19/155)*(155/19): {}'.format((19/155)*(155/19)))
result = (19/155)*(155/19)
print('rounded to 3rd decimal place: {}'.format(round(result, 3)))
print('floating point number approximation: {}'.format(1-result))