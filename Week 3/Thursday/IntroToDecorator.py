def x(fun):
    
    def y():
        print("Hello ")
        fun() #namee of the argument
        print(" Welcome to python")
    return y
def z():
    print("Code Academy")

f = x(z)
f()