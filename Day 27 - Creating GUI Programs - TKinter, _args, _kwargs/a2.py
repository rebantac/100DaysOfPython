# Unlimited Positional Arguments => *args

def add(*args):
    # Stores as a tuple
    print(args[0])
    sum = 0
    for n in args:
        sum += n
    print(f"Sum = {sum}")

# add(1, 2, 3)
# add(4, 11)
# add(9)


###################
# Many Keyworded Arguments => **kwargs


def calculate(**kwargs):
    # stores as a dictionary
    s1 = kwargs.get("str1")
    s2 = kwargs.get("str2")
    print(s1, s2)

    # using .get() instead of .[], bcz .get() returns Null if the key doesn't exist


calculate(str1 = "one", str2 = "two")
calculate(str1 = "one")
