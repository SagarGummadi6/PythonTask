#For question 6

def func_b():
    print("Function B")

def call_func_a():
    from geometry.venv.main6 import func_a # delayed import to avoid circular import
    func_a()
