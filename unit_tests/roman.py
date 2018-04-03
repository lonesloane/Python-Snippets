__author__ = 'stephane'

# Define exceptions
class RomanError(Exception):pass
class OutOfRangeError(RomanError):pass
class NotIntegerError(RomanError):pass
class InvalidRomanNumeralError(RomanError):pass

def toRoman(n):
    """convert integer to roman numeral"""
    pass

def fromRoman(s):
    """convert roman numeral to integer"""
    pass