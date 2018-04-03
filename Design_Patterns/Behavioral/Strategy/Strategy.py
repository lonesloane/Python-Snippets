class PrimeFinder:

    def __init__(self):
        self.primes = []

    def calculate(self, limit):
        """ Will calculate all primes below limit """
        pass

    def out(self):
        """ Prints the list of primes prefixed with the algorithm used """
        print(self.__class__.__name__)
        for prime in self.primes:
            print(prime)


class HardcodedPrimeFinder(PrimeFinder):
    def calculate(self, limit):
        harcoded_primes = [2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        for prime in harcoded_primes:
            if prime < limit:
                self.primes.append(prime)


class StandardPrimeFinder(PrimeFinder):
    def calculate(self, limit):
        self.primes = [2]
        # check only odd numbers
        for number in range(3, limit, 2):
            is_prime = True
            for prime in self.primes:
                if number % prime == 0:
                    is_prime = False
                    break
            if is_prime:
                self.primes.append(number)


class PrimeFinderClient:

    def __init__(self, limit):
        self.limit = limit

        if limit <= 50:
            self.prime_finder = HardcodedPrimeFinder()
        else:
            self.prime_finder = StandardPrimeFinder()

    def get_primes(self):
        self.prime_finder.calculate(self.limit)
        self.prime_finder.out()


# === usage ===
pfc = PrimeFinderClient(45)
pfc.get_primes()

pfc = PrimeFinderClient(60)
pfc.get_primes()
