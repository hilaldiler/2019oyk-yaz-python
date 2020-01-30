from random import randint
with open('data.txt',"w") as file:
    for i in range(0,100):
        file.write("\\{}|{}|".format(
            randint(0,100),
            randint(0,100)

        ))