from use_RSA_encryption import *
from make_primes import *

keys = RSA_Keys(getRandomPrime(1, 100), getRandomPrime(1,100))

print(keys.encrypt(10))

print(keys.decrypt(10))
