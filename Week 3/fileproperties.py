try:
    with open("d:/Sample.txt", "r") as f:
        content = f.read()
        print(content)
        print("Filename:", f.name)
        print("Mode:", f.mode)
        print("Is Closed?", f.closed)

except FileNotFoundError:
    print("File not found. Please check the filename and path.")
finally:
    #f.close()
    print("Is Closed?", f.closed)


