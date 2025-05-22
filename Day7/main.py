#1. Create & import your own module

ms.add(4, 9)
ms.sub(77, 44)
ms.mul(5, 9)
ms.div(10, 2)

#2. Package basics with __init__.py

from geometry import area_circle, area_rectangle

print("Area of Circle:", area_circle(5))
print("Area of Rectangle:", area_rectangle(4, 6))


#4. Module‑level vs function‑level scope
my_list = [1, 2, 3]

def add_item(item):
    my_list.append(item)
    print(my_list)

add_item(4)
print(my_list)

my_number = 10

def change_wrong():
    my_number = 20
    print(my_number)

change_wrong()
print(my_number)

def change_correct():
    global my_number
    my_number = 30
    print(my_number)

change_correct()
print(my_number)

#5. nonlocal keyword practice
def outer():
    x = 5
    print("Before:", x)

    def inner():
        nonlocal x
        x = 10
        print("Inside inner:", x)

    inner()
    print("After:", x)

outer()

#6. Circular import pitfall

def func_a():
    print("Function A")

if __name__ == "__main__":
    print("\nRunning as main script!")

    from circular_demo import func_b, call_func_a
    func_b()
    call_func_a()

#7. Dynamic imports with importlib
import importlib

Q7 = importlib.import_module("greetings")
Q7.hi()

#8. Private vs public names
from question8 import *

public()

#helper() #Will not work, we have to update __all__ = ["public", "_helper"] in question8.py

#9. Reloading a module
import my_module
import importlib

my_module.greet()

importlib.reload(my_module) #Forcefull reimports the module without the need of closing the current running file for the updates in the imported module.

my_module.greet()
#10. Package‑wide state with Singleton pattern
import logger
import module

print(logger.status)
module.activate()
print(logger.status)


