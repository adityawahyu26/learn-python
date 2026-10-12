# width dan alignment pada string

# metode newline \n untuk bikin baris baru dan \t untuk tab
name = "aditya"
food = "mie ayam"
color = "blue"
format_str = f"name \t= {name}\nfood \t= {food}\ncolor \t= {color}"
print(format_str)

print("\n"+"="*10)

# metode strip """
format_str = f"""
name    = {name}
food    = {food}
color   = {color}
"""
print(format_str)