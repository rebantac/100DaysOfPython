class Instagram: # class defn


    def __init__(self, a, b): # constructor
        self.id = a
        self.name = b
        self.follower = 0
        self.following = 0

    def follow(self, user): # when the calling object(self) follows the other object(here - user)
        user.follower += 1
        self.following += 1


user_1 = Instagram(1, "Xyz")
user_2 = Instagram(2, "Abc")

user_1.follow(user_2)

print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)