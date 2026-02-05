# can be created via DUNDER method (__init__(self), that is a rule)
'''
Docstring for DSA.45_constructor
a constructor is automaticlally called when a object is created of a class.
the main purpose of the constructor is to initialize or assign values to the data members of the class.
A constructor does not return anything other than none
'''

class TEST:
    name = "mayank"
    role = "developer"
    print("hey i am a person")

    def info(self):
        print(f"{self.name} is a {self.role}")

a = TEST()
b = TEST()      # as class is creted and run once so only once print statement is printed does not work like exceptionally printing like functions
print(a.name)
a.name = "MAYANK"
a.role = "SDE"
a.info()

###########
###################

class illustration:     # parametrized constructor
    def __init__(self, n, o): # DUNDER METHOD
        print("hey i am here")
        self.name = n   # attriutes to the objects in the code
        self.occ = o
    def info(self):
        print(f"{self.name} is a {self.occ}")

a = illustration("Mayank", "SDE") # passing the arguments to __init__(self,n,o), self is automatic passable, object itself pass it.
b = illustration("Kamal", "Manager")
# c = illustration(1,2,3) type error as there are 4 arguments and defined are 3 i.e, self,n,o, slef itslef has its own value no overlap 
#c = illustration() typerror no argument passed
# self pased automatically
a.info()
b.info()



'''
types of constructors:
1. parametrized: when the constructor accepts arguments along with self
2. default constructor: when the constructoir does not take any argument just take self argument
'''