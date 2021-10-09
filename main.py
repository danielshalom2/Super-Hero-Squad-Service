from models.data import heroesCreation, squadCreation
from models.service import battle, heroComparison, heroToSquad, changeAlignment


def main():
    heroes = heroesCreation()
    squads = squadCreation()
    squads[3].members = [x for x in heroes if x.alignment == "good"]
    squads[4].members = [x for x in heroes if x.alignment == "bad"]
    print("Good Team:")
    for hero in squads[3].members:
        print(hero.name)
    print("Bad Team:")
    for hero in squads[4].members:
        print(hero.name)
    # simulate battle
    battle(squads[3], squads[4])
    # show battle not allowed while in-action
    squads[2].status = "in-action"
    battle(squads[3], squads[2])
    # heroes power comparison
    heroComparison(heroes[0], heroes[1])
    # move hero from one squad to other
    squads[3].members = [x for x in heroes if x.alignment == "good"]
    heroToSquad(heroes[0], squads[2], squads[3])
    # change hero alignment
    changeAlignment(heroes[0])


if __name__ == "__main__":
    main()
