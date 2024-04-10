import array
from collections import deque
import random
# 创建一个数组
numbers = array.array('h', [1, 3, -1 , 3, 5])
print(len(numbers), numbers)

menv = memoryview(numbers)
menv_oct = menv.cast('B')
print('the length is :%d' %len(menv_oct))
menv_oct.tolist()
[print('%x'%x, end="") for x in menv_oct]
print()
menv_oct[5] = 4
print('the length is :%d   ' %len(numbers), numbers)

#my_deque = deque(range(10), maxlen = 10)
#print(my_deque)
#my_deque.rotate(4)
#print(my_deque)
#my_deque.rotate(-5)
#print(my_deque)
#my_deque.appendleft(100)
#print(my_deque)
#my_deque.extend([10, 20, 30])
#print("after extend the value is:%r" %my_deque)


#list conprehension generate list objection ,while generator expression return a genetator objection 
my_list1 = (random.randint(1, 10) for _ in range(10))
my_list2 = my_list1
[print('%d  '%item, end= "") for item in my_list1]
print()
def delAndmodify(generator):
    for item in generator:
        if item >= 5:
            yield item ** 2

[print('%d  '%item, end= "") for item in my_list2]
#my_list2 = [random.randint(1, 100) for _ in range(10)]
#print(type(my_list2), my_list2)
