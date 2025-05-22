#For question 6

def func_b():
    print("Function B")

def call_func_a():
    from main import func_a # delaying import to avoid circular import
    func_a()
