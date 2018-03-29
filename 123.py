LIST_OF_MANS_NAMES = []
f = open('123.txt', 'r+')
for line in f:
    LIST_OF_MANS_NAMES.append(line)
New = [line.rstrip() for line in LIST_OF_MANS_NAMES]
print(New)
f.close()
