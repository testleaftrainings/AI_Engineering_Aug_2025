list_to_append = [
    'Python is very efficient.\n',
    'Python uses interpretter.\n',
    'Python is ease to use.\n'
]
try:
    #with open("d:/Samplewrite.txt", "w") as f:
    with open('d:/Samplewrite.txt', 'a') as f:
        for line in list_to_append:
            f.write(line)
        print("File Append Completed\n")
except FileNotFoundError:
    print("File not found. Please check the filename and path.")
finally:
    f.close()


