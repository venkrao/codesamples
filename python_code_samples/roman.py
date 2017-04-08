roman = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
roman_ints_set = (1000, 500, 100, 50, 10, 5, 1)

def print_roman(x):
   for ir in roman_ints_set:
       if ir > x:
          continue
       howmany = x/ir
       remainder = x%ir

       if remainder == 0:
          return "%s" %roman[ir]*howmany

       elif remainder < 5:
          return "%s%s" %(roman[ir]*howmany, roman[1]*remainder)
       else:
          return "%s%s" %(roman[ir]*howmany, print_roman(remainder))

num = raw_input("Enter a number to get it's roman equivalant:")

if num:
  print print_roman(int(num))
