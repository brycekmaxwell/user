
class User:	
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name,self.last_name,self.age,self.email,self.is_rewards_member,self.gold_card_points)

    def enroll(self):
        is_rewards_member = True

    def spend_points(self, amount):
        gold_card_points = gold_card_points - amount

User_mia = User("Mia", "Thermopolis", 32, "princessofgenovia@gmail.com")
User_scott = User("Scott", "Styles", 17, "wolffriend@yahoo.com")
User_ted = User("Ted", "Lasso", 46, "englishfootbal@crumpet.com")


User_mia.enroll()
User_mia.spend_points(50)

User_scott.enroll()
User_scott.spend_points(80)

User_mia.display_info()
User_scott.display_info()