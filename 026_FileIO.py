''' file input/output '''

# open a file for reading
f = open('myfile.txt', 'r')

# read the file
text = f.read()
print(text)

# close the file
f.close()

# open a file for writing
f = open('myfile.txt', 'w')

# write to the file
f.write('Hello, world!')

# close the file
f.close()

# open a file for appending
f = open('myfile.txt', 'a')
f.write('This is an appended line.')
f.close()

# open a file for reading and writing
f = open('myfile.txt', 'r+')
f.write('This is a line.')
f.close()

# open a file with 'with' statement
with open('myfile.txt', 'r') as f:
    text = f.read()
    print(text)
    
# open a file with 'with' statement
with open('myfile.txt', 'w') as f:
    f.write('Hello, world!')
    
# open a file with 'with' statement
with open('myfile.txt', 'a') as f:
    f.write('This is an appended line.')
    f.close()
    
# read, readline, readlines
with open('myfile.txt', 'r') as f:
    text = f.read()
    print(text)
    
with open('myfile.txt', 'r') as f:
    line = f.readline()
    print(line)
    
with open('myfile.txt', 'r') as f:
    lines = f.readlines()
    print(lines)
    
# write multiple lines
lines = ['Line 1\n', 'Line 2\n', 'Line 3\n']
with open('myfile.txt', 'w') as f:
    f.writelines(lines)
    f.close()
    
# seek, tell, truncate, flush
with open('myfile.txt', 'r+') as f:
    f.seek(5)
    print(f.tell())
    f.truncate(10)
    f.flush()
    f.close()
    
# binary files
with open('myfile.txt', 'rb') as f:
    data = f.read()
    print(data)
    
with open('myfile.txt', 'wb') as f:
    f.write(b'Hello, world!')
    f.close()
    
# file modes
'''
r: read
w: write
a: append
r+: read and write
w+: write and read
a+: append and read
b: binary
t: text
'''