def my_decorator(func):
    def wrapper():
        print('check before')
        func()
        print('check after')
    return wrapper

# say_hello = my_decorator(hello)
# say_hello()
@my_decorator
def hello():
    print('hello')
    return None
hello()
