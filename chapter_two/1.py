def factorial(n):
    # this is a function 
    return  1 if n < 2 else n * factorial(n - 1)
print(factorial.__doc__)
# function that receive other function as augument or return functions as resault are called higher-older funcrtions 
# example :
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
sorted(fruits, key=len)
print(fruits)
# sorted() function will return a new list, however calss.sort() function will sort list in place 
# In the sorting function , keywork 'key' accept funciton name as value and applies this function 
# to each object in container to ues return value as basis for sorting  
class fruit:
    def __init__(self, _name, _weight ) -> None:
        self.name = _name
        self.weight = _weight
    def get_name(self):
        return self.name 
def cmp(A = fruit):
    return A.weight
apple = fruit('apple', 10)
cherry = fruit('chrry', 20)
banana = fruit('banana', 30)
fruits = [cherry, apple, banana]
for item in fruits:
    print(item.get_name())
new_fruits= sorted(fruits, key=cmp)
for item in new_fruits:
    print(item.get_name())

def blank_function():
    return None
function_set = set(x for x in dir(blank_function))
class blank_class:
    def __init__(self) -> None:
        pass
class_set = set(item for item in dir(blank_class))
blank_var = ()
var_set = set(item for item in dir(blank_var) )


print(function_set & class_set & var_set )

