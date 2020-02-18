import os

folder = os.path.dirname(r'/home/laz/')
file = folder+'/file.txt'


def get_password(obj):
    file = open(obj, 'r')
    for line in file:
        password = line
    return password
