import random

lvl = random.randint(1,20)

enemyNM = 'NULL'
enemySTR = 0
enemyDEF = 0

enemiesNM = ['Slime', 'Stone Golem', 'Wolf', 'War construct']
colors = ['Red','Yellow','Green','Orange','Purple','None']
currentENEMY = random.randint(0,3)
if currentENEMY == 0:
    enemyNM = enemiesNM[currentENEMY]
    enemySTR = 10
    enemyDEF = 10
    colorWEAK = colors[1]
    colorSTRENGTH = colors[3]

if currentENEMY == 1:
    enemyNM = enemiesNM[currentENEMY]
    enemySTR = 5
    enemyDEF = 15
    colorWEAK = colors[5]
    colorSTRENGTH = colors[5]
if currentENEMY == 2:
    enemyNM = enemiesNM[currentENEMY]
    enemySTR = 15
    enemyDEF = 5
    colorWEAK = colors[4]
    colorSTRENGTH = colors[2]
if currentENEMY == 3:
    enemyNM = enemiesNM[currentENEMY]
    enemySTR = 15
    enemyDEF = 10
    colorWEAK = colors[4]
    colorSTRENGTH = colors[4]

print(f'''Enemy : {enemyNM}
Power : {enemySTR}
Defence : {enemyDEF}
Resist : {colorSTRENGTH}
Weakness : {colorWEAK}
''')


