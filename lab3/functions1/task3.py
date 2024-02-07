def solve(numheads,numlegs):
    rabbit = (numlegs - numheads * 2) // 2
    chicken = numheads - rabbit
    print("There are " + str(rabbit) + " rabbits and " + str(chicken) + " chickens")

solve(35, 94)