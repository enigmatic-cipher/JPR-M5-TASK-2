"""
Given a number n as input, print al primes from 1 to n.
Input-> 10
Output-> 2,3,5,7
"""

def prime_num(n):
    for i in range(1,n+1):
      if i > 1:
        for j in range(2,i):
          if (i%j)==0:
            break
        else:
          print(i)
      
num = 10
prime_num(num)
