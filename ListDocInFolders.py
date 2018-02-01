import os
root = 'C:\\Users\\marco\\Desktop\\Folder'
values=''

for path, subdirs, files in os.walk(root):
    for name in files:
        values = values + os.path.join(path, name) + '\n'

samplef = open('sample.txt', 'w')
samplef.write(values)
samplef.close() 
