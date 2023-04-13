#OOP modules concept

# !Extending module load path
PYTHONPATH=/foo python game.py

# !Sys.path, allows searching files fron another path (includes)
sys.path.append("/foo")





# ! Writing packages

# Each package in Python is a directory which MUST contain a special 
# file called __init__.py. This file, which can be empty, indicates 
# that the directory it's in is a Python package. That way it can be 
# imported the same way as a module.