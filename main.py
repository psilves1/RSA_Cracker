from use_RSA_encryption import *
from make_primes import *

keys = RSA_Keys(getRandomPrime(1, 1000), getRandomPrime(1,1000))

print("Code: " + str(keys.encrypt(10)))

print("Message: " + str(keys.decrypt(10)))

print("\n")

keys.printVals()
