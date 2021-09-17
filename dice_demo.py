import random
print("D I C E  S T I M U L A T I O N")
x = "y"

while x == "y" :
    num = random.randint(1,6)

    if num==1:
        print("---------")
        print("|       |")
        print("|   o   |")
        print("|       |")
        print("---------")        

    if num==2:
        print("---------")
        print("|   o   |")
        print("|       |")
        print("|   o   |")
        print("---------")        

    if num==3:
        print("---------")
        print("|   o   |")
        print("|   o   |")
        print("|   o   |")
        print("---------")        

    if num==4:
        print("---------")
        print("| o   o |")
        print("|       |")
        print("| o   o |")
        print("---------")        

    if num==5:
        print("---------")
        print("| o   o |")
        print("|   o   |")
        print("| o   o |")
        print("---------")        

    if num==6:
        print("---------")
        print("| o   o |")
        print("| o   o |")
        print("| o   o |")
        print("---------")        

    x=input("Press enter 'y' to roll !! \n")