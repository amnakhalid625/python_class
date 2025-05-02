# what is set
# function is set of code usd to perform the specific task

# def student():
#     print('this is form')


# student()

# set
# sdudent={22,33,55,66,4,4,3}

# print(sdudent)

# student =set([22,4,3,2,2,2])
# added=student.add(44)
# removed=student.remove(4)




# student.discard(4)
# print(student)



a=[1,2]
print(a*3)

example=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
del example[2]
print(example)


check=[1,2,2,3,4,4]
if 4 in check:
    print('found')

numbers=(4,7,8,9,0,6,4,3,2,1)
sorted_numbers=sorted(numbers)
print(sorted_numbers)

def thirve(n):
    if n % 15==0:
        print('thirve',end='')
    elif n% 3 !=0 and n%5!=0:
        print(n,end='')
    elif n%3==0:
        print('thrive',end='')
    elif n%5==0:
        print('thrive',end='')
    thirve(35)
    thirve(56)
    thirve(15)
    thirve(39)


num=(4,2,5,6,7,8,9,56)
sorted_num=sorted(num)
even=lambda a:a%2==0
even_numbers=filter(even,sorted_num)
print(type(even_numbers))


