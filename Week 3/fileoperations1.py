try:
    with open("d:/Sample.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not found. Please check the filename and path.")
finally:
    f.close()


