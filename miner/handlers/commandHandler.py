def nextTree(arr):
    stuff = []
    for i in enumerate(arr):
        stuff.append(i[1])
    return stuff

class world:
    def __init__(self):

        # this is a bit of a cluster fuck but here is what it does
        # in the commands are the most basic commands
        # in thier set are the commands that you could use after you use the basic one
        # this contineus troughout the tree
        self.commands = {
            "goto": {
                "vender": {
                    "shop": (
                        "sell",
                        "buy"
                        )
                    },
                "mine": {"mine" : ("R")}
            }
        }

        # yes i know this is not what it was meant to be and i
        # miss it but there is no need to get more complicated
        # then this, and i can't get it to work anymore
        # don't ask, i have no idea. i'm going to be making it again later
        # -R.

        def findPath(self, what):
            if what == sell:
                return ["vender", "shop", "sell", "ore"]

            if what == buy:
                return ["mine", "mine", "5"]
