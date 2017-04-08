#!/usr/bin/env python

# Problem: https://web.archive.org/web/20130502115734/http://www.streamtech.nl/problemset/100.html

def cycles(n, counter):
   if n == 1:
      counter += 1
      return counter
   elif n % 2 != 0:
      n = 3*n + 1
      counter += 1
      return cycles(n, counter)
   else:
      n = n / 2
      counter += 1
      return cycles(n, counter)


print "Read https://web.archive.org/web/20130502115734/http://www.streamtech.nl/problemset/100.html"
pairs = list()
while True:
  pair = raw_input()
  if pair == '':
     break
  pairs.append(pair.split(" "))

for pair in pairs:
   max = 0

   for i in range(int(pair[0]), int(pair[1]) + 1, 1):
      cycle_count = cycles(i, 0)
      if max < cycle_count:
         max = cycle_count

   print "%s %s %s" %(pair[0], pair[1], max)

