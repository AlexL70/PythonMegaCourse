file = open("members.txt", 'r')
members = file.readlines()
file.close()

newMember = input("Enter new member's name: ")
members.append(f"{newMember}\n")
file = open("members.txt", 'w')
file.writelines(members)
file.close()
for member in members:
    print(member, end='')