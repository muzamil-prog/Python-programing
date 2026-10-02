class Character:
    def __init__(self, name, health, level):
        self.name=name
        self.health=health
        self.level=level
    
    def attaks(self, other):
        damage=10
        print(f"{self.name} attaks{other.name}")
        other.take_damage(damage)
    def take_damage(self, damage):
        self.health=self.health-damage
        if self.health <0:
            self.health=0
        print(f"{self.name} took {damage} damage") 
    def show(self):
        print("----------------------------")
        print("Name:" , self.name)
        print("health:", self.health) 
        print("level:", self.level)
        print("------------------------------")   
        
player1=Character("ali", 70, 2)
player2=Character("qasim", 80, 1)
player1.show()
player2.show()
player1.attaks(player2)
player1.show()
player2.attaks(player1)
player2.show()            
            