from collections import namedtuple
import random
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
#for tshirt in ('%s%s'%(c, s) for c in colors for s in sizes):
#   print(type(tshirt), tshirt)
City = namedtuple('City', 'name country population coordinates')



Beijin = City('bejin', 'China', 14, (14, 42))
#print(Beijin)

#print(City._fields)

# 切片
number = [x for x in range(10)]
second_number = number[6:10]
print(second_number)

#sorted function will return inorder array, and don't change older list 
#list.sort() will return none and sorted older list 
random_number = [random.randint(1, 100) for _ in range(20)]
print(f'random number is :{random_number}')
print(sorted(random_number), random_number)
print(random_number.sort(), random_number)