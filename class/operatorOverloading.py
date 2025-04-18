class OperatorOverloading:
    def __init__(self, a, b,):
        self.a = a
        self.b = b

    def __add__(self, other):
        
        return OperatorOverloading(self.a+other.a,self.b,other.b)

obj=OperatorOverloading(1,2)
obj1=OperatorOverloading(3,4)
print(obj+obj1) 


    



    
