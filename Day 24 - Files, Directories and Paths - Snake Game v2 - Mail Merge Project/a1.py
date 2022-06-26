# file1 = open("file1.txt")
# contents = file1.read()
# print(contents)
# file1.close() # essential to close file

with open("file1.txt") as file1: # by default mode='r' i.e, read
    # same output as above block, but in this case, we don't have to close the file
    contents = file1.read()
    print(contents)


# with open("file1.txt", mode="w") as file2:  # to write
#     file2.write("\nThis is written, erasing previous lines")


# with open("file1.txt", mode="a") as file3:  # to append
#     file3.write("\nThis is appended")
