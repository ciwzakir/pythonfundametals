def test1(func):
    def nestedfunc():
        print("First line of nested func")
        func() # test1 func
        print("Third line of nested func")
    return nestedfunc

@test1 #decorator
def my_func():
    print("Please see the it very carefully.")

# my_func = test1(my_func)
my_func() #call the function