filestream = open("ex15_example.txt")
print(filestream.readline())
print(filestream.readline())
print(filestream.readline())
print(filestream.readline())

filestream2 = open("ex15_example.txt")
print("------------------------------------------------")
print(filestream2.read())