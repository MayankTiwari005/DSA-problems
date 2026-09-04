"""from pydantic import BaseModel

class Message(BaseModel):
    sender: str
    receiver: str      # receiver's username/id
    department_id: str
    message: str
######
"""

def sum_print(func):    
    def inner(a,b):
        print(str(a), "+", str(b), "is: ", end="")
        func(a,b)
    return inner

@sum_print
def sum_(a,b):      # sum_ = sum_print(sum_)
    added = a+b
    print(added)

if __name__ == "__main__":
    sum_(5,3)


import time
def set_t(func):
    def inner(*arg):
        t= time.time()
        res = func(*arg)
        print("Function took " + str(time.time()-t) + " seconds to run")
        return res
    return inner

@set_t
def myFunction(n):
    time.sleep(n)

if __name__ == "__main__":
    myFunction(2)