import os

root = 'c:\users\marco\desktop\jazz books'

for path, subdirs, files in os.walk(root):
    for name in files:
        print os.path.join(path, name)
