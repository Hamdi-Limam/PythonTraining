import os
path = os.path.join(os.getcwd(), "day5")

# Traversing file system with os.walk
for (dirpath,dirnames,filenames) in os.walk(path):
    print (dirpath)
    print (dirnames)
    print (filenames)
    print ('--------------------------------')

# Getting user’s environmental variables with os.environ
# Get all list of env var
print(os.environ)

# Get a specific env var
print(os.environ.get('HOME'))

os.path.exists()