#class creation
class myClass:

    #private variable
    __privateVar=27;

    #private method
    def __privMeth(self):
        ("I'm inside class myClass")

#function to print the private variable
    def hello(self):
        print("Private variable value:",myClass.__privateVar)

#object creation and method call
foo=myClass()
foo.hello()
foo.__privMeth

    