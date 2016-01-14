__author__ = 'stephane'

import math

class MathTest(object):
    def __init__(self):
        pass

    @staticmethod
    def simplefunctions():
        print'\n**********************'
        print "simple math functions:"
        print'**********************'
        signal_power = 235
        noise_power = 0.23
        ratio = signal_power / noise_power
        decibels = 10 * math.log10(ratio)
        print "decibels:%f" % decibels

        radians = 0.7
        height = math.sin(radians)
        print "sinus de %f (radians) = %f" % (radians, height)

        degrees = 45
        radians = degrees / 360.0 * 2 * math.pi
        height = math.sin(radians)
        print "sinus de %f (degrees) = %f" % (degrees, height)

def main():
    mathtest = MathTest()
    mathtest.simplefunctions()

if __name__ == '__main__':
    main()