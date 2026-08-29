import random

playerCHR = 0

playerHP = 50
weaponDMG = 5
mana = 50
manaM = 50
playerDEF = 1
playerMHP = 50
playerHEAL = 0
cost = 2
magicDMG = 1
playerFAI = 0
playerNM = 'NAMELESS ONE'
playerLVL = 1
corrupted = True


playerCHR = int(input('''
Select a Warrior:
1: Knigth | Basic character. Has low spell DMG but high physical DMG.
2: Priest | Follower of the flesh god, has faith based spells and attacks.
3: Ocultist | Spell caster. Focuses on mostly casting spells, but has low defence.

Selection: '''))

if playerCHR == 1:
    manaM = 50
    mana = 50
    playerDEF = 1.2
    weaponDMG = 13
    playerMHP = 150
    playerHP = 150
    playerNM = 'KNIGHT'
    playerFAI = 100
    cost = 1
    corrupted = False


if playerCHR == 2:
    playerMHP = 75
    playerHP = 75
    playerFAI = 150
    magicDMG = 1.5
    manaM = 125
    mana = 125
    weaponDMG = 8
    playerNM = 'PRIEST'
    cost = 1
    corrupted = False

if playerCHR == 3:
    playerMHP = 30
    playerHP = 30
    magicDMG = 2
    manaM = 300
    mana = 300
    weaponDMG = 6
    playerDEF = 0.8
    playerNM = 'OCULTIST'
    playerFAI = 100
    cost = 1
    corrupted = False
    


item1 = 'Small healing potion | Heals a small amount of health'
item2 = 'Small healing potion | Heals a small amount of health'
item3 = 'Large healing potion | Heals a large amount of health'
item4 = 'Large healing potion | Heals a large amount of health'
item5 = 'Small mana potion | Heals a small amount of mana'
item6 = 'Large mana potion | Heals a large amount of mana'
item7 = 'Berserker brew | makes you deal more physical DMG, in exchange for defence'
item8 = 'Sacrificial Dagger | Deals half of your current health in DMG, while making you much stronger. Makes the gods happy'

itemC = 0


enemyHP = 250
enemyMHP = 250
enemySTN = 0

action = 0
actionE = 0
enemyATK = 0
spell = 0
stunCHN = 0.0
choiceLVL = 0






while enemyHP > 0 or playerHP > 0:
    if playerHP > playerMHP:
        playerHP = playerMHP
    if mana > manaM:
        mana = manaM
    if enemyHP > enemyMHP:
        enemyHP = enemyMHP
    print(f'''
------------------------------------------------------------------------------------------------------

{playerNM} LVL: {playerLVL}

YOUR HEALTH: {playerHP}/{playerMHP} | YOUR MANA: {mana}/{manaM} | YOUR FAITH: {playerFAI}
GOLEM: {enemyHP}/{enemyMHP}''')
    action = int(input('''
ATTACK: 1
SPELL: 2
ITEM: 3
RECHARGE: 4
'''))
    if action == 1:
        enemyHP += -1*(weaponDMG * (random.uniform(0.6, 1.2))//1)
    elif action == 2 and playerCHR != 3:
        spell = int(input(f'''
FIREBALL: 1 | COST: {25 * cost} | Orange fire magic, does a large amount of DMG
ELECTRIC BOLT: 2 | COST: {10 * cost} | Yellow electric magic, does a small amount of DMG but can stun the enemy
HEAL: 3 | COST: {30 * cost} | Green nature magic, heals HP
'''))
        if spell == 1 and mana >= 20 * cost:
            enemyHP += -1*( 15 * random.uniform(0.8, 1.2)//1) * magicDMG
            mana += -25 * cost
        elif spell ==  2 and mana >=  10 * cost:
            enemyHP += -1*( 5 * random.uniform(0.6, 1.5)//1 + 2) * magicDMG
            mana += -10 * cost
            stunCHN = random.uniform(0.0, 1.5)
            if stunCHN >= 0.9 and stunCHN < 1.4:
                enemySTN += 2
            elif stunCHN >= 1.4:
                enemySTN += 4
            
        elif spell == 3 and mana >= 30 * cost and playerHP < playerMHP:
            playerHEAL = ( 16 * random.uniform(1, 2)//1)  * magicDMG//2
            print(f'''
You healed {playerHEAL} HP.
''')
            playerHP += playerHEAL
            mana += -30 * cost
        elif spell == 1 and mana < 20 * cost:
            print('''
-- NOT ENOUTH MANA. TURN SKIPED. --
''')
            mana = 0
        elif spell ==  2 and mana <  10 * cost:
            print('''
-- NOT ENOUTH MANA. TURN SKIPED. --
''')
            mana = 0
        elif spell == 3 and mana < 30 * cost:
            print('''
-- NOT ENOUTH MANA. TURN SKIPED. --
''')
            mana = 0



    elif action == 2 and playerCHR == 3:
        spell = int(input(f'''
UNHOLY TENTACLES: 1 | COST: {50 * cost} | Purple ocult magic, deals a medium amount of DMG multiple times. Scales with how much mana you have.
BOLT OF LIGTHNING: 2 | COST: {70 * cost} | Yellow electric magic, does a large amount of DMG and may stun the enemy
FLESH RITUAL: 3 | COST: {20* cost} MANA , 10 HP | Red flesh magic, deals self DMG, but increases your magic DMG largely.
HEAL: 4 | COST: {20 * cost} | Green nature magic, heals HP
'''))
        if spell == 1 and mana >= 50:
            spellHT = random.randint(1,4)
            print(f'''
{spellHT} tentacle(s) sprouts from the depths and mauls the creature.
''')
            if corrupted == True:
                for i in range(spellHT):
                    enemyHP += -1*(( 8 * random.uniform(0.8, 1.2)//1) * magicDMG) * ((faith * -1)//10)
            for i in range(spellHT):
                enemyHP += -1*( 8 * random.uniform(0.8, 1.2)//1) * magicDMG
            mana += -50 * cost
            playerFAI -= 200
            if playerFAI <= 0 and corrupted == False:
                print(f'''
The unholy magic of the ocult corrupts you, your sense of self becomes one with the depths and such, the gods abandon you for your sacrilidge.
''')
                playerNM = 'UNHOLY'
                magicDMG += 1
                cost += 1
        elif spell ==  2 and mana >=  70:
            enemyHP += -1*( 18 * random.uniform(0.6, 1.5)//1 + 2) * magicDMG
            mana += -70 * cost
            stunCHN = random.uniform(0.0, 1.5)
            if stunCHN >= 0.9 and stunCHN < 1.4:
                enemySTN += 2
            elif stunCHN >= 1.4:
                enemySTN += 4

        elif spell == 3 and mana >= 20:
            magicDMG = magicDMG * 1.75
            playerHP -= 10
            mana -= 20 * cost
            
        elif spell == 4 and mana >= 30 and playerHP < playerMHP:
            playerHEAL = ( 16 * random.uniform(1, 2)//1)  * magicDMG//2
            print(f'''
You healed {playerHEAL} HP.
''')
            playerHP += playerHEAL
            mana += -30 * cost

            
        elif spell == 1 and mana < 50 * cost:
            print('''
-- NOT ENOUTH MANA. TURN SKIPED. --
''')
            mana = 0
        elif spell ==  2 and mana <  70 * cost:
            print('''
-- NOT ENOUTH MANA. TURN SKIPED. --
''')
            mana = 0
        elif spell == 3 and mana < 20 * cost:
            print('''
-- NOT ENOUTH MANA. TURN SKIPED. --
''')
            mana = 0

        elif spell == 4 and mana < 20 * cost:
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
            playerDEF = playerDEF * 0.5
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

    elif action == 4 and playerCHR != 3:
        mana += random.randint(10,30)
        print('''
You rested and recovered mana.
''')

    elif action == 4 and playerCHR == 3:
        mana += random.randint(30,70)
        print('''
You rested and recovered alot of mana.
''')

    #Enemy AI

    actionE = random.randint(1,3)

    if actionE == 1 and enemySTN == 0:
        enemyATK = random.randint(6,18)//playerDEF
        playerHP -= enemyATK
        print(f'''
The Golem headbutted you, dealing {enemyATK} damage.
''')
    elif actionE == 2 and enemySTN == 0:
        enemyATK = random.randint(12,24)//playerDEF
        playerHP -= enemyATK
        print(f'''
The Golem slamed its fists on you, dealing {enemyATK} damage.
''')
    elif actionE == 3 and enemySTN == 0:
        enemyATK = random.randint(6,14)
        enemyHP += enemyATK
        print(f'''
The Golem rebuilt itself, healing {enemyATK} health.
''')
    elif enemySTN != 0:
        print(f'''
The Slime was stunned, it's turn was skipped. it's stun will last for {enemySTN -1} more turns.
''')
        enemySTN -= 1



    if playerHP <= 0:
        if mana > manaM:
            mana = manaM
        print(f'''
------------------------------------------------------------------------------------------------------

{playerNM} LVL: {playerLVL}

YOUR HEALTH: {playerHP}/{playerMHP} | YOUR MANA: {mana}/{manaM} | YOUR FAITH: {playerFAI}
GOLEM: {enemyHP}''')
        print('''
The gods look down uppon your failure. You have perished and will soon be forgoten.
''')
        break

    if enemyHP <= 0 and corrupted == False:
        playerLVL += 1
        if mana > manaM:
            mana = manaM
        print(f'''
------------------------------------------------------------------------------------------------------

{playerNM} LVL: {playerLVL}

YOUR HEALTH: {playerHP}/{playerMHP} | YOUR MANA: {mana}/{manaM} | YOUR FAITH: {playerFAI}
GOLEM: {enemyHP}''')
        print('''
As you deal the final blow to the creature, you feel like the gods are smiling upon you. You have succeded, but the quest continues.
''')

    elif enemyHP <= 0 and corrupted == True:
        playerLVL += 1
        if mana > manaM:
            mana = manaM
        print(f'''
------------------------------------------------------------------------------------------------------

{playerNM} LVL: {playerLVL}

YOUR HEALTH: {playerHP}/{playerMHP} | YOUR MANA: {mana}/{manaM} | YOUR FAITH: {playerFAI}
GOLEM: {enemyHP}''')
        print('''
As you deal the final blow to the creature, you feel the abyss in your soul expand. You have succeded, but the quest continues.
''')
        
        choiceLVL = int(input(f'''
--- CHOSE A LEVEL UP REWARD ---

1: MAX HP UP
2: MAX MANA UP
3: WEAPON UPGRADE
4: RANDOM PASSIVE ITEM

--------------------------------
'''))
        if choiceLVL == 1:
            playerMHP += 30 * playerLVL
        elif choiceLVL == 2:
            manaM += 50 * playerLVL
        elif choiceLVL == 3:
            weaponDMG += random.randint(2,4)* playerLVL
        elif choiceLVL == 4:
            























