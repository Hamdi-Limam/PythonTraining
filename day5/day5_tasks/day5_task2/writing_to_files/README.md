## Writing to files with Python
Now let’s dive into writing files. As with reading files, file objects have multiple methods that are useful for writing to a file:
* write(string):	This writes the string to the file.
* writelines(seq):	This writes the sequence to the file. No line endings are appended to each sequence item. It’s up to you to add the appropriate line ending(s).

To write to an existing file, you must add a parameter to the open() function:
* "a" - Append - will append to the end of the file
* "w" - Write - will overwrite any existing content

```
f = open("demofile2.txt", "a")
f.write(f"\nNow the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
f.close()
```
Here’s a quick example of using .write() and .writelines():
print(f
with open('dog_breeds.txt', 'r') as reader:
    # Note: readlines doesn't trim the line endings
    dog_breeds = reader.readlines()

with open('dog_breeds_reversed.txt', 'w') as writer:
    # Alternatively you could use
    # writer.writelines(reversed(dog_breeds))

    # Write the dog breeds to the file in reversed order
    for breed in reversed(dog_breeds):
        writer.write(breed)

### Working With Two Files at the Same Time
There are times when you may want to read a file and write to another file at the same time. If you use the example that was shown when you were learning how to write to a file, it can actually be combined into the following:
```
d_path = 'dog_breeds.txt'
d_r_path = 'dog_breeds_reversed.txt'
with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
    dog_breeds = reader.readlines()
    writer.writelines(reversed(dog_breeds))
```

### Creating file with Python
To create a new file in Python, use the open() method, with one of the following parameters:
* "x" - Create - will create a file, returns an error if the file exist
* "a" - Append - will create a file if the specified file does not exist
* "w" - Write - will create a file if the specified file does not exist

Example :Create a file called "myfile.txt":
```
f = open("myfile.txt", "x")
```
-> Result: a new empty file is created!

