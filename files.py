with open ("python_i_have_learned.txt") as file_object:
    contents = file_object.read()
    print(contents * 3)

with open ("python_i_have_learned.txt") as file_object:
    for line in file_object:
        print(line)

with open ("python_i_have_learned.txt") as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line)

user = input("please enter your name  ")
with open ("guest.txt" ,"w") as file_object:
    file_object.write(user)

why = ""
while why != "q":
    why = input("what do you like about python  ")
    with open ("guest.txt" ,"a") as file_object:
        file_object.write(why + "\n")


