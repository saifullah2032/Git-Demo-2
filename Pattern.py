print("-- Pattern --")
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol to use: ")
print(f"Pattern of {symbol} with {rows} rows and {cols} columns:")
for row in range(rows):
    for col in range(cols):
        print(symbol, end="")
    cols -= 1
    print()
print("Pattern complete.")
print("--pattern--")
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol to use: ")
print(f"Pattern of {symbol} with {rows} rows and {cols} columns:")
for row in range(rows):
    for col in range(cols):
        print(symbol, end="")
    print()
print("Pattern complete.")
