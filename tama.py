class Tamagochi: 
    def __init__(self, name):
        self.name = name
        self.age = 1
        self.hunger = 100
        self.happiness = 100

    def timepassed(self) :
        self.age += 1
        self.hunger -= 10
        self.happiness -= 10
        if self.hunger <= 0 :
            print(f"{self.name} dies of starvation.")
            return "dead"
        elif self.happiness <= 0 :
            print(f"{self.name} dies of boredom")
            return "dead"
        else :
            print(f"{self.name} aged!")
    def feed(self) :
        if self.hunger > 80 :
            print(f"{self.name} is not hungry right now.")
        else :
            self.hunger += 20
            print(f"{self.name} ate.")

    def play(self) :
        if self.happiness > 80 :
            print(f"{self.name} is not in the mood to play.")
        else :
            self.happiness += 20
            print(f"{self.name} enjoyed playing!")

pet = Tamagochi("tama") 

while True :
    while True :
        try :
            choice = int(input("[1] Feed, [2] Play, [3] Wait    "))
            break
        except :
            print("invalid choice")
    if choice == 1 :
        pet.feed()
    elif choice == 2 :
        pet.play()
    elif choice == 3 :
        pass
    alive = pet.timepassed()
    if alive == "dead" :
        break