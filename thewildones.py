class Person:
    def __init__(self, name, career):
      self.name = name
      self.career = career

    def getName(self):
      print(self.name)

# main characters
leader = Person("Johnny", "biker")
enemy = Person("Chino", "rival")
watress = Person("Kathie", "lady")

cast = dict()
cast = [leader.name, enemy.name, watress.name]
print('******The Wild Ones******')

leader.getName()

# Make a dict() for every character
leads = {"biker" : "Johnny", "rival" : "Chino", "lady" : "Kathie"}

for l, k in leads.items():
    print(l, ':', k)    

print("What will this program do -_o_-")
