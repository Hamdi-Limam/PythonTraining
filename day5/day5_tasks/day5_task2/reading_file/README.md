## Reading files in Python

### What Is a File?
Before we can go into how to work with files in Python, it’s important to understand what exactly a file is and how modern operating systems handle some of their aspects.

At its core, a file is a contiguous set of bytes used to store data. This data is organized in a specific format and can be anything as simple as a text file or as complicated as a program executable. In the end, these byte files are then translated into binary 1 and 0 for easier processing by the computer.

Files on most modern file systems are composed of three main parts:
* Header: metadata about the contents of the file (file name, size, type, and so on)
* Data: contents of the file as written by the creator or editor
* End of file (EOF): special character that indicates the end of the file

What this data represents depends on the format specification used, which is typically represented by an extension. For example, a file that has an extension of .gif most likely conforms to the `Graphics Interchange Format` specification. There are hundreds, if not thousands, of file extensions out there. For this task, we’ll only deal with `.txt` or `.csv` file extensions.

### File Paths
When you access a file on an operating system, a file path is required. The file path is a string that represents the location of a file. It’s broken up into three major parts:
1. Folder Path: the file folder location on the file system where subsequent folders are separated by a forward slash / (Unix) or backslash \ (Windows)
2. File Name: the actual name of the file
3. Extension: the end of the file path pre-pended with a period (.) used to indicate the file type

Here’s a quick example. Let’s say you have a file located within a file structure like this:
```
/
│
├── path/
|   │
│   ├── to/
│   │   └── cats.gif
│   │
│   └── dog_breeds.txt
|
└── animals.csv
```

Let’s say you wanted to access the cats.gif file, and your current location was in the same folder as path. In order to access the file, you need to go through the path folder and then the to folder, finally arriving at the cats.gif file. The Folder Path is `path/to/.` The File Name is `cats`. The File Extension is `.gif`. So the full path is `path/to/cats.gif`.

Now let’s say that your current location or current working directory (cwd) is in the to folder of our example folder structure. Instead of referring to the cats.gif by the full path of path/to/cats.gif, the file can be simply referenced by the file name and extension `cats.gif`.

But what about `dog_breeds.txt`? How would you access that without using the full path? You can use the **special characters double-dot (..)** to move one directory up. This means that `../dog_breeds.txt` will reference the dog_breeds.txt file from the directory of to.

### Line Endings
One problem often encountered when working with file data is the representation of a new line or line ending. The line ending has its roots from back in the Morse Code era, when a specific pro-sign was used to communicate the end of a transmission or the end of a line.

Later, this was standardized for teleprinters by both the International Organization for Standardization (ISO) and the American Standards Association (ASA). ASA standard states that line endings should use the sequence of the Carriage Return **(CR or \r) and the Line Feed (LF or \n) characters (CR+LF or \r\n)**. The ISO standard however allowed for either the CR+LF characters or just the LF character.

Windows uses the `CR+LF characters` to indicate a new line, while Unix and the newer Mac versions use just the `LF character`. This can cause some complications when you’re processing files on an operating system that is different than the file’s source. Here’s a quick example. Let’s say that we examine the file dog_breeds.txt that was created on a Windows system:
```
Pug\r\n
Jack Russell Terrier\r\n
English Springer Spaniel\r\n
German Shepherd\r\n
Staffordshire Bull Terrier\r\n
Cavalier King Charles Spaniel\r\n
Golden Retriever\r\n
West Highland White Terrier\r\n
Boxer\r\n
Border Terrier\r\n
```
This same output will be interpreted on a Unix device differently:
```
Pug\r
\n
Jack Russell Terrier\r
\n
English Springer Spaniel\r
\n
German Shepherd\r
\n
Staffordshire Bull Terrier\r
\n
Cavalier King Charles Spaniel\r
\n
Golden Retriever\r
\n
West Highland White Terrier\r
\n
Boxer\r
\n
Border Terrier\r
\n
```
This can make iterating over each line problematic, and you may need to account for situations like this.

### Character Encodings
Another common problem that you may face is the encoding of the byte data. An encoding is a translation from byte data to human readable characters. This is typically done by assigning a numerical value to represent a character. The two most common encodings are the ASCII and UNICODE Formats. ASCII can only store 128 characters, while Unicode can contain up to 1,114,112 characters.

ASCII is actually a subset of Unicode (UTF-8), meaning that ASCII and Unicode share the same numerical to character values. It’s important to note that parsing a file with the incorrect character encoding can lead to failures or misrepresentation of the character. For example, if a file was created using the UTF-8 encoding, and you try to parse it using the ASCII encoding, if there is a character that is outside of those 128 values, then an error will be thrown.

### Open file in Python
When you want to work with a file, the first thing to do is to open it. This is done by invoking the open() built-in function. open() has a single required argument that is the path to the file. `open()` has a single return, the file object, which has a `read()` method for reading the content of the file:
```
f = open("demofile.txt", "r")
print(f.read())
```

#### Read Only Parts of the File
By default the read() method returns the whole text, but you can also specify how many characters you want to return:
```
# Return the 5 first characters of the file:
f = open("demofile.txt", "r")
print(f.read(5))
```

#### Read Lines
You can return one line by using the readline() method:
```
# Read one line of the file:
f = open("demofile.txt", "r")
print(f.readline())
```
By calling readline() two times, you can read the two first lines.
By looping through the lines of the file, you can read the whole file, line by line:
```
f = open("demofile.txt", "r")
for x in f:
  print(x)
```

readlines(): This reads the remaining lines from the file object and returns them as a list.
```
f = open("demofile.txt", "r")
print(f.readlines()) -> list of lines
f.close()
```

### Close Files
After you open a file, You should always make sure that an open file is properly closed. 

It’s important to remember that it’s your responsibility to close the file. In most cases, upon termination of an application or script, a file will be closed eventually. However, there is no guarantee when exactly that will happen. This can **lead to unwanted behavior including resource leaks**. It’s also a best practice within Python to make sure that your code behaves in a way that is well defined and reduces any unwanted behavior.

When you’re manipulating a file, there are two ways that you can use to ensure that a file is closed properly, even when encountering an error. The first way to close a file is to use the [try-finally block](https://realpython.com/python-exceptions/):
```
reader = open('dog_breeds.txt')
try:
    # Further file processing goes here
finally:
    reader.close()
```

The second way to close a file is to use the **with statement**.

#### Python’s “with open(…) as …” Pattern
Reading  a from files using Python is pretty straightforward. To do this, you must first open files in the appropriate mode. Here’s an example of how to use Python’s “with open(…) as …” pattern to open a text file and read its contents:
```
with open('data.txt', 'w') as f:
    data = 'some data to be written to the file'
    f.write(data)
```

The with statement **automatically takes care of closing the file once it leaves the with block, even in cases of error**. It is highly recommended that you use the with statement as much as possible, as it allows for cleaner code and makes handling any unexpected errors easier for you.

### File modes
 Mode argument is a string that contains multiple characters to represent how you want to open the file. The default and most common is 'r', which represents opening the file in read-only mode as a text file.
Other options for modes are [fully documented online](https://docs.python.org/3/library/functions.html#open), but the most commonly used ones are the following:
* 'r'	Open for reading (default)
* 'w'	Open for writing, truncating (overwriting) the file first
* 'rb' or 'wb'	Open in binary mode (read/write using byte data)
* 'a'   Append - Opens a file for appending, creates the file if it does not exist
* 'x'   Create - Creates the specified file, returns an error if the file exists
### File objects
There are three different categories of file objects:
1. Text files
2. Buffered binary files
3. Raw binary files
Each of these file types are defined in the io module. Here’s a quick rundown of how everything lines up.

#### Text File Types
A text file is the most common file that you’ll encounter. Here are some examples of how these files are opened:
```
open('abc.txt')
open('abc.txt', 'r')
open('abc.txt', 'w')
```
With these types of files, open() will return a `TextIOWrapper` file object.

#### Buffered Binary File Types
A buffered binary file type is used for reading and writing binary files. Here are some examples of how these files are opened. With these types of files, open() will return either a BufferedReader or BufferedWriter file object:
```
open('abc.txt', 'rb')
```

#### Raw File Types
A raw file type is generally used as a low-level building-block for binary and text streams.
It is therefore not typically used. Here’s an example of how these files are opened. With these types of files, open() will return a FileIO file object:
```
open('abc.txt', 'rb', buffering=0)
```

