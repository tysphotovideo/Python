class User:
    def __init__(self, first_name, last_name, email, age) -> None:
        self.first = first_name
        self.last = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        
    def display_info(self):
        print(self.first)
        print(self.last)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200 
    
    def spend_points(self, amount):
        self.gold_card_points = self.gold_card_points - amount

john_user = User("John", "Doe", "j@doe.com", 37)
john_user.display_info()
john_user.enroll()
tyler_user = User("Tyler", "Sellers", "t@sellers.com", 33)
lyndi_user = User("Lyndi", "Sellers", "l@sellers.com", 33)
john_user.spend_points(50)
tyler_user.enroll()
tyler_user.spend_points(80)
john_user.display_info()
tyler_user.display_info()
lyndi_user.display_info()


