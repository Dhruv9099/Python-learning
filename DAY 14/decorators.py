def hello():
    print("Hello world!")
hello() # Call the function



def greet(fx):
    def mfx(*args, **kwargs):
        print("Good morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
        print( "    -------    ")
    return mfx
print( "    -------    ")

@greet
def hello():
    print("hello world")
# greet (hello()) # without using @greet , it will work fine. But with @g
hello()


@greet
def add(a,b):
    print(a+b)
# Call the function with two arguments
add(1,2) 
