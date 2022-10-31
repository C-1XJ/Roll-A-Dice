import random
for x in range(999):
    answer = input("do you want to roll a dice? y/n >>>")
    if answer == "y":
        roll=random.randint(1,6)
        if roll == 1:
            print("""
            [       ]
            [   o   ]
            [       ]""")
        elif roll == 2:
            print("""
            [ o     ]
            [       ]
            [     o ]""")
        elif roll == 3:
            print("""
            [ o     ]
            [   o   ]
            [     o ]""")
        elif roll == 4:
            print("""
            [ o   o ]
            [       ]
            [ o   o ]""")
        elif roll == 5:
            print("""
            [ o   o ]
            [   o   ]
            [ o   o ]""")
        elif roll == 6:
            print("""
            [ o   o ]
            [ o   o ]
            [ o   o ]""")
    else:
        print ("ok")    


