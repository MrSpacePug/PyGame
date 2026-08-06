import random

playerHP = 30
weaponDMG = 10
mana = 100
playerDEF = 1
playerMHP = 100
cost = 1

enemyHP = 100
enemySTN = 0

action = 0
spell = 0
stunCHN = 0.0





while enemyHP > 0 or playerHP > 0:
    print(f'''YOUR HEALTH: {playerHP}/{playerMHP} | YOUR MANA: {mana}
SLIME: {enemyHP}''')
    action = int(input('''
ATTACK: 1
SPELL: 2
ITEM: 3
RECHARGE: 4
'''))
    if action == 1:
        enemyHP += -1*(weaponDMG * (random.uniform(0.6, 1.2))//1)
    elif action == 2:
        spell = int(input('''
FIREBALL: 1 | COST: 25
ELECTRIC BOLT: 2 | COST: 10
HEAL: 3 | COST: 30
RETURN: 4 
'''))
        if spell == 1 and mana >= 20:
            enemyHP += -1*( 20 * random.uniform(0.4, 1.2)//1)
            mana += -25
        elif spell ==  2 and mana >=  10:
            enemyHP += -1*( 5 * random.uniform(0.6, 1.5)//1 + 2)
            mana += -10 * cost
            stunCHN = random.uniform(0.0, 1.5)
            if stunCHN >= 0.9 and stunCHN < 1.4:
                enemySTN += 2
            elif stunCHN >= 1.4:
                pass
            
        elif spell == 3 and mana >= 30 and playerHP < playerMHP:
            playerHP += ( 10 * random.uniform(0.5, 2)//1)
            mana += -30 * cost
        elif spell == 1 and mana < 20:
            print('''
-- NOT ENOUTH MANA. TURN SKIPED. --
''')
            mana = 0
        elif spell ==  2 and mana <  10:
            print('''
-- NOT ENOUTH MANA. TURN SKIPED. --
''')
            mana = 0
        elif spell == 3 and mana < 30:
            print('''
-- NOT ENOUTH MANA. TURN SKIPED. --
''')
            mana = 0
            


            
            
