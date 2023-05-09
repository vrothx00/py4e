# Write a program to read through a file and print the contents
# of the file (line by line) all in upper case.

fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()
for line in fh:
    line = line.strip()
    print(line.upper())
