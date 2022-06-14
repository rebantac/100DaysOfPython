# sum of even numbers from 1 to 100 using range()

sum = 0
for number in range(0, 101, 2):
    sum += number

print("Sum: ", sum)