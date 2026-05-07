try:
    with open("config.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: config.txt File not visible!")


try:
    print(10 / 0)
except ZeroDivisionError:
    print("can't devide with zero!")