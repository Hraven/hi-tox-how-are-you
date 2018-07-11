from classes.vender import vender
from classes.mine import cave
from tqdm import tqdm
import time as T
vender = vender()

# "I don't need comments, i'll just read the code" -someone who doesn't work with classes


# the miner class were the actions are handeled and the script does it's things
class miner:
    where = "home"
    def __init__(self):
        self.money = 0
        self.inventory = ["pickaxe"]

    # this is the action handler it handles what you want the miner to do
    def action(self, action):
        # the basic goto
        if "goto" in action[0]:
            print("where do i go")
            self.goto(action[1])
            print(action[0:1])
            return action[0:2]

        # for access to the shop
        elif "shop" in action[0]:
            if self.where == "vender":
                print("what should i do")
                self.shop(action[1])
                return action[0:2]
            else:
                print("but i'm not at a store")

        # a place to mine
        elif "mine" in action[0]:
            # comence the mining
            if self.where == "cave":
                print("for how long should i mine")
                self.mine(5)
                return action[0]
            else:
                print("i'm not at the mine")
        # looking in your wallet
        elif "money" in action[0]:
            print(self.money)
            return self.money

        # for checking your inv
        elif "inventory" in action[0]:
            print(self.inventory)
        else:
            pass

        # yes i could have put this in a dict but i didn't know the were a thing back when i made this


    # for going somewhere
    def goto(self, goto):
        self.where = goto


    # for handeling the vender
    def shop(self, what = None):
        vender.show()
        if self.where == "vender":
            # this is for buying something from the vender
            if "buy" in what:
                print("what should i buy")
                item = vender.sell("ore")
                self.inventory.append(item)
                print(self.inventory)

            # this is for selling to the vender
            if "sell" in what:
                print(self.inventory)
                item = "ore"
                if item in self.inventory or item == "ore":
                    shop = vender.buy(item, self.inventory)
                    self.money += shop[0]
                    for i in enumerate(shop[1]):
                        self.inventory.remove(i[1])
                else:
                    print("i don't have that")

        else:
            print("i'm not at a store")

    # for going to the mine
    def mine(self, time):
        mine = cave()
        for i in range(0, time):
            print("mining")
            for i in tqdm(range(10)):
                T.sleep(0.1)
            self.inventory.append(mine.giveOre())

    def Smoney(self):
        return self.money
