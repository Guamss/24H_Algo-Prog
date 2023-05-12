danseurs_pos = list("abcdefghijklmnop")
with open("salle9.txt") as file:
    content_file_l = file.readlines()
content_file_l[0] = content_file_l[0].replace("\n", "")
actions = content_file_l[0].split(",")
for action in actions:
    if action[0] == "s":
        for i in range(int(action[1:])):
            danseurs_pos.insert(i, danseurs_pos.pop())
    elif action[0] == "x":
        action = action.replace("x", "")
        action = action.split("/")
        danseurs_pos[int(action[0])], danseurs_pos[int(action[1])] = danseurs_pos[int(action[1])], danseurs_pos[int(action[0])]   
    elif action[0] == "p":
        action = action.replace("p", "", 1)
        action = action.split("/")
        danseurs_pos[danseurs_pos.index(action[0])], danseurs_pos[danseurs_pos.index(action[1])] = danseurs_pos[danseurs_pos.index(action[1])], danseurs_pos[danseurs_pos.index(action[0])]   


print(content_file_l)
print(danseurs_pos)
