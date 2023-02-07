class Person:
    def __init__(self, name, career):
      self.name = name
      self.career = career

    def getName(self):
      print(self.name)

leader = Person("Johnny", "biker")
enemy = Person("Chino", "rival")
watress = Person("Kathie", "lady")
print('******The Wild Ones******')



# Make a dict() for every character
leads = {"biker" : "Johnny", "rival" : "Chino", "lady" : "Kathie"}

for l, k in leads.items():
    print(l, ':', k)
    

