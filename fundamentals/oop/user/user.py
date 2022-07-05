class User():
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print("User already a member")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self
    
    def spend_points(self, amount):
        if self.gold_card_points < amount:
            print("User does not have enough funds")
        else:
            self.gold_card_points = self.gold_card_points - amount
        return self

new_user_1 = User("kevin", "huynh", "kvhuynh820@gmail.com", "22")
new_user_1.display_info().spend_points(50)
new_user_2 = User("bob", "wart", "bwart@gmail.com", "22")
new_user_3 = User("sally", "thompson", "salthomp@gmail.com", "22")
print(new_user_1.gold_card_points)

new_user_2.enroll().spend_points(80)

new_user_1.display_info(), new_user_2.display_info(), new_user_3.display_info()
new_user_2.enroll()
new_user_3.spend_points(40)