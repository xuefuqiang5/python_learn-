import bisect
import random
import array
def grade(score, break_point = [60, 70, 80, 90], grades = "FDCBA"):
    position = bisect.bisect(break_point, score)
    return grades[position]
# Can be sorted by alphabetically 
fruits = ['grape','raspberry', 'apple', 'banana']
print(sorted(fruits))
# sorted by word length
print(sorted(fruits, key = len , reverse = True))

#Genarate ten random fraction 
scores = [random.randint(1, 100) for _ in range(10)]
print(f'the scores is :{scores}')



grades = [grade(score) for score in scores]
print(f"the grades is :{grades}")

#bisect.insort 
SIZE = 7 
my_list = []
for i in range(SIZE):
    my_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, my_item)
    #print('%2d --> '%my_item, my_list)
number1 = 10 
number2 = 20
#print('the first number is :%2d the second number is: %2d'%(number1,number2))

floats = array.array('d', (random.random() for _ in range(10 ** 7 )))
last_float = floats[-1]
print(last_float)



