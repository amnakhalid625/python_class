class one:
    def coder(self):
        print('one')


class two:
    def coder(self):
        print('two')

class three:
    def coder(self):
        print('one')

def combine(obj):
     obj.coder()


obj1=one()
obj2=two()
obj3=three()

print(obj1,obj2,obj3)