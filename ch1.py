#!/usr/bin/env python3

from fractions import Fraction
f = Fraction(22, 7)
print(f + 2) # 36/7

# irrational numbers
a = 2+3j
b = 3+3j
print(a-b) 
print(a+b)
print(a.real)
print(a.imag)

print("Magnitude of a")
print((a.real ** 2 + a.imag ** 2) ** 0.5)
print(abs(a))

print('1')
print(int(1))
print(float(1))


print(float(22/7))  # 3.0 except in P3
print(float(22/7.0))# 3.14285714286
print(float(22.0/7))# 3.14285714286

a = input()
print(a)

print("Input a number:")
print(range(int(a)))
for i in range(int(a)):
  print(i)

print ("------")
for i in range(0,100,5):
  print(i)

print('{0:.04f}'.format(3.14159) )
print('{0:.04f}'.format(3) )
