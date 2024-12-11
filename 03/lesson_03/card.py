class card:
    number = '4562 4613 4697 3666'
    validDate = '10/26'
    holder = 'unknown'


    def __init__(self, number, date, holder):
        self.number = number
        self.validDate = date
        self.holder = holder



    def pay(self, amount):
        print("с карты ", self.number, "списано", amount)
