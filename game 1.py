import random

print(" wellcome to ")
print(" Snake Water Gun")
print(" Enter w : for water")
print("Enter g : for Gun")
print("Enter s : for Snake")

count=0
computer=0
winner =0
while(count<3):
    s = str(input(" Press : "))
    lst = ["snake", "water", "gun"]
    a = random.choice(lst)
    if( s=="s"and a=="water"):
            winner=winner+1
            print("computer choice is:",a)
    elif(s=="s"and a=="gun"):
                computer=computer+1
                print("computer choice is:", a)

    elif(s=="w"and a=="gun"):
               # print("you won ")
               winner=winner+1
               print("computer choice is:", a)

    elif(s=="W"and a=="snake"):
                computer=computer+1
                print("computer choice is:", a)

    elif(s=="g" and a=="snake"):
                winner = winner + 1
                print("computer choice is:", a)

    elif(s=="g"and a=="water"):

        computer = computer + 1
        print("computer choice is:", a)
    count=count+1

print("User Win this match ",winner," times")
print("PC win this game ",computer,"times")






