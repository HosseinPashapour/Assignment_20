import random

boys = ["mohammad", "sobhan", "abdollah", "kiya", "mahdi", "sajjad", "homan", "arman"]
girls = ["mahtab", "hane", "harir", "fateme", "kiana", "faezeh", "minoo", "mina", "soghra"]

Marriage = []

for i in range( 0, len(boys)):
    boy = random.choice(boys)
    girl = random.choice(girls)
    Marriage.append((boy, girl))
    boys.remove(boy)
    girls.remove(girl)

print(Marriage)