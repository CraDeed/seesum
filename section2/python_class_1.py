import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

class UserInfo:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def print_info(self):
        print("-" * 15)
        print("Name : " + self.name)
        print("Phone : " + self.phone)
        print("-" * 15)

    def __del__(self):
        print("delete!")

user1 = UserInfo('Kim','010-3433-7777')
user2 = UserInfo('Park','010-7777-7777')

print(id(user1))
print(id(user2))

#user1.set_info('Kim','010-3433-7777')
#user2.set_info('Park','010-7777-7777')

user1.print_info()
user2.print_info()

print(user1.__dict__)
print(user2.__dict__)

print(user1.phone, user1.name)
