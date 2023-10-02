class Players:
    Health=0
    Name=""
    Strike_power=0
    def attack(self,obj):
        if obj.Health>=0:
            obj.Health-=self.Strike_power
            print("%s Got attcked " %obj.name)
            print("Health=",obj.Health)
            
        else:
            c="Game won by"
            print("%s is Eliminated" % obj.name)
            print("+","-"*(len(self.name)+len(c)),"+")
            print("|",c ,self.name,"|")
            print("+","-"*(len(self.name)+len(c)),"+")

class Hero(Players):
    def __init__(self,name):
        self.name=name
        self.Health=200
        self.Strike_power=20
        print("Health=",self.Health)

class villian(Players):
    def __init__(self,name):
        self.name=name
        self.Health=150
        self.Strike_power=25
        print("Health=",self.Health)