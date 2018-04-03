
def decorate(func):
    def wrapper():
        print('do something before')
        func()  # the original function is still called, but embedded inside the "wrapper"
        print('do something after')
    return wrapper


def original_timer():
    print('This is from the original function')


# Possible when you have access to the code and are willing to decorate it
@decorate
def original_function():
    print('This is from another original function')


original_function()
# Best when you need to add functionality to existing code without modifying it
decorated = decorate(original_timer)
decorated()
