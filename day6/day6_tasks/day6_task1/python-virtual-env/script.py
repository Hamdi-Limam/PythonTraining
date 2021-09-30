# This script uses env/ virtual environment to have its own dependencies, regardless of what dependencies every other project has. 
import bcrypt

print(bcrypt.hashpw('password'.encode('utf-8'), bcrypt.gensalt()))
