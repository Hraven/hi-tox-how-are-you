from random import randint as rand
import time as T


class cave:
    potentialOre = ["copper", "iron", "tin", "lead", "dawnstone", "silver", "gold", "platinum", "diamond"]
    def __init__(self):
        self.ore = []

        for i in range(0, rand(0, 20)):
            self.ore.append(self.potentialOre[rand(0, len(self.potentialOre) - 1)])
    
    def giveOre(self):
        index = rand(0, len(self.ore))
        print(index)
        try:
            minedOre = self.ore[index]
            del self.ore[index]
            print("i found some %s" %minedOre)
            return minedOre

        except Exception as e:
            print("i found some stone and dust")
            return "stone"
