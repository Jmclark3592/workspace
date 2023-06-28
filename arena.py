import random, copy

print('''\tWelcome to the arena''')

npc1 = {'str1' : 8, 'agi' : 6, 'hp' : 28, 'alive' : 1}
npc2 = {'str1' : 4, 'agi' : 9, 'hp' : 32, 'alive' : 1}

player1 = {'str1' : 10, 'agi' : 8, 'hp' : 40}

def comp_attack(char_stats): #function for computer to attack. Each attack adjusts for strength factor (str1)
    attack = random.choice(range(11))
    adjustment = int((char_stats * 0.2) * attack)
    if attack == 0:
        print('NPC misses!')
    else:
        print(f'NPC hits player for {adjustment} HP')
    player1['hp'] = player1['hp'] - adjustment

def player_attack(char_stats, npc): #function for player to attack
    attack = random.choice(range(11))
    adjustment = int((char_stats * 0.2) * attack)
    if attack == 0:
        print('YOU miss!')
    else:
        print(f'You hit player for {adjustment} HP')
    npc['hp'] = npc['hp'] - adjustment

flag = True

def agi_check(stat_c, stat_p): #if computer AGI is greater than player's, flag = False and comp goes first
    if stat_c > stat_p: 
        return flag == False
    else:
        return flag == True

while True:
    if player1['hp'] <= 0:
        print("You have died!")
        break
    
    if npc1['alive'] == 1: #if NPC1 is alive, they check AGI to see who goes first and then battle
        agi_check(npc1['agi'], player1['agi'])
        if flag == False:
            comp_attack(npc1['str1'])
            print(f"Player HP has dropped to {player1['hp']}")
            player_attack(player1['str1'], npc1)
            print(f"Computer HP has dropped to {npc1['hp']}")
            if npc1['hp'] <= 0:
                print("You beat NPC1!")
                npc1['alive'] = 0 #if NPC1 hp goes to 0 flag sets to False and runs back loop down to NPC2
                print("\nNPC2 has entered the arena")
            if player1['hp'] <= 0:
                print("You have died!")
                break
        else: #if player1 AGI is higher then he goes first
            player_attack(player1['str1'], npc1)
            print(f"Computer HP has dropped to {npc1['hp']}") 
            comp_attack(npc1['str1'])
            print(f"Player HP has dropped to {player1['hp']}")
            if npc1['hp'] <= 0:
                print("You beat NPC1!")
                npc1['alive'] = 0 #if NPC1 hp goes to 0 flag sets to False and runs back loop down to NPC2
                print("\nNPC2 has entered the arena")
            if player1['hp'] <= 0:
                print("You have died!")
                break


    elif npc2['alive'] == 1: #After NPC1 dies, player1 hp is reset and we do AGI check to see who goes first for this fight
        player1['hp'] = 40
        agi_check(npc2['agi'], player1['agi'])
        if flag == False:
            comp_attack(npc2['str1'])
            print(f"Player HP has dropped to {player1['hp']}")
            player_attack(player1['str1'], npc2)
            print(f"Computer HP has dropped to {npc2['hp']}")
            if npc2['hp'] <= 0:
                print("You beat NPC1!")
                npc2['alive'] = 0
                break 
            if player1['hp'] <= 0:
                print("You have died!")
                break
        else:
            player_attack(player1['str1'], npc2)
            print(f"Computer HP has dropped to {npc2['hp']}") 
            comp_attack(npc2['str1'])
            print(f"Player HP has dropped to {player1['hp']}")
            if npc2['hp'] <= 0:
                print("You beat NPC1!")
                npc2['alive'] = 0
                print("\nNPC3 has entered the arena")
                break
            if player1['hp'] <= 0:
                print("You have died!")
                break