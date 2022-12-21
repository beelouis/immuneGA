class Body:
    def __init__(self, label, health):
        self.health = health
        self.antigens = []
        self.label = label

    def printHealth():
        print(self.health)

    def takeDamage(self, damage):
        self.health -= damage

    def checkDeath(self):
        return True if self.health <= 0 else False
