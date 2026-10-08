print ("Hello")
print ("World")

print ("This is a test of the interpreter.")

a = 5
print ("The value of a is:", a)

# menggunakan interpreter dan bytecode itu berbeda
# 01_interpreter_dan_bytecode/Main.py adalah metode interpreter
# 01_interpreter_dan_bytecode/__pycache__/Main.cpython-310.pyc adalah metode bytecode
# untuk compile python -m py_compile Main.py/sourcecode.py
# bytecode / compile lebih cepat dari interpreter, karena bytecode sudah di compile, sedangkan interpreter harus membaca source code dan mengeksekusi langsung