try:
    with open("config.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: config.txt ఫైల్ కనపడలేదు!")


try:
    print(10 / 0)
except ZeroDivisionError:
    print("సున్నా తో భాగించలేము!")