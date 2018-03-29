LIST_OF_MANS_NAMES = []
LIST_OF_GIRLS_NAMES = []
f = open('mans.txt', 'r+')
for line in f:
    LIST_OF_MANS_NAMES.append(line)
New = [line.rstrip() for line in LIST_OF_MANS_NAMES]
print(New)
f.close()


f = open('girls.txt', 'r+')
for line in f:
    LIST_OF_GIRLS_NAMES.append(line)
New = [line.rstrip() for line in LIST_OF_GIRLS_NAMES]
print(New)
f.close()
