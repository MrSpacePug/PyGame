import random

playerCHR = 0

playerCHR = int(input('''
Select a Warrior:
1: Knigth | Basic character. Has low spell DMG but high physical DMG.
2: Priest | Follower of the flesh god, has faith based spells and attacks.
3: Ocultist | Spell caster. Focuses on mostly casting spells, but has low defence.

Selection: '''))

if playerCHR == 1:
    manaM = 50
    playerDEF = 2
    weaponDMG = 15
    

playerHP = 100
weaponDMG = 10
mana = 100
manaM = 100
playerDEF = 1
playerMHP = 100
playerHEAL = 0
cost = 1
magicDMG = 1

item1 = 'Small healing potion | Heals a small amount of health'
item2 = 'Small healing potion | Heals a small amount of health'
item3 = 'Large healing potion | Heals a large amount of health'
item4 = 'Large healing potion | Heals a large amount of health'
item5 = 'Small mana potion | Heals a small amount of mana'
item6 = 'Large mana potion | Heals a large amount of mana'
item7 = 'Berserker brew | makes you deal more physical DMG, in exchange for defence'
item8 = 'Sacrificial Dagger | Deals half of your current health in DMG, while making you much stronger. Makes the gods happy'

itemC = 0


enemyHP = 100
enemySTN = 0

action = 0
actionE = 0
enemyATK = 0
spell = 0
stunCHN = 0.0






while enemyHP > 0 or playerHP > 0:
    if playerHP > playerMHP:
        playerHP = playerMHP
    if mana > manaM:
        mana = manaM
    print(f'''
YOUR HEALTH: {playerHP}/{playerMHP} | YOUR MANA: {mana}/{manaM}
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
FIREBALL: 1 | COST: 25 | Red fire magic, does a large amount of DMG
ELECTRIC BOLT: 2 | COST: 10 | Yellow electric magic, does a small amount of DMG but can stun the enemy
HEAL: 3 | COST: 30 | Green nature magic, heals HP
'''))
        if spell == 1 and mana >= 20:
            enemyHP += -1*( 15 * random.uniform(0.8, 1.2)//1) * magicDMG
            mana += -25
        elif spell ==  2 and mana >=  10:
            enemyHP += -1*( 5 * random.uniform(0.6, 1.5)//1 + 2) * magicDMG
            mana += -10 * cost
            stunCHN = random.uniform(0.0, 1.5)
            if stunCHN >= 0.9 and stunCHN < 1.4:
                enemySTN += 2
            elif stunCHN >= 1.4:
                enemySTN += 4
            
        elif spell == 3 and mana >= 30 and playerHP < playerMHP:
            playerHEAL = ( 16 * random.uniform(1, 2)//1)  * magicDMG//2
            print(f'''
You healed {playerHEAL} HP.
''')
            playerHP += playerHEAL
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

    elif action == 3:
        print(f'''Your items are:
1. {item1}
2. {item2}
3. {item3}
4. {item4}
5. {item5}
6. {item6}
7. {item7}
8. {item8}
''')
        itemC = int(input('Chose an item: '))
        if itemC == 1 and item1 != '* EMPTY *':
            playerHP += 15
            print(f'''
The {item1} was used up.
''')
            item1 = '* EMPTY *'
        if itemC == 2 and item2 != '* EMPTY *':
            playerHP += 15
            print(f'''
The {item2} was used up.
''')
            item2 = '* EMPTY *'
        if itemC == 3 and item3 != '* EMPTY *':
            playerHP += 40
            print(f'''
The {item3} was used up.
''')
            item3 = '* EMPTY *'
        if itemC == 4 and item4 != '* EMPTY *':
            playerHP += 40
            print(f'''
The {item4} was used up.
''')
            item4 = '* EMPTY *'
        if itemC == 5 and item5 != '* EMPTY *':
            mana += 15
            print(f'''
The {item5} was used up.
''')
            item5 = '* EMPTY *'
        if itemC == 6 and item6 != '* EMPTY *':
            mana += 30
            print(f'''
The {item6} was used up.
''')
            item6 = '* EMPTY *'
        if itemC == 7 and item7 != '* EMPTY *':
            weaponDMG = weaponDMG * 1.5
            playerDEF -= 2
            print(f'''
The {item7} was used up.
''')
            item7 = '* EMPTY *'
        if itemC == 8 and item8 != '* EMPTY *':
            playerHP -= playerHP//2
            weaponDMG = weaponDMG * 2
            magicDMG = magicDMG * 2
            print(f'''
The dagger pierces your flesh. the gods accept your blood, you feel much stronger.
''')

    elif action == 4:
        mana += random.randint(10,30)
        print('''
You rested and recovered mana.
''')

    #Enemy AI

    actionE = random.randint(1,3)

    if actionE == 1 and enemySTN == 0:
        enemyATK = random.randint(6,14)//playerDEF
        playerHP -= enemyATK
        print(f'''
The Slime headbutted you, dealing {enemyATK} damage.
''')
    elif actionE == 2 and enemySTN == 0:
        enemyATK = random.randint(10,18)//playerDEF
        playerHP -= enemyATK
        print(f'''
The Slime charged at you, dealing {enemyATK} damage.
''')
    elif actionE == 3 and enemySTN == 0:
        enemyATK = random.randint(2,10)
        enemyHP += enemyATK
        print(f'''
The Slime regenerated, healing {enemyATK} health.
''')
    elif enemySTN != 0:
        print(f'''
The Slime was stunned, it's turn was skipped. it's stun will last for {enemySTN -1} more turns.
''')
        enemySTN -= 1



    if playerHP <= 0:
        if mana > manaM:
            mana = manaM
        print(f'''YOUR HEALTH: {playerHP}/{playerMHP} | YOUR MANA: {mana}/{manaM}
SLIME: {enemyHP}''')
        print('''
The gods look down uppon your failure. You have perished and will soon be forgoten.
''')
        break

    if enemyHP <= 0:
        if mana > manaM:
            mana = manaM
        print(f'''YOUR HEALTH: {playerHP}/{playerMHP} | YOUR MANA: {mana}/{manaM}
SLIME: {enemyHP}''')
        print('''
As you deal the final blow to the creature, you feel like the gods are smiling upon you. You have succeded, but the quest continues.
''')
        break

    























