"""will be deleted"""
LIST_OF_GOODS = []
f = open('fruits', 'r+')
for line in f:
    LIST_OF_GOODS.append(line)
New = [line.rstrip() for line in LIST_OF_GOODS]
print(New)
f.close()
