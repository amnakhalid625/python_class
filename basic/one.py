print('hello')

grade=int(input('enter you marks'))

if(grade>90):
    print('your grade is A')

elif(grade>70):
    print('your grade is B')

elif(grade>=4040):
    print('your grade is c')

else:
   print('you are fail')

# list

# pop is used for the remove the last element

# if we give the index in the pop method then remove the element in the list

name=['one','two','three']
name.pop(1)
print(name)

# for loop
things=['1','2', '3']
for show in  things:
    print(show)

names=['alid','ahmad','abduallag']
ages=[22,30,25]

for h in name:

  for s in name:
    print(f"the age of {names[h]} is {ages[s]}")

