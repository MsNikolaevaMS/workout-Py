class User:
    def __init__(self, name):
        print("я создался")
        self.username = name

    def seyName(self):
        print("меня зовут ", self.username)


user1 = User("Mark")
user2 = User("NIKI")
user3 = User("Petra")

user1.seyName()
user2.seyName()