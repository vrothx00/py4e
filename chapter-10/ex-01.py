name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()
lst = list()

for line in handle:
    words = line.split()
    if len(words) > 2 and words[0] == 'From':
        hour = words[5].split(':')
        counts[hour[0]] = counts.get(hour[0], 0) + 1

for k, v in counts.items():
    lst.append((k,v))

lst.sort()
for k,v in lst:
    print(k,v)
