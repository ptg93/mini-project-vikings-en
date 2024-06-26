import random


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"


class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        result = random.choice(self.saxonArmy).receiveDamage(random.choice(self.vikingArmy).strength)
        self.saxonArmy[:] = [saxon for saxon in self.saxonArmy if saxon.health > 0]
        return result
        
    def saxonAttack(self):
        result = random.choice(self.vikingArmy).receiveDamage(random.choice(self.saxonArmy).strength)
        self.vikingArmy[:] = [viking for viking in self.vikingArmy if viking.health > 0]
        return result

    def showStatus(self):
        if not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        elif not self.saxonArmy:
            return "Vikings have won the war of the century!"
        else:
            return "Vikings and Saxons are still in the thick of battle."            
    pass
