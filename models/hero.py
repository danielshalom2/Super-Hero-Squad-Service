

class Hero:
    def __init__(self, name, power, alignment):
        self.name = name
        self.health = 100
        self.status = "live"
        ####################
        # 25 < health < 75 => power decrease by 25%,status =  injured
        # 0 < health < 25 => power decrease by 50%, status =  injured
        # 0 >= health => status = dead
        ####################
        self.power = power
        self.alignment = alignment  # Good or Bad

    def setHeroHealth(self, health):
        self.health = health

    def setHeroPower(self, power):
        self.power = power

    def setHeroStatus(self, status):
        self.status = status
