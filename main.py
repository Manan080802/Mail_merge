names = []
with open("./input/invited_name/invited_names.txt") as file:
    names = file.readlines()

    # for name in data.split("\n"):
    #     names.append(name)






for name in names:
    name = name.strip()
    with open("./input/Letters/starting_letter.txt") as file:
        data = file.read()
        new_letter= data.replace("[name]",name)
    with open(f"./output/ReadyToSend/letter_for_{name}.txt",mode="w") as file:
        file.write(new_letter)