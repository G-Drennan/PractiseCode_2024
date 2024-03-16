import math
import random 

def HP_calc(D10, A10):
    average_value = 10 + (5 *(D10 + A10) / 2)
    result = 5 * round(average_value / 5) 
    return result

def roll():
        roll = random.randint(1, 10)
        if roll == 10: 
            print("\n Explode!\n")
            roll += random.randint(1, 10)
        elif roll == 1:
            print("\n Implode!\n")
            roll -= random.randint(1, 10)
        else:
            roll = roll 
        output = roll 
        return output 

class npc:
   
    Inte = 6
    Ref = 6
    Dex = 6 
    Tech = 6
    Cool = 6
    Will = 6
    Move = 6
    Body = 6

    def __init__(self, id, tag):
        self.id = id
        self.tag = tag 
        self.HP_Max = HP_calc(self.Will, self.Body) 
        self.current_HP = self.HP_Max

    def rollNew(self, stat, bonus):
        output = roll()+ bonus + getattr(self, stat)
        return output

    def Damage_HP(self, dmg):
        self.current_HP -= dmg
    
    def Gain_HP(self, heal):
        self.current_HP -= heal

    def get_current_HP(self): 
        return self.current_HP
    
    def get_tag(self):
        return self.tag

class Driver(npc):
    MotoRank = 0
    DriveBonus = 6
    AtkBonus = 6
    
    Car_Hp = 50
    Current_car_HP = Car_Hp

    def atk_Ref(self):
        outcome = roll() + self.Ref + self.AtkBonus
        return outcome 
    
    def Drive(self):
        return roll() + self.Ref + self.DriveBonus
    
    def Damage_Car_HP(self, dmg):
        self.Current_car_HP -= dmg
    
    def Gain_Car_HP(self, heal):
        self.Current_car_HP -= heal
    def get_type(self):
        return "Driver" 

class RoadGanger(Driver):
    Inte = 4
    Ref = 6
    Dex = 4 
    Tech = 4
    Cool = 3
    Will = 3
    Move = 3
    Body = 3
    MotoRank = 1

    DriveBonus = 4 + MotoRank
    AtkBonus = 4
    def get_type(self):
        return "RoadGanger"


class nomad(Driver):
    Inte = 6
    Ref = 8
    Dex = 6 
    Tech = 3
    Cool = 5
    Will = 6 
    Move = 6
    Body = 6
    MotoRank = 3

    DriveBonus = 4 + MotoRank
    AtkBonus = 6

    def get_type(self):
        return "nomad"

class outrider(Driver):
    Inte = 6
    Ref = 8
    Dex = 8 
    Tech = 3
    Cool = 5
    Will = 6
    Move = 6
    Body = 6
    MotoRank = 4

    DriveBonus = 6 + MotoRank
    AtkBonus = 6

    def get_type(self):
        return "outrider" 

n = 0; 

Racers = []
RacerTags = ["Aldecaldo 1", "Aldecaldo 2", "Jodes 1", "Blood Nation 1", "Meta 1", "Wraiths 1", "Wraiths 2" ]
print("Initilizing Race...\n") 
while n<len(RacerTags): 
    if "Aldecaldo" in RacerTags[n] or "Meta" in RacerTags[n]:
        Racers.append(outrider(n, RacerTags[n]))
    elif "Jodes" in RacerTags[n] or "Blood Nation" in RacerTags[n]:
        Racers.append(RoadGanger(n, RacerTags[n]))
    elif "Wraiths" in RacerTags[n]:   
        Racers.append(nomad(n, RacerTags[n]))
    
    print(Racers[n].get_tag(), " ", Racers[n].get_type(), end='\n\n')   
    n+=1  

print("READY!") 

action = input("Drive or Attack: ")  
while action.lower() != 'end': 
    print("\n")  
    if action.lower() == 'drive':
        for r in Racers:
            print(r.get_tag(), "Drive:", r.Drive())
    elif action.lower() == 'attack': 
        for r in Racers:
            print(r.get_tag(), "Attack:", r.atk_Ref())  
    action = input("\nDrive or Attack: ")    


"""
action = input("Drive or Attack: ") 
print("\n")  
if action.lower() == 'drive':
    for r in Racers:
        print(r.get_tag(), "Drive:", r.Drive())
elif action.lower() == 'attack': 
    for r in Racers:
        print(r.get_tag(), "Attack:", r.atk_Ref())   """


