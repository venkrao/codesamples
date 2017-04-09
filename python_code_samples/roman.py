roman = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40:"XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
roman_ints_set = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)

def print_roman(x):
   for ir in roman_ints_set:
       if ir > x:
          continue
       howmany = x/ir
       remainder = x%ir

       if remainder == 0:
          return "%s" %roman[ir]*howmany

       elif remainder < 4:
          return "%s%s" %(roman[ir]*howmany, roman[1]*remainder)
       else:
          return "%s%s" %(roman[ir]*howmany, print_roman(remainder))

num = raw_input("Enter a number to get it's roman equivalant:")

if num:
  print print_roman(int(num))
