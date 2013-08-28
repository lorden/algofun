"""
Given a function that generates a random number between 1 and 2, write a
function that generates an equally probable random number between 1 and 6
"""


def rand2():
    import random
    return random.randrange(2) + 1


def rand6():
    binary = "%s%s%s" % (rand2() - 1, rand2() - 1, rand2() - 1)
    num = int(binary, 2) + 1
    while num > 6:
        binary = "%s%s%s" % (rand2() - 1, rand2() - 1, rand2() - 1)
        num = int(binary, 2) + 1
    return num

rolls = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
total = 10000

for i in xrange(total):
    rolls[rand6()] += 1

for number, r in rolls.items():
    print "%s => %s%%  %s" % (number, 100 * r / total, r)
