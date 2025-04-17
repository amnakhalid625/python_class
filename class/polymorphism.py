class one:
    def programmer(self):
        print('one line')

class two:
    def programmer(self):
        print('two line')

class three:
    def programmer(self):
        print('three line')

def combine(obj):
    obj.programmer()


obj1=one()
obj2=two()
obj3=three()

for obj in (obj1,obj2,obj3):
    combine(obj)
    