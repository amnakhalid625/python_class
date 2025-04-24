# file read mode and write mode

file=open('file.txt','r')
# for read the data in file use the read function
# for write the data in the file use the write function
show=file.read()
# file.write('hello')
print(show)

# file must be closed when open the file
file.close()

# check if file is closed or not check using the file.closed its giv only two values ture or false
print(file.closed)

# file modes or file operations
# r read mode
# w write mode
# a append mode
# r+ read and write mode


