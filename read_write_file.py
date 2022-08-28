"""
open() returns a file object, and is most commonly used with two positional arguments and one keyword argument: open(filename, mode, encoding=None)
"""
f = open('workfile.txt', 'w', encoding="utf-8")

file = open("hello.txt", "w") # open in write mode 'w'
file.write("Hello World") 