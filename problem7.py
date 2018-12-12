"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

def isPrime(num):
  limit = num // 2
  flag = True
  for i in range(2, limit+1):
    if num % i == 0:
      flag = False
      break
  return flag

primes = [] #List to store primes
i = 2

index = int(input("Enter the index for the required prime number: "))

while(len(primes)<index):
  if isPrime(i):
    primes.append(i)
  i += 1

print("The {}th primes is {}".format(index,primes[len(primes)-1]))
