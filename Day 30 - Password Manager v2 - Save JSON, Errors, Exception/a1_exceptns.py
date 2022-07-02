
# try: # the code where a exception can occur is written here
#     file = open("a_file.txt")
# except FileNotFoundError as error_msg: # this block is executed if the given exception occurs in the try block
#     print(f"{error_msg}. New file created")
#     file = open("a_file.txt", "w")
#     file.write("Something")
# else: # this bloack is executed when no exceptns occurs in the try block
#     print("No exceptions occured")
#     print(file.read())
# finally: # this block is executed whether or not an exceptions occurs 
#     print("Inside finally block")
#     file.close()


# Raise an Exception:
height = float(input("height: "))

if height > 3:
    raise ValueError("Human height can not be > 3 m.")

print(height)