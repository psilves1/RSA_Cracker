import random
from math import *

class RSA_Keys:

    def __init__(self, p, q):

        self.p = p
        self.q = q

        self.n = p * q
        self.m = (p-1) * (q-1)
        
        self.e = random.randint(2, self.n)

        self.d = euclid(self.e, self.m, 1, 1)

    def printVals(self):
        print("P: " + str(self.p))
        print("Q: " + str(self.q))
        print("E: " + str(self.e))
        print("D: " + str(self.d))
        
    def encrypt(self,message): #just for a number right now
        return (pow(message,self.e))%self.n #returns code

    def decrypt(self, code):
        return (pow(code, self.d))%self.n #returns message


def euclid(a, b, x, y): 
    # Base Case 
    if a == 0 :  
        x = 0
        y = 1
        return b 
          
    x1 = 1
    y1 = 1 
    gcd = euclid(b%a, a, x1, y1) 
   
    x = y1 - (b/a) * x1 
    y = x1 
  
    return gcd 
