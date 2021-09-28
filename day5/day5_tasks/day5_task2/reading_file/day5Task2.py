# Opening demofile
print("The read() method returns the whole text:")
f = open("demofile.txt", "r")
print(f.read())
print("Type of the file object is: ", type(f))
f.close()

print("Return the 5 first characters of the file:")
f = open("demofile.txt", "r")
print(f.read(5))
print(f.read(5))
f.close()

print("Read one line of the file:")
f = open("demofile.txt", "r")
print(f.readline())
f.close()

print("Read at most size number of characters from the line:")
f = open("demofile.txt", "r")
print(f.readline(5))
print(f.readline(5))
f.close()

print("This reads the remaining lines from the file object and returns them as a list:")
f = open("demofile.txt", "r")
print(f.readlines())
f.close()

print("Reading the file line by line:")
file = open("demofile.txt", "r")
for lines in file:
  print(lines)
f.close()

print("Python’s “with open(…) as …” Pattern:")
with open('demofile.txt', 'r') as f:
    print(f.read())

print("Buffered binary file:")
f = open('demofile.txt', 'rb')
print(f.read())
print("Type of the file object is: ", type(f))