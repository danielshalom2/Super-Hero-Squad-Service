import random


def updateBattleResults(hero, squadMembers, squadName):
    if(hero.health < 75 and hero.health > 25):
        if(hero.status == "injured"):
            pass
        else:
            hero.setHeroStatus("injured")
            print("%s from %s injured! decreasing power..." %
                  (hero.name, squadName))
            hero.setHeroPower(int(hero.power * 0.75))
    elif(hero.health < 25 and hero.health > 0):
        hero.setHeroPower(int(hero.power * 0.90))
    elif(hero.health <= 0):
        print("%s from squad %s DEAD :(" % (hero.name, squadName))
        hero.status = "dead"
        squadMembers.remove(hero)


def battle(squadA, squadB):
    if (squadA.status != "resting"):
        print("%s squad in-action, wait for sqaud status \"resting\"" %
              squadA.squadName)
        return
    elif (squadB.status != "resting"):
        print("%s squad in-action,  wait for sqaud status \"resting\"" %
              squadB.squadName)
        return
    else:
        squadA.status = squadB.status = "in-action"
        while(len(squadA.members) > 0 and len(squadB.members) > 0):
            heroA = random.choice(squadA.members)
            heroB = random.choice(squadB.members)
            heroAHit = random.choice(
                range(1, heroA.power))
            heroBHit = random.choice(
                range(1, heroB.power))
            print("%s from squad %s make a damage of %d to %s from squad %s" %
                  (heroA.name, squadA.squadName, heroAHit, heroB.name, squadB.squadName))
            print("%s from squad %s make a damage of %d to %s from squad %s" %
                  (heroB.name, squadB.squadName, heroBHit, heroA.name, squadA.squadName))
            heroA.setHeroHealth(heroA.health - heroBHit)
            heroB.setHeroHealth(heroB.health - heroAHit)
            updateBattleResults(heroA, squadA.members, squadA.squadName)
            updateBattleResults(heroB, squadB.members, squadB.squadName)
        if(len(squadA.members) > 0):
            print("squad %s WINS!" % squadA.squadName)
        else:
            print("squad %s WINS!" % squadB.squadName)
        squadA.status = squadB.status = "resting"


def heroComparison(heroA, heroB):
    if (heroA.power > heroB.power):
        print("%s is stronger than %s " % (heroA.name, heroB.name))
    elif(heroA.power < heroB.power):
        print("%s is stronger than %s " % (heroA.name, heroB.name))
    else:
        print("%s and %s has the same power" % (heroA.name, heroB.name))


def heroToSquad(hero, inSquad, outSquad):
    print("squad-in:(before)")
    for item in inSquad.members:
        print(item.name)
    print("squad-out:(before)")
    for item in outSquad.members:
        print(item.name)
    if hero not in outSquad.members:
        raise Exception("%s not in %s squad" % (hero.name, outSquad.squadName))
    inSquad.members.append(hero)
    outSquad.members.remove(hero)
    print("squad-in:(After)")
    for item in inSquad.members:
        print(item.name)
    print("squad-out:(After)")
    for item in outSquad.members:
        print(item.name)


def changeAlignment(hero):
    print("%s is: %s (BEFORE change alignment)" % (hero.name, hero.alignment))
    if(hero.alignment == "bad"):
        hero.alignment = "good"
    else:
        hero.alignment = "bad"
    print("%s is: %s (AFTER change alignment)" % (hero.name, hero.alignment))
