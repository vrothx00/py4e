fname = input("Enter file name: ")
if len(fname) < 1:
        fname = "mbox-short.txt"

try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)


lst = list()
count = 0
for line in fh:
    line = line.rstrip()
    if line.startswith('From'):
        words = line.split()
        if len(words) > 2:
            lst.append(words[1])
            count += 1


for word in lst:
    print(word)
print("There were", count, "lines in the file with From as the first word")
