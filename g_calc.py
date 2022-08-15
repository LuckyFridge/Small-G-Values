import random
import base64
import hashlib

g = 11
p = 1001

x = random.randint(5, 10)
y = random.randint(10, 20)

A = (g**x) % p
B = (g**y) % p

print('g: ',g,' (a shared value), n: ',p, ' (a prime number)')

print('\nAlice calculates:')
print('a (Alice random): ',x)
print('Alice value (A): ',A,' (g^a) mod p')

print('\nBob calculates:')
print('b (Bob random): ',y)
print('Bob value (B): ',B,' (g^b) mod p')

print('\nAlice calculates:')
keyA = (B**x) % p
print('Key: ',keyA,' (B^a) mod p')
print('Key: ',hashlib.sha256(str(keyA).encode('utf-8')).hexdigest())

print('\nBob calculates:')
keyB = (A**y) % p
print('Key: ',keyB,' (A^b) mod p')
print('Key: ',hashlib.sha256(str(keyB).encode('utf-8')).hexdigest())