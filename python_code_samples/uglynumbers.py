#!/usr/bin/env python

# https://web.archive.org/web/20130218171127/http://www.streamtech.nl/problemset/136.html
prime_factors = [1, 2, 3, 5]

def get_prime(n):
  for i in range(1, n/2 + 1, 1):
     if n % i == 0 and i not in prime_factors: 
        return

  return n

ugly_numbers = list()

start = 1
while len(ugly_numbers) < 1500:
   ugly = get_prime(start)
   if ugly:
      ugly_numbers.append(ugly)
   start += 1 


print "1500th ugly prime: %d" %ugly_numbers[1499]
