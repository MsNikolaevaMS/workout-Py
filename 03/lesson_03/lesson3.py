from user import User
from card import card

user1 = User("Mark")
user1.seyName()
user1.setAge(33)
user1.sayAge()

card = card("4562 4613 4697 3666", "10/26", "Mark A")
user1.addCard(card)
user1.getCard().pay(596.48)
