def tambah(*args):
    count = 0
    for number in args:
        count += number
    return count

def kali(*args):
    count = 1
    for number in args:
        count *= number
    return count

def pangkat(n):
    return lambda x:x**n

