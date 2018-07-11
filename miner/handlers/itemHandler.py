class itemHandler:
    def __init__(self):
        # a bunch of items in a dict
        self.items = {
            "copper": {"type": ("ore"), "price": (5),"state": ()},
            "iron": {"type": ("ore"), "price": (7),"state": ()},
            "tin": {"type": ("ore"), "price": (7),"state": ()},
            "lead": {"type": ("ore"), "price": (7),"state": ()},
            "dawnstone": {"type": ("ore"), "price": (20),"state": ()},
            "silver": {"type": ("ore"), "price": (8),"state": ()},
            "gold": {"type": ("ore"), "price": (8),"state": ()},
            "platinum": {"type": ("ore"), "price": (9),"state": ()},
            "diamond": {"type": ("ore"), "price": (10),"state": ()},
            "stone": {"type": ("ore"), "price": (2),"state": ()},
            "pickaxe": {"type": ("item"), "price": (20),"state": ()},
            "water": {"type": ("food"), "price": (2),"state": ()},
            "bread": {"type": ("food"), "price": (2),"state": ()},
            # "item": {"type": (""), "price": ()},
            }

    def isType(self, item):
        thing = self.items[item]
        type = thing["type"]
        return type

    def price(self, item):
        try:
            thing = self.items[item]
            price = thing["price"]
            return price
        except:
            return 0
