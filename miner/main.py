from miner import miner
import random
miner = miner()


# config ----+ {
genAmount = 10 # the amount of moves it will make before evolving

# config ----+ }

# setup ----+ {

moves = []
for i in range(genAmount):
    moves.append(0)

bestmoves = []
gen = 0
cut = []
bestnet = 1
prewelth = 1
bestgen = 0
i = []
# setup ----+ }

# functions ----+ {
# getting the path to a place

def findPath(what):
    if what == "sell":
        mine = ["goto", "vender", "shop", "sell", "ore"]
        time = 4
        return mine, time

    if what == "mine":
        mine = ["goto", "cave", "mine"]
        time = 2
        return mine, time

# to make it easer to mutate the moveset
mutation = 0.10 # it has a 1/4 chance to change from 1 to 0 or vice fersa
def mutate(moveSet):
    for i in enumerate(moveSet):
        M = random.random()
        if M <= mutation and i[1]:
            moveSet[i[0]] = 0
        elif M <= mutation and not i[1]:
            moveSet[i[0]] = 1
    return moveSet


# functions ----+ }




# this is the ai for the miner
while True:
    gen += 1
    moves = mutate(moves)
    for i in enumerate(moves):
        # this gives the commands to the miner
        print(moves)
        if i[1]:
            path = findPath("mine")[0]
            time = findPath("mine")[1]
        else:
            path = findPath("sell")[0]
            time = findPath("sell")[1]


        for i in range(0, time):
            cut = miner.action(path)
            print(cut)
            try:
                for i in enumerate(cut):
                    print("here %s" %i[1])
                    path.remove(i[1])
                    print(path)
            except:
                cut = []
                break
        path = []

    welth = miner.Smoney()
    net = welth - prewelth
    print(welth)
    if net > bestnet:
        bestmoves = moves
        bestnet = net
        bestgen = gen

    prewelth = welth

    print("+-----------+")
    print("stats")
    print("+-----------+")
    print("gen: %s" %gen)
    print("net gain/loss: %s" %net)
    print("gen moveset: %s" %moves)
    print("best gen: %s" %bestgen)
    print("best gen moveset: %s" %bestmoves)
    print("best gen net: %s" %bestnet)

    input()
