def my_func_args(*args):
    for arg in args:
        print(arg)

my_func_args(1, 2, 3)

def my_func_kwargs(**kwargs):
    name = kwargs.get("name", None)
    age = kwargs.get("age", None)
    print(f"My name is {name} and I am {age}")

    #for key, value in kwargs.items():
    #    print(f"{key} = {value}")

my_func_kwargs(name="John", age=30, location="USA")
