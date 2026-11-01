import random
import string

def random_number(len):
    count = ''.join(random.choice(string.ascii_letters) for i in range(len))
    return count
