class student:
    def study(self):
        print("studying")

class classroom:
    def __init__(self):
        self.ali=student()
        print('we are going to study')


obj=classroom()
obj.ali.study()




# in compositon one property use the 