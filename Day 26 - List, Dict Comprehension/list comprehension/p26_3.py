with open("file1.txt") as f1:
    num_list1 = f1.readlines()

with open("file2.txt") as f2:
    num_list2 = f2.readlines()

result = [int(num.strip()) for num in num_list1 if num in num_list2]
# Write your code above 👆

print(result)
