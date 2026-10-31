# menggunakan library numbers
from numbers import Number

# fungsi operasi aritmatika add
def add(a,b) :
    # membuat exception dengan if statement
    if not isinstance(a,Number) or not isinstance(b,Number):
        print("input harus angka!")
    return a+b

print(add("a","b"))

# mencetak error message
number = 0

# menggunakan Exception sebagai error message
try :
    count = 10/number
    print(count)
except Exception as error_message:
    print(error_message)

# menggunakan zerodivisionerror sebagai error message
try :
    count = 10/number
    print(count)
except ZeroDivisionError as error_message:
    print(error_message)