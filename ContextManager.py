from threading import Lock
from contextlib import contextmanager


__author__ = "Ejie Emmanuel Ebuka"

# Context Managers

"""
Context Managers are great tools for resources management that allow you to allocate resources the way you want them
with open statement.
"""

# This is a recommended way to open a file
with open("contxtMg/notes.txt", "w") as f:
    f.write("#!/usr/bin/env")

# We can use Lock
lock = Lock()
with lock:
    file = open("contxtMg/note2.txt", "w")
    file.write("Python is great")
    print("Writing note")

# Context Managers in class: __enter__ method and __exit__ method must be called
class ManageFile:
    def __init__(self, filename):
        print("Initializing ManageFile")
        self.filename = filename
    
    def __enter__(self):
        # Allocate our resource
        print("In enter method")
        self.f =  open(self.filename, "w")
        return self.f
    
    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.f:
            self.f.close()
        print("Exit")

# To Use our class as context manager
with ManageFile("contxtMg/note3.txt") as f:
    f.write("Class context manager\n")

# Using contextmanager method as decorator
# We have to import it from contextlib

@contextmanager
def handle_file(filename):
    file = open(filename, "w")
    try:
        yield file
    finally:
        file.close()

with handle_file("contxtMg/note4.txt") as f:
    f.write("Working with imported context manager decorator")
