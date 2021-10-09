from models.squad import Squad
from models.hero import Hero


def heroesCreation():
    h1 = Hero("Deadpool", 100, "good")
    h2 = Hero("Leonardo", 75, "good")
    h3 = Hero("Donatello", 58, "good")
    h4 = Hero("Michelangelo", 85, "good")
    h5 = Hero("Raphael", 59, "good")
    h6 = Hero("Loki", 100, "bad")
    h7 = Hero("Luke Cage", 55, "bad")
    h8 = Hero("Venom", 96, "bad")
    h9 = Hero("Cyborg Superman", 100, "bad")
    h10 = Hero("Bizarro", 85, "bad")

    return [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10]


def squadCreation():
    s1 = Squad("Ninja Turtles")
    s2 = Squad("The Avengers")
    s3 = Squad("The Frightful Four")
    s4 = Squad("Good Team")
    s5 = Squad("Bad Team")
    # s6 = Squad("Ninja Turtles") --> throw exception, name already has been taken
    return [s1, s2, s3, s4, s5]
