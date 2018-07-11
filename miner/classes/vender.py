from handlers.itemHandler import itemHandler
IH = itemHandler()

# the functions are made in prospective to the class so the vender may sell something while the
# miner buy the item

class vender:
    inventory = []

    # sell stuff
    def sell(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print("here you go")
            return item
        else:
            print("I don't have that in stock")

    # buys something from the miner
    def buy(self, what, inv):

        if "ore" in what:
            sell = []
            price = 0
            for i in enumerate(inv):
                type = IH.isType(i[1])
                if type == "ore":
                    sell.append(i[1])
            print("all your ore ay, ok i'll take it")
            print("you sure you want to sell:")
            for i in enumerate(sell):
                print(i[1])

            print("good")
            print(sell)
            for i in enumerate(sell):
                price += IH.price(i[1])
            return price, sell


        if "ore" not in what:
            for i in enumerate(accept):
                if what in i:
                    print("you found some %s hu, i'll buy it for: " %i[1] + "%s" %price[i[1]])
                    return price[i[0]]

    # shows inventory
    def show(self):
        for i in enumerate(self.inventory):
            print(i[1])
