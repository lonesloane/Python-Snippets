class ProximityFinder:

    def __init__(self, hash_table_filename=None):
        self._hash_table_filename = hash_table_filename if hash_table_filename is not None else HASH_TABLE_FILENAME
        self._corpus_table = None

    @property
    def corpus_table(self):
        return self._corpus_table

    @corpus_table.setter
    def corpus_table_setter(self, val):
        self._corpus_table = val


class Temperature(object):
    def __init__(self):
        self.cTemp = None

    def f_get(self):
        return self.celsius * 9 / 5 + 32

    def f_set(self, value):
        self.celsius = (float(value)-32)*5/9

    farenheit = property(f_get, f_set)

    def c_set(self, value):
        self.cTemp = float(value)

    def c_get(self):
        return self.cTemp

    celsius = property(c_get, c_set, doc="Celsius temperature")

if __name__ == "__main__":
    temp = Temperature()
    temp.celsius = 30
    print temp.farenheit
