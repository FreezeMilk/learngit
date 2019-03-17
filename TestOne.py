#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# for practise
sum = 0
for x in [1,2,3,4,5,6,7,8,9,10]:
    sum += x
print('The sum is: %d' %sum)

he = 0
for x in range(101):
    he += x
print('The sum is: %d' %he)

# while practise
sum = 0
n = 1
while n <= 100:
    if n > 10:
        break
    sum += n
    n += 1
print('Calculation End.')
print('The sum is %d' %sum)

sum = 0
n = 0
while n < 9:
    n += 1
    if n % 2 == 0:
        continue
    print(n)
    sum += n
print('The sum is %d' %sum)

# Dictionary practise
d = {'Michael':95,'Bob':75,'Trancy':85}
print(d['Michael'])
d['Kangkang'] = 10
kmean = int(d['Kangkang'])
print(kmean+12)
print('Jack' in d)      # use 'in' to judge whether 'Jack' is in d
n = d.get('Bobb', -1)   # use 'get' to judge whether 'Bobb' is in d
print(n)
k = {123:'JoJo',456:'Zhou'}
print(k.get(123,123))

# SET practise
s = set([1,1,2,3,3,3])
print(s)
s.add(4)                # 'add' is used to add one element into a set
print(s)
s.add((4,5))            # list is unable; tuple is able
print(s)
s.remove(2)
print(s)
s1 = set([1,2,3,4])
s2 = set([2,3,4,5])
print(s1 & s2)
print(s1 | s2)







