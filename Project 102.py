class chores():

    def __init__(self, broom, left_over_toys):
        self.broom = broom
        broom = str(input("Pick up the broom: "))
        self.left_over_toys = left_over_toys
        

    

    def broom_house():
        broom = str(input("Pick up the broom: "))
        if broom == str("Yes"):
            print("Start broming")

        elif broom == str("No"):
            print("You are grounded if you do not broom the floor")


    def pickUp_toys():
        toys = 10 
        condintion = True
        while(condintion):
            print("Toys remaning:", toys)
            toys = toys - 1

            if toys == 0:
                print("You are done picking up your toys")
                result = False
                
                break


    



#Aditya = chores('broom', 'left_over_toys', 'mop')       


chores.broom_house()

# This is option 2 for the chores class, uncomment the next line for it to work
#chores.pickUp_toys()



