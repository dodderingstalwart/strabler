print('******The Wild Ones******')

# Make a dict() for every character
leads = {"biker" : "Johnny", "rival" : "Chino", "lady" : "Kathie"}

for l, k in leads.items():
    print(l, k)
    
with open("absalom.txt", "r") as fhand:
    for line in fhand:
        for word in line.rstrip():
            print(len(word))

