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


for  combine in (obj1,obj2,obj3):
     combine(obj)




# class Cat:
#     def animal(self):
#        print('cat')


# class Dog:
#     def animal(self):
#         print('dog')

# def com