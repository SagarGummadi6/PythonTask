#For question 1 and 3
def add(x,y):
    print("Add: ", x+y)
def sub(x,y):
    print("Subtract: ", x-y)
def mul(x,y):
    print("Multiply: ", x*y)
def div(x,y):
    if y==0:
        print("Denominator cannot be zero.")
    else:
        print("Divide: ", x/y)
#For question 3
import sys

if __name__ == "__main__":
    # Get command-line arguments
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    op = sys.argv[3]

    if op == "add":
        add(x, y)
    elif op == "sub":
        sub(x, y)
    elif op == "mul":
        mul(x, y)
    elif op == "div":
        div(x, y)
    else:
        print("Invalid operation. Use: add, sub, mul, div")