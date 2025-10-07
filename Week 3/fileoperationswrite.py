try:
    with open("d:/Samplewrite1.txt", "a") as f:
        f.write("Hello Test Leaf\n")
        f.write("Learning Python ")
        f.write("is must for AI Engineer")
        print("File Write Completed\n")
except FileNotFoundError:
    print("File not found. Please check the filename and path.")
finally:
    f.close()


