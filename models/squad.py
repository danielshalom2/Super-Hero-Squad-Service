squadList = []


class Squad:

    def __init__(self, squadName):
        if squadName in squadList:
            raise Exception("Sorry, this name alrady taken")
        self.squadName = squadName
        squadList.append(squadName)
        self.status = "resting"
        self.members = []
        print("%s squad has been created secessfully" % squadName)
