# Using append mode
f = open("demofile.txt", "a")
f.write(f"\nNow the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())
f.close()

# Using write mode
f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the writing:
f = open("demofile.txt", "r")
print(f.read())
f.close()

with open('dog_breeds.txt', 'r') as reader:
    # Note: readlines doesn't trim the line endings
    dog_breeds = reader.readlines()
    print(dog_breeds)

with open('dog_breeds_reversed.txt', 'w') as writer:
    # Alternatively you could use
    # writer.writelines(reversed(dog_breeds))

    # Write the dog breeds to the file in reversed order
    for breed in reversed(dog_breeds):
        writer.write(breed)

Print("Working with two files at the same time:")
d_path = 'dog_breeds.txt'
d_r_path = 'dog_breeds_reversed.txt'
with open(d_path, 'r') as reader, open(d_r_path, 'w') as writer:
    dog_breeds = reader.readlines()
    writer.writelines(reversed(dog_breeds))