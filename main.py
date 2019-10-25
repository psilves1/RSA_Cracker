from use_RSA_encryption import *
from make_primes import *

keys = RSA_Keys(getRandomPrime(1, 100), getRandomPrime(1,100))



print("Code: " + str(keys.encrypt(10)))

print("Message: " + str(keys.decrypt(keys.encrypt(10))))

print("\n")

print("Original Value: 10")

keys.printVals()
