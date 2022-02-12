import random
#global dif, genError, difLevels, username, inputs, debug (COPY THIS BIT AT THE BEGINNING OF EACH FUNCTION)
username = "Player"
dif = 1
genError = "Didn't catch that. Check your response and try again."
difLevels = [1,2,3]
inputs = "abcdef"
debug = False

def capCheck(val, spaces):
    global dif, genError, difLevels, username, inputs, debug
    board = []
    board.append(spaces[0])
    board.append(spaces[1])
    board.append(spaces[2])
    board.append(spaces[3])
    board.append(spaces[4])
    board.append(spaces[5])
    board.append(spaces[6])
    board.append(spaces[7])
    board.append(spaces[8])
    board.append(spaces[9])
    board.append(spaces[10])
    board.append(spaces[11])
    board.append(spaces[12])
    board.append(spaces[13])
    if val == 12:
        if board[12] <= 0:
            return False
        handStart = 12
        handVal = board[12]
        board[12] = 0
        i=0
        chk = False
        chk2 = False
        chk3 = False
        while chk == False:
            for i in range(handVal):
                if i > 0 and chk2 == False:
                    handStart = -1
                    chk2 = True
                    break
                elif i >= 6  and chk2 == True and chk3 == False:
                    handStart = 6
                    chk3 = True
                    break
                elif i >= 7 and chk3 == True:
                    handStart = -1
                    chk3 = False
                    break
                elif chk == True:
                    break
                else:
                    moves = i+1
                    handLoc = handStart+moves
                    board[handLoc] += 1
                    handVal -= 1
                    if handVal == 0:
                        chk = True
        endVal = handLoc
        if endVal == 7 and board[7] == 1 and board[5] != 0:
            board[13] += board[7] + board[5]
            board[7] = 0
            board[5] = 0
            return True
        elif endVal == 8 and board[8] == 1 and board[4] != 0:
            board[13] += board[8] + board[4]
            board[8] = 0
            board[4] = 0
            return True
        elif endVal == 9 and board[9] == 1 and board[3] != 0:
            board[13] += board[9] + board[3]
            board[9] = 0
            board[3] = 0
            return True
        elif endVal == 10 and board[10] == 1 and board[2] != 0:
            board[13] += board[10] + board[2]
            board[10] = 0
            board[2] = 0
            return True
        elif endVal == 11 and board[11] == 1 and board[1] != 0:
            board[13] += board[11] + board[1]
            board[11] = 0
            board[1] = 0
            return True
        elif endVal == 12 and board[12] == 1 and board[0] != 0:
            board[13] += board[12] + board[0]
            board[12] = 0
            board[0] = 0
            return True
        else:
            return False
    elif val == 11:
        if board[11] <= 0:
            return False
        handStart = 11
        handVal = board[11]
        board[11] = 0
        i=0
        chk = False
        chk2 = False
        chk3 = False
        while chk == False:
            for i in range(handVal):
                if i > 1 and chk2 == False:
                    handStart = -1
                    chk2 = True
                    break
                elif i >= 6  and chk2 == True and chk3 == False:
                    handStart = 6
                    chk3 = True
                    break
                elif i >= 7 and chk3 == True:
                    handStart = -1
                    chk3 = False
                    break
                elif chk == True:
                    break
                else:
                    moves = i+1
                    handLoc = handStart+moves
                    board[handLoc] += 1
                    handVal -= 1
                if handVal == 0:
                        chk = True
        endVal = handLoc
        if endVal == 7 and board[7] == 1 and board[5] != 0:
            board[13] += board[7] + board[5]
            board[7] = 0
            board[5] = 0
            return True
        elif endVal == 8 and board[8] == 1 and board[4] != 0:
            board[13] += board[8] + board[4]
            board[8] = 0
            board[4] = 0
            return True
        elif endVal == 9 and board[9] == 1 and board[3] != 0:
            board[13] += board[9] + board[3]
            board[9] = 0
            board[3] = 0
            return True
        elif endVal == 10 and board[10] == 1 and board[2] != 0:
            board[13] += board[10] + board[2]
            board[10] = 0
            board[2] = 0
            return True
        elif endVal == 11 and board[11] == 1 and board[1] != 0:
            board[13] += board[11] + board[1]
            board[11] = 0
            board[1] = 0
            return True
        elif endVal == 12 and board[12] == 1 and board[0] != 0:
            board[13] += board[12] + board[0]
            board[12] = 0
            board[0] = 0
            return True
        else:
            return False
    elif val == 10:
        if board[10] <= 0:
            return False
        handStart = 10
        handVal = board[10]
        board[10] = 0
        i=0
        chk = False
        chk2 = False
        chk3 = False
        while chk == False:
            for i in range(handVal):
                if i > 2 and chk2 == False:
                    handStart = -1
                    chk2 = True
                    break
                elif i >= 6  and chk2 == True and chk3 == False:
                    handStart = 6
                    chk3 = True
                    break
                elif i >= 7 and chk3 == True:
                    handStart = -1
                    chk3 = False
                    break
                elif chk == True:
                    break
                else:
                    moves = i+1
                    handLoc = handStart+moves
                    board[handLoc] += 1
                    handVal -= 1
                    if handVal == 0:
                        chk = True
        endVal = handLoc
        if endVal == 7 and board[7] == 1 and board[5] != 0:
            board[13] += board[7] + board[5]
            board[7] = 0
            board[5] = 0
            return True
        elif endVal == 8 and board[8] == 1 and board[4] != 0:
            board[13] += board[8] + board[4]
            board[8] = 0
            board[4] = 0
            return True
        elif endVal == 9 and board[9] == 1 and board[3] != 0:
            board[13] += board[9] + board[3]
            board[9] = 0
            board[3] = 0
            return True
        elif endVal == 10 and board[10] == 1 and board[2] != 0:
            board[13] += board[10] + board[2]
            board[10] = 0
            board[2] = 0
            return True
        elif endVal == 11 and board[11] == 1 and board[1] != 0:
            board[13] += board[11] + board[1]
            board[11] = 0
            board[1] = 0
            return True
        elif endVal == 12 and board[12] == 1 and board[0] != 0:
            board[13] += board[12] + board[0]
            board[12] = 0
            board[0] = 0
            return True
    elif val == 9:
        if board[9] <= 0:
            return False
        handStart = 9
        handVal = board[9]
        board[9] = 0
        i=0
        chk = False
        chk2 = False
        chk3 = False
        while chk == False:
            for i in range(handVal):
                if i > 3 and chk2 == False:
                    handStart = -1
                    chk2 = True
                    break
                elif i >= 6  and chk2 == True and chk3 == False:
                    handStart = 6
                    chk3 = True
                    break
                elif i >= 7 and chk3 == True:
                    handStart = -1
                    chk3 = False
                    break
                elif chk == True:
                    break
                else:
                    moves = i+1
                    handLoc = handStart+moves
                    board[handLoc] += 1
                    handVal -= 1
                    if handVal == 0:
                        chk = True
        endVal = handLoc
        if endVal == 7 and board[7] == 1 and board[5] != 0:
            board[13] += board[7] + board[5]
            board[7] = 0
            board[5] = 0
            return True
        elif endVal == 8 and board[8] == 1 and board[4] != 0:
            board[13] += board[8] + board[4]
            board[8] = 0
            board[4] = 0
            return True
        elif endVal == 9 and board[9] == 1 and board[3] != 0:
            board[13] += board[9] + board[3]
            board[9] = 0
            board[3] = 0
            return True
        elif endVal == 10 and board[10] == 1 and board[2] != 0:
            board[13] += board[10] + board[2]
            board[10] = 0
            board[2] = 0
            return True
        elif endVal == 11 and board[11] == 1 and board[1] != 0:
            board[13] += board[11] + board[1]
            board[11] = 0
            board[1] = 0
            return True
        elif endVal == 12 and board[12] == 1 and board[0] != 0:
            board[13] += board[12] + board[0]
            board[12] = 0
            board[0] = 0
            return True
        else:
            return False
    elif val == 8:
        if board[8] <= 0:
            return False
        handStart = 8
        handVal = board[8]
        board[8] = 0
        i=0
        chk = False
        chk2 = False
        chk3 = False
        while chk == False:
            for i in range(handVal):
                if i > 4 and chk2 == False:
                    handStart = -1
                    chk2 = True
                    break
                elif i >= 6  and chk2 == True and chk3 == False:
                    handStart = 6
                    chk3 = True
                    break
                elif i >= 7 and chk3 == True:
                    handStart = -1
                    chk3 = False
                    break
                elif chk == True:
                    break
                else:
                    moves = i+1
                    handLoc = handStart+moves
                    board[handLoc] += 1
                    handVal -= 1
                    if handVal == 0:
                        chk = True
        endVal = handLoc
        if endVal == 7 and board[7] == 1 and board[5] != 0:
            board[13] += board[7] + board[5]
            board[7] = 0
            board[5] = 0
            return True
        elif endVal == 8 and board[8] == 1 and board[4] != 0:
            board[13] += board[8] + board[4]
            board[8] = 0
            board[4] = 0
            return True
        elif endVal == 9 and board[9] == 1 and board[3] != 0:
            board[13] += board[9] + board[3]
            board[9] = 0
            board[3] = 0
            return True
        elif endVal == 10 and board[10] == 1 and board[2] != 0:
            board[13] += board[10] + board[2]
            board[10] = 0
            board[2] = 0
            return True
        elif endVal == 11 and board[11] == 1 and board[1] != 0:
            board[13] += board[11] + board[1]
            board[11] = 0
            board[1] = 0
            return True
        elif endVal == 12 and board[12] == 1 and board[0] != 0:
            board[13] += board[12] + board[0]
            board[12] = 0
            board[0] = 0
            return True
        else:
            return False
    if val == 7:
        if board[7] <= 0:
            return False
        handStart = 7
        handVal = board[7]
        board[7] = 0
        i=0
        chk = False
        chk2 = False
        chk3 = False
        while chk == False:
            for i in range(handVal):
                if i > 5 and chk2 == False:
                    handStart = -1
                    chk2 = True
                    break
                elif i >= 6  and chk2 == True and chk3 == False:
                    handStart = 6
                    chk3 = True
                    break
                elif i >= 7 and chk3 == True:
                    handStart = -1
                    chk3 = False
                    break
                elif chk == True:
                    break
                else:
                    moves = i+1
                    handLoc = handStart+moves
                    board[handLoc] += 1
                    handVal -= 1
                    if handVal == 0:
                        chk = True
        endVal = handLoc
        if endVal == 7 and board[7] == 1 and board[5] != 0:
            board[13] += board[7] + board[5]
            board[7] = 0
            board[5] = 0
            return True
        elif endVal == 8 and board[8] == 1 and board[4] != 0:
            board[13] += board[8] + board[4]
            board[8] = 0
            board[4] = 0
            return True
        elif endVal == 9 and board[9] == 1 and board[3] != 0:
            board[13] += board[9] + board[3]
            board[9] = 0
            board[3] = 0
            return True
        elif endVal == 10 and board[10] == 1 and board[2] != 0:
            board[13] += board[10] + board[2]
            board[10] = 0
            board[2] = 0
            return True
        elif endVal == 11 and board[11] == 1 and board[1] != 0:
            board[13] += board[11] + board[1]
            board[11] = 0
            board[1] = 0
            return True
        elif endVal == 12 and board[12] == 1 and board[0] != 0:
            board[13] += board[12] + board[0]
            board[12] = 0
            board[0] = 0
            return True
        else:
            return False
    else:
        return False


def mancala():
    global dif, genError, difLevels, username, inputs, debug
    turn1 = True
    if dif not in difLevels:
        dif = 1
    handLoc = 0
    printChk = False
    play = True
    posTraitsBack=["fearsome","honorable","mighty","awesome","coolest mancala player around,","person who still owes me $5,","cuddly","adorable","kinda cute ngl (//o/w/o)","hopefully good at this game","licensed mancala master,","person that is going to buy a tote bag from the gift shop on their way out,"]
    posTraits=["fearsome","honorable","mighty","awesome","coolest mancala player around,","person who still owes me $5,","cuddly","adorable","kinda cute ngl (//o/w/o)","hopefully good at this game","licensed mancala master,","person that is going to buy a tote bag from the gift shop on their way out,"]
    trait = posTraits[random.randint(0,len(posTraits)-1)]
    print("\n\nTime for the main event... Mancala!\n")
    print(f"In one corner, the {trait} CPU1!\n")
    posTraits.remove(trait)
    trait2 = posTraits[random.randint(0,len(posTraits)-1)]
    print(f"And in the other corner, the {trait2} {username}!\n")
    posTraits = posTraitsBack
    ruleOpt=""
    while ruleOpt != "y" and ruleOpt != "n":
        ruleOpt=input(f"\n\nHey, uh, {username}, you want me to explain the rules? (y or n)\n")
        if ruleOpt == "n":
            print("\nYou know what to do? Alright then. Go get \'em, tiger!\n")
        elif ruleOpt == "y":
            print("\nOk. Here's the aim of the game.\n")
            print("The board has 14 spaces, each of which can hold stones represented by the number in each space.\n")
            print("The big one on the far right makes up your points, and the big one on the far left makes up your opponent\'s.\n")
            print("Your goal is to move as many stones as you can to your point space. Whoever has the most at the end wins.\n")
            print("When it\'s your turn, you can pick up all the stones in any of the spaces on your side (the bottom side) and move them.\n")
            print("You move counterclockwise one space at a time, dropping off a stone in each space you pass, except for your opponent\'s point space, which you skip over.\n")
            print("When you run out of stones, that\'s the end of your turn.\n")
            print("After your turn is up, your opponent gets to move the stones on their side.\n")
            print("Additionally, there are two special moves you can do if you end your turn on the right space.\n")
            print("If you end your turn by dropping a stone in your point space, you get to move another pile of stones.\n")
            print("If you end your turn by dropping a stone into an empty space on your side (the bottom side),\nall of the stones from the space opposite from it on your opponent\'s side get added to your point space.\n")
            print("The game ends when all of the spaces on either side are empty. Good luck, and have fun! :D\n\n")
        else:
            print(genError)
    print("NOTE: MANCALA UI MAY APPEAR STRANGE IF YOUR WINDOW IS NOT LARGE ENOUGH. MAXIMIZE WINDOW FOR BEST EXPERIENCE.\n")
    print("ps - it will also become slightly deformed if space values exceed 2 digits. This is normal, do not worry.\n\n")
    spaceVal=[4,4,4,4,4,4,0,4,4,4,4,4,4,0]
    if dif == 4:
        spaceVal[13] += 2
    if dif == 3 or dif == 4:
        playerTurn = False
    else:
        playerTurn = True
    while play == True:
        while playerTurn != False:
            print(f"    CPU1                                                                                                                    {username}\n   Points                                                                                                                   Points\n_________________________________________________________________________________________________________________________________________\n|                |                |                |                |                |                |                |                |\n|                |                |                |                |                |                |                |                |\n|                |       {spaceVal[12]}        |       {spaceVal[11]}        |       {spaceVal[10]}        |       {spaceVal[9]}        |       {spaceVal[8]}        |       {spaceVal[7]}        |                |\n|                |                |                |                |                |                |                |                |\n|       {spaceVal[13]}        |_____________________________________________________________________________________________________|       {spaceVal[6]}        |\n|                |                |                |                |                |                |                |                |\n|                |                |                |                |                |                |                |                |\n|                |       {spaceVal[0]}        |       {spaceVal[1]}        |       {spaceVal[2]}        |       {spaceVal[3]}        |       {spaceVal[4]}        |       {spaceVal[5]}        |                |\n|                |                |                |                |                |                |                |                |\n|                |                |                |                |                |                |                |                |\n_________________________________________________________________________________________________________________________________________\n                      Space A          Space B          Space C          Space D          Space E          Space F\n")
            playerInp="this is a long and boring string which I hope is not in any dictionary"
            while playerInp not in inputs:
                playerInp = str(input("Enter letters A through F to move stones from that space.\n")).lower()
                if playerInp == "a":
                    if spaceVal[0] <= 0:
                        print("\nThat space has no stones.\n")
                        break
                    print(f"\n{username} moves from space A\n")
                    handStart = 0
                    handVal = spaceVal[0]
                    spaceVal[0] = 0
                    i=0
                    chk = False
                    chk2 = False
                    while chk == False:
                        for i in range(handVal):
                            if i >= 12:
                                handStart = -1
                                break
                            elif chk == True:
                                break
                            else:
                                moves = i+1
                                handLoc = handStart+moves
                                spaceVal[handLoc] += 1
                                handVal -= 1
                                if handVal == 0:
                                    chk = True
                    endVal = handLoc
                    if endVal == 0 and spaceVal[0] == 1 and spaceVal[12] != 0:
                        print(f"\n{username} captures {spaceVal[12]} stones from space A!\n")
                        spaceVal[6] += spaceVal[0] + spaceVal[12]
                        spaceVal[0] = 0
                        spaceVal[12] = 0
                    elif endVal == 1 and spaceVal[1] == 1 and spaceVal[11] != 0:
                        print(f"\n{username} captures {spaceVal[11]} stones from space B!\n")
                        spaceVal[6] += spaceVal[1] + spaceVal[11]
                        spaceVal[1] = 0
                        spaceVal[11] = 0
                    elif endVal == 2 and spaceVal[2] == 1 and spaceVal[10] != 0:
                        print(f"\n{username} captures {spaceVal[10]} stones from space C!\n")
                        spaceVal[6] += spaceVal[2] + spaceVal[10]
                        spaceVal[2] = 0
                        spaceVal[10] = 0
                    elif endVal == 3 and spaceVal[3] == 1 and spaceVal[9] != 0:
                        print(f"\n{username} captures {spaceVal[9]} stones from space D!\n")
                        spaceVal[6] += spaceVal[3] + spaceVal[9]
                        spaceVal[3] = 0
                        spaceVal[9] = 0
                    elif endVal == 4 and spaceVal[4] == 1 and spaceVal[8] != 0:
                        print(f"\n{username} captures {spaceVal[8]} stones from space E!\n")
                        spaceVal[6] += spaceVal[4] + spaceVal[8]
                        spaceVal[4] = 0
                        spaceVal[8] = 0
                    elif endVal == 5 and spaceVal[5] == 1 and spaceVal[7] != 0:
                        print(f"\n{username} captures {spaceVal[7]} stones from space F!\n")
                        spaceVal[6] += spaceVal[5] + spaceVal[7]
                        spaceVal[5] = 0
                        spaceVal[7] = 0
                    if endVal != 6:
                        playerTurn = False
                    elif endVal == 6:
                        print(f"\n{username} gets an extra turn!\n")
                elif playerInp == "b":
                    if spaceVal[1] <= 0:
                        print("\nThat space has no stones.\n")
                        break
                    print(f"\n{username} moves from space B\n")
                    handStart = 1
                    handVal = spaceVal[1]
                    spaceVal[1] = 0
                    i=0
                    chk = False
                    chk2 = False
                    while chk == False:
                        for i in range(handVal):
                            if i >= 11 and chk2 == False:
                                handStart = -1
                                chk2 = True
                                break
                            elif i >=12 and chk2 == True:
                                handStart = -1
                                break
                            elif chk == True:
                                break
                            else:
                                moves = i+1
                                handLoc = handStart+moves
                                spaceVal[handLoc] += 1
                                handVal -= 1
                                if handVal == 0:
                                    chk = True
                    endVal = handLoc
                    if endVal == 0 and spaceVal[0] == 1 and spaceVal[12] != 0:
                        print(f"\n{username} captures {spaceVal[12]} stones from space A!\n")
                        spaceVal[6] += spaceVal[0] + spaceVal[12]
                        spaceVal[0] = 0
                        spaceVal[12] = 0
                    elif endVal == 1 and spaceVal[1] == 1 and spaceVal[11] != 0:
                        print(f"\n{username} captures {spaceVal[11]} stones from space B!\n")
                        spaceVal[6] += spaceVal[1] + spaceVal[11]
                        spaceVal[1] = 0
                        spaceVal[11] = 0
                    elif endVal == 2 and spaceVal[2] == 1 and spaceVal[10] != 0:
                        print(f"\n{username} captures {spaceVal[10]} stones from space C!\n")
                        spaceVal[6] += spaceVal[2] + spaceVal[10]
                        spaceVal[2] = 0
                        spaceVal[10] = 0
                    elif endVal == 3 and spaceVal[3] == 1 and spaceVal[9] != 0:
                        print(f"\n{username} captures {spaceVal[9]} stones from space D!\n")
                        spaceVal[6] += spaceVal[3] + spaceVal[9]
                        spaceVal[3] = 0
                        spaceVal[9] = 0
                    elif endVal == 4 and spaceVal[4] == 1 and spaceVal[8] != 0:
                        print(f"\n{username} captures {spaceVal[8]} stones from space E!\n")
                        spaceVal[6] += spaceVal[4] + spaceVal[8]
                        spaceVal[4] = 0
                        spaceVal[8] = 0
                    elif endVal == 5 and spaceVal[5] == 1 and spaceVal[7] != 0:
                        print(f"\n{username} captures {spaceVal[7]} stones from space F!\n")
                        spaceVal[6] += spaceVal[5] + spaceVal[7]
                        spaceVal[5] = 0
                        spaceVal[7] = 0
                    if endVal != 6:
                        playerTurn = False
                    elif endVal == 6:
                        print(f"\n{username} gets an extra turn!\n")
                elif playerInp == "c":
                    if spaceVal[2] <= 0:
                        print("\nThat space has no stones.\n")
                        break
                    print(f"\n{username} moves from space C\n")
                    handStart = 2
                    handVal = spaceVal[2]
                    spaceVal[2] = 0
                    i=0
                    chk = False
                    chk2 = False
                    while chk == False:
                        for i in range(handVal):
                            if i >= 10 and chk2 == False:
                                handStart = -1
                                chk2 = True
                                break
                            elif i >=12 and chk2 == True:
                                handStart = -1
                                break
                            elif chk == True:
                                break
                            else:
                                moves = i+1
                                handLoc = handStart+moves
                                spaceVal[handLoc] += 1
                                handVal -= 1
                                if handVal == 0:
                                    chk = True
                    endVal = handLoc
                    if endVal == 0 and spaceVal[0] == 1 and spaceVal[12] != 0:
                        print(f"\n{username} captures {spaceVal[12]} stones from space A!\n")
                        spaceVal[6] += spaceVal[0] + spaceVal[12]
                        spaceVal[0] = 0
                        spaceVal[12] = 0
                    elif endVal == 1 and spaceVal[1] == 1 and spaceVal[11] != 0:
                        print(f"\n{username} captures {spaceVal[11]} stones from space B!\n")
                        spaceVal[6] += spaceVal[1] + spaceVal[11]
                        spaceVal[1] = 0
                        spaceVal[11] = 0
                    elif endVal == 2 and spaceVal[2] == 1 and spaceVal[10] != 0:
                        print(f"\n{username} captures {spaceVal[10]} stones from space C!\n")
                        spaceVal[6] += spaceVal[2] + spaceVal[10]
                        spaceVal[2] = 0
                        spaceVal[10] = 0
                    elif endVal == 3 and spaceVal[3] == 1 and spaceVal[9] != 0:
                        print(f"\n{username} captures {spaceVal[9]} stones from space D!\n")
                        spaceVal[6] += spaceVal[3] + spaceVal[9]
                        spaceVal[3] = 0
                        spaceVal[9] = 0
                    elif endVal == 4 and spaceVal[4] == 1 and spaceVal[8] != 0:
                        print(f"\n{username} captures {spaceVal[8]} stones from space E!\n")
                        spaceVal[6] += spaceVal[4] + spaceVal[8]
                        spaceVal[4] = 0
                        spaceVal[8] = 0
                    elif endVal == 5 and spaceVal[5] == 1 and spaceVal[7] != 0:
                        print(f"\n{username} captures {spaceVal[7]} stones from space F!\n")
                        spaceVal[6] += spaceVal[5] + spaceVal[7]
                        spaceVal[5] = 0
                        spaceVal[7] = 0
                    if endVal != 6:
                        playerTurn = False
                    elif endVal == 6:
                        print(f"\n{username} gets an extra turn!\n")
                elif playerInp == "d":
                    if spaceVal[3] <= 0:
                        print("\nThat space has no stones.\n")
                        break
                    print(f"\n{username} moves from space D\n")
                    handStart = 3
                    handVal = spaceVal[3]
                    spaceVal[3] = 0
                    i=0
                    chk = False
                    chk2 = False
                    while chk == False:
                        for i in range(handVal):
                            if i >= 9 and chk2 == False:
                                handStart = -1
                                chk2 = True
                                break
                            elif i >=12 and chk2 == True:
                                handStart = -1
                                break
                            elif chk == True:
                                break
                            else:
                                moves = i+1
                                handLoc = handStart+moves
                                spaceVal[handLoc] += 1
                                handVal -= 1
                                if handVal == 0:
                                    chk = True
                    endVal = handLoc
                    if endVal == 0 and spaceVal[0] == 1 and spaceVal[12] != 0:
                        print(f"\n{username} captures {spaceVal[12]} stones from space A!\n")
                        spaceVal[6] += spaceVal[0] + spaceVal[12]
                        spaceVal[0] = 0
                        spaceVal[12] = 0
                    elif endVal == 1 and spaceVal[1] == 1 and spaceVal[11] != 0:
                        print(f"\n{username} captures {spaceVal[11]} stones from space B!\n")
                        spaceVal[6] += spaceVal[1] + spaceVal[11]
                        spaceVal[1] = 0
                        spaceVal[11] = 0
                    elif endVal == 2 and spaceVal[2] == 1 and spaceVal[10] != 0:
                        print(f"\n{username} captures {spaceVal[10]} stones from space C!\n")
                        spaceVal[6] += spaceVal[2] + spaceVal[10]
                        spaceVal[2] = 0
                        spaceVal[10] = 0
                    elif endVal == 3 and spaceVal[3] == 1 and spaceVal[9] != 0:
                        print(f"\n{username} captures {spaceVal[9]} stones from space D!\n")
                        spaceVal[6] += spaceVal[3] + spaceVal[9]
                        spaceVal[3] = 0
                        spaceVal[9] = 0
                    elif endVal == 4 and spaceVal[4] == 1 and spaceVal[8] != 0:
                        print(f"\n{username} captures {spaceVal[8]} stones from space E!\n")
                        spaceVal[6] += spaceVal[4] + spaceVal[8]
                        spaceVal[4] = 0
                        spaceVal[8] = 0
                    elif endVal == 5 and spaceVal[5] == 1 and spaceVal[7] != 0:
                        print(f"\n{username} captures {spaceVal[7]} stones from space F!\n")
                        spaceVal[6] += spaceVal[5] + spaceVal[7]
                        spaceVal[5] = 0
                        spaceVal[7] = 0
                    if endVal != 6:
                        playerTurn = False
                    elif endVal == 6:
                        print(f"\n{username} gets an extra turn!\n")
                elif playerInp == "e":
                    if spaceVal[4] <= 0:
                        print("\nThat space has no stones.\n")
                        break
                    print(f"\n{username} moves from space E\n")
                    handStart = 4
                    handVal = spaceVal[4]
                    spaceVal[4] = 0
                    i=0
                    chk = False
                    chk2 = False
                    while chk == False:
                        for i in range(handVal):
                            if i >= 8 and chk2 == False:
                                handStart = -1
                                chk2 = True
                                break
                            elif i >=12 and chk2 == True:
                                handStart = -1
                                break
                            elif chk == True:
                                break
                            else:
                                moves = i+1
                                handLoc = handStart+moves
                                spaceVal[handLoc] += 1
                                handVal -= 1
                                if handVal == 0:
                                    chk = True
                    endVal = handLoc
                    if endVal == 0 and spaceVal[0] == 1 and spaceVal[12] != 0:
                        print(f"\n{username} captures {spaceVal[12]} stones from space A!\n")
                        spaceVal[6] += spaceVal[0] + spaceVal[12]
                        spaceVal[0] = 0
                        spaceVal[12] = 0
                    elif endVal == 1 and spaceVal[1] == 1 and spaceVal[11] != 0:
                        print(f"\n{username} captures {spaceVal[11]} stones from space B!\n")
                        spaceVal[6] += spaceVal[1] + spaceVal[11]
                        spaceVal[1] = 0
                        spaceVal[11] = 0
                    elif endVal == 2 and spaceVal[2] == 1 and spaceVal[10] != 0:
                        print(f"\n{username} captures {spaceVal[10]} stones from space C!\n")
                        spaceVal[6] += spaceVal[2] + spaceVal[10]
                        spaceVal[2] = 0
                        spaceVal[10] = 0
                    elif endVal == 3 and spaceVal[3] == 1 and spaceVal[9] != 0:
                        print(f"\n{username} captures {spaceVal[9]} stones from space D!\n")
                        spaceVal[6] += spaceVal[3] + spaceVal[9]
                        spaceVal[3] = 0
                        spaceVal[9] = 0
                    elif endVal == 4 and spaceVal[4] == 1 and spaceVal[8] != 0:
                        print(f"\n{username} captures {spaceVal[8]} stones from space E!\n")
                        spaceVal[6] += spaceVal[4] + spaceVal[8]
                        spaceVal[4] = 0
                        spaceVal[8] = 0
                    elif endVal == 5 and spaceVal[5] == 1 and spaceVal[7] != 0:
                        print(f"\n{username} captures {spaceVal[7]} stones from space F!\n")
                        spaceVal[6] += spaceVal[5] + spaceVal[7]
                        spaceVal[5] = 0
                        spaceVal[7] = 0
                    if endVal != 6:
                        playerTurn = False
                    elif endVal == 6:
                        print(f"\n{username} gets an extra turn!\n")
                elif playerInp == "f":
                    if spaceVal[5] <= 0:
                        print("\nThat space has no stones.\n")
                        break
                    print(f"\n{username} moves from space F\n")
                    handStart = 5
                    handVal = spaceVal[5]
                    spaceVal[5] = 0
                    i=0
                    chk = False
                    chk2 = False
                    while chk == False:
                        for i in range(handVal):
                            if i >= 7 and chk2 == False:
                                handStart = -1
                                chk2 = True
                                break
                            elif i >=12 and chk2 == True:
                                handStart = -1
                                break
                            elif chk == True:
                                break
                            else:
                                moves = i+1
                                handLoc = handStart+moves
                                spaceVal[handLoc] += 1
                                handVal -= 1
                                if handVal == 0:
                                    chk = True
                    endVal = handLoc
                    if endVal == 0 and spaceVal[0] == 1 and spaceVal[12] != 0:
                        print(f"\n{username} captures {spaceVal[12]} stones from space A!\n")
                        spaceVal[6] += spaceVal[0] + spaceVal[12]
                        spaceVal[0] = 0
                        spaceVal[12] = 0
                    elif endVal == 1 and spaceVal[1] == 1 and spaceVal[11] != 0:
                        print(f"\n{username} captures {spaceVal[11]} stones from space B!\n")
                        spaceVal[6] += spaceVal[1] + spaceVal[11]
                        spaceVal[1] = 0
                        spaceVal[11] = 0
                    elif endVal == 2 and spaceVal[2] == 1 and spaceVal[10] != 0:
                        print(f"\n{username} captures {spaceVal[10]} stones from space C!\n")
                        spaceVal[6] += spaceVal[2] + spaceVal[10]
                        spaceVal[2] = 0
                        spaceVal[10] = 0
                    elif endVal == 3 and spaceVal[3] == 1 and spaceVal[9] != 0:
                        print(f"\n{username} captures {spaceVal[9]} stones from space D!\n")
                        spaceVal[6] += spaceVal[3] + spaceVal[9]
                        spaceVal[3] = 0
                        spaceVal[9] = 0
                    elif endVal == 4 and spaceVal[4] == 1 and spaceVal[8] != 0:
                        print(f"\n{username} captures {spaceVal[8]} stones from space E!\n")
                        spaceVal[6] += spaceVal[4] + spaceVal[8]
                        spaceVal[4] = 0
                        spaceVal[8] = 0
                    elif endVal == 5 and spaceVal[5] == 1 and spaceVal[7] != 0:
                        print(f"\n{username} captures {spaceVal[7]} stones from space F!\n")
                        spaceVal[6] += spaceVal[5] + spaceVal[7]
                        spaceVal[5] = 0
                        spaceVal[7] = 0
                    if endVal != 6:
                        playerTurn = False
                    elif endVal == 6:
                        print(f"\n{username} gets an extra turn!\n")
                else:
                    print(genError)
        if spaceVal[0]+spaceVal[1]+spaceVal[2]+spaceVal[3]+spaceVal[4]+spaceVal[5] == 0 or spaceVal[7]+spaceVal[8]+spaceVal[9]+spaceVal[10]+spaceVal[11]+spaceVal[12] == 0:
            play = False
            print("\n")
            print(f"    CPU1                                                                                                                    {username}\n   Points                                                                                                                   Points\n_________________________________________________________________________________________________________________________________________\n|                |                |                |                |                |                |                |                |\n|                |                |                |                |                |                |                |                |\n|                |       {spaceVal[12]}        |       {spaceVal[11]}        |       {spaceVal[10]}        |       {spaceVal[9]}        |       {spaceVal[8]}        |       {spaceVal[7]}        |                |\n|                |                |                |                |                |                |                |                |\n|       {spaceVal[13]}        |_____________________________________________________________________________________________________|       {spaceVal[6]}        |\n|                |                |                |                |                |                |                |                |\n|                |                |                |                |                |                |                |                |\n|                |       {spaceVal[0]}        |       {spaceVal[1]}        |       {spaceVal[2]}        |       {spaceVal[3]}        |       {spaceVal[4]}        |       {spaceVal[5]}        |                |\n|                |                |                |                |                |                |                |                |\n|                |                |                |                |                |                |                |                |\n_________________________________________________________________________________________________________________________________________\n                      Space A          Space B          Space C          Space D          Space E          Space F\n")
            print("\n")
            break
        while playerTurn == False:
            if printChk == False:
                print(f"    CPU1                                                                                                                    {username}\n   Points                                                                                                                   Points\n_________________________________________________________________________________________________________________________________________\n|                |                |                |                |                |                |                |                |\n|                |                |                |                |                |                |                |                |\n|                |       {spaceVal[12]}        |       {spaceVal[11]}        |       {spaceVal[10]}        |       {spaceVal[9]}        |       {spaceVal[8]}        |       {spaceVal[7]}        |                |\n|                |                |                |                |                |                |                |                |\n|       {spaceVal[13]}        |_____________________________________________________________________________________________________|       {spaceVal[6]}        |\n|                |                |                |                |                |                |                |                |\n|                |                |                |                |                |                |                |                |\n|                |       {spaceVal[0]}        |       {spaceVal[1]}        |       {spaceVal[2]}        |       {spaceVal[3]}        |       {spaceVal[4]}        |       {spaceVal[5]}        |                |\n|                |                |                |                |                |                |                |                |\n|                |                |                |                |                |                |                |                |\n_________________________________________________________________________________________________________________________________________\n                      Space A          Space B          Space C          Space D          Space E          Space F\n")
                printChk = True
            if dif == 1:
                bonusChk = random.randint(1,5)
            elif dif == 2:
                bonusChk = random.randint(1,3)
            elif dif == 3:
                if turn1 == True:
                    bonusChk = 1
                    turn1 == False
                else:
                    bonusChk = random.randint(1,3)
                    if bonusChk == 2:
                        bonusChk = 1
            elif dif == 4:
                bonusChk = 1
            if spaceVal[12] % 12 == 1 and spaceVal[12] != 0 and bonusChk == 1:
                cpuInp = 6
            elif spaceVal[11] % 12 == 2 and spaceVal[11] != 0 and bonusChk == 1:
                cpuInp = 5
            elif spaceVal[10] % 12 == 3 and spaceVal[10] != 0 and bonusChk == 1:
                cpuInp = 4
            elif spaceVal[9] % 12 == 4 and spaceVal[9] != 0 and bonusChk == 1:
                cpuInp = 3
            elif spaceVal[8] % 12 == 5 and spaceVal[8] != 0 and bonusChk == 1:
                cpuInp = 2
            elif spaceVal[7] % 12 == 6 and spaceVal[7] != 0 and bonusChk == 1:
                cpuInp = 1
            elif capCheck(12, spaceVal) == True and bonusChk == 1:
                cpuInp = 6
            elif capCheck(11, spaceVal) == True and bonusChk == 1:
                cpuInp = 5
            elif capCheck(10, spaceVal) == True and bonusChk == 1:
                cpuInp = 4
            elif capCheck(9, spaceVal) == True and bonusChk == 1:
                cpuInp = 3
            elif capCheck(8, spaceVal) == True and bonusChk == 1:
                cpuInp = 2
            elif capCheck(7, spaceVal) == True and bonusChk == 1:
                cpuInp = 1
            else:
                cpuInp = random.randint(1,6)
            if cpuInp == 1:
                if spaceVal[7] <= 0:
                    break
                print("\nCPU1 moves from Space F\n")
                handStart = 7
                handVal = spaceVal[7]
                spaceVal[7] = 0
                i=0
                chk = False
                chk2 = False
                chk3 = False
                while chk == False:
                    for i in range(handVal):
                        if i > 5 and chk2 == False:
                            handStart = -1
                            chk2 = True
                            break
                        elif i >= 6  and chk2 == True and chk3 == False:
                            handStart = 6
                            chk3 = True
                            break
                        elif i >= 7 and chk3 == True:
                            handStart = -1
                            chk3 = False
                            break
                        elif chk == True:
                            break
                        else:
                            moves = i+1
                            handLoc = handStart+moves
                            spaceVal[handLoc] += 1
                            handVal -= 1
                            if handVal == 0:
                                chk = True
                endVal = handLoc
                if endVal == 7 and spaceVal[7] == 1 and spaceVal[5] != 0:
                    print(f"\nCPU1 captures {spaceVal[5]} stones from space F!\n")
                    spaceVal[13] += spaceVal[7] + spaceVal[5]
                    spaceVal[7] = 0
                    spaceVal[5] = 0
                elif endVal == 8 and spaceVal[8] == 1 and spaceVal[4] != 0:
                    print(f"\nCPU1 captures {spaceVal[4]} stones from space E!\n")
                    spaceVal[13] += spaceVal[8] + spaceVal[4]
                    spaceVal[8] = 0
                    spaceVal[4] = 0
                elif endVal == 9 and spaceVal[9] == 1 and spaceVal[3] != 0:
                    print(f"\nCPU1 captures {spaceVal[3]} stones from space D!\n")
                    spaceVal[13] += spaceVal[9] + spaceVal[3]
                    spaceVal[9] = 0
                    spaceVal[3] = 0
                elif endVal == 10 and spaceVal[10] == 1 and spaceVal[2] != 0:
                    print(f"\nCPU1 captures {spaceVal[2]} stones from space C!\n")
                    spaceVal[13] += spaceVal[10] + spaceVal[2]
                    spaceVal[10] = 0
                    spaceVal[2] = 0
                elif endVal == 11 and spaceVal[11] == 1 and spaceVal[1] != 0:
                    print(f"\nCPU1 captures {spaceVal[1]} stones from space B!\n")
                    spaceVal[13] += spaceVal[11] + spaceVal[1]
                    spaceVal[11] = 0
                    spaceVal[1] = 0
                elif endVal == 12 and spaceVal[12] == 1 and spaceVal[0] != 0:
                    print(f"\nCPU1 captures {spaceVal[0]} stones from space A!\n")
                    spaceVal[13] += spaceVal[12] + spaceVal[0]
                    spaceVal[12] = 0
                    spaceVal[0] = 0
                if endVal != 13:
                    playerTurn = True
                elif endVal == 13:
                    print("\nCPU1 gets an extra turn!\n")
                printChk = False
            elif cpuInp == 2:
                if spaceVal[8] <= 0:
                    break
                print("\nCPU1 moves from space E\n")
                handStart = 8
                handVal = spaceVal[8]
                spaceVal[8] = 0
                i=0
                chk = False
                chk2 = False
                chk3 = False
                while chk == False:
                    for i in range(handVal):
                        if i > 4 and chk2 == False:
                            handStart = -1
                            chk2 = True
                            break
                        elif i >= 6  and chk2 == True and chk3 == False:
                            handStart = 6
                            chk3 = True
                            break
                        elif i >= 7 and chk3 == True:
                            handStart = -1
                            chk3 = False
                            break
                        elif chk == True:
                            break
                        else:
                            moves = i+1
                            handLoc = handStart+moves
                            spaceVal[handLoc] += 1
                            handVal -= 1
                            if handVal == 0:
                                chk = True
                endVal = handLoc
                if endVal == 7 and spaceVal[7] == 1 and spaceVal[5] != 0:
                    print(f"\nCPU1 captures {spaceVal[5]} stones from space F!\n")
                    spaceVal[13] += spaceVal[7] + spaceVal[5]
                    spaceVal[7] = 0
                    spaceVal[5] = 0
                elif endVal == 8 and spaceVal[8] == 1 and spaceVal[4] != 0:
                    print(f"\nCPU1 captures {spaceVal[4]} stones from space E!\n")
                    spaceVal[13] += spaceVal[8] + spaceVal[4]
                    spaceVal[8] = 0
                    spaceVal[4] = 0
                elif endVal == 9 and spaceVal[9] == 1 and spaceVal[3] != 0:
                    print(f"\nCPU1 captures {spaceVal[3]} stones from space D!\n")
                    spaceVal[13] += spaceVal[9] + spaceVal[3]
                    spaceVal[9] = 0
                    spaceVal[3] = 0
                elif endVal == 10 and spaceVal[10] == 1 and spaceVal[2] != 0:
                    print(f"\nCPU1 captures {spaceVal[2]} stones from space C!\n")
                    spaceVal[13] += spaceVal[10] + spaceVal[2]
                    spaceVal[10] = 0
                    spaceVal[2] = 0
                elif endVal == 11 and spaceVal[11] == 1 and spaceVal[1] != 0:
                    print(f"\nCPU1 captures {spaceVal[1]} stones from space B!\n")
                    spaceVal[13] += spaceVal[11] + spaceVal[1]
                    spaceVal[11] = 0
                    spaceVal[1] = 0
                elif endVal == 12 and spaceVal[12] == 1 and spaceVal[0] != 0:
                    print(f"\nCPU1 captures {spaceVal[0]} stones from space A!\n")
                    spaceVal[13] += spaceVal[12] + spaceVal[0]
                    spaceVal[12] = 0
                    spaceVal[0] = 0
                if endVal != 13:
                    playerTurn = True
                elif endVal == 13:
                    print("\nCPU1 gets an extra turn!\n")
                printChk = False
            elif cpuInp == 3:
                if spaceVal[9] <= 0:
                    break
                print("\nCPU1 moves from space D\n")
                handStart = 9
                handVal = spaceVal[9]
                spaceVal[9] = 0
                i=0
                chk = False
                chk2 = False
                chk3 = False
                while chk == False:
                    for i in range(handVal):
                        if i > 3 and chk2 == False:
                            handStart = -1
                            chk2 = True
                            break
                        elif i >= 6  and chk2 == True and chk3 == False:
                            handStart = 6
                            chk3 = True
                            break
                        elif i >= 7 and chk3 == True:
                            handStart = -1
                            chk3 = False
                            break
                        elif chk == True:
                            break
                        else:
                            moves = i+1
                            handLoc = handStart+moves
                            spaceVal[handLoc] += 1
                            handVal -= 1
                            if handVal == 0:
                                chk = True
                endVal = handLoc
                if endVal == 7 and spaceVal[7] == 1 and spaceVal[5] != 0:
                    print(f"\nCPU1 captures {spaceVal[5]} stones from space F!\n")
                    spaceVal[13] += spaceVal[7] + spaceVal[5]
                    spaceVal[7] = 0
                    spaceVal[5] = 0
                elif endVal == 8 and spaceVal[8] == 1 and spaceVal[4] != 0:
                    print(f"\nCPU1 captures {spaceVal[4]} stones from space E!\n")
                    spaceVal[13] += spaceVal[8] + spaceVal[4]
                    spaceVal[8] = 0
                    spaceVal[4] = 0
                elif endVal == 9 and spaceVal[9] == 1 and spaceVal[3] != 0:
                    print(f"\nCPU1 captures {spaceVal[3]} stones from space D!\n")
                    spaceVal[13] += spaceVal[9] + spaceVal[3]
                    spaceVal[9] = 0
                    spaceVal[3] = 0
                elif endVal == 10 and spaceVal[10] == 1 and spaceVal[2] != 0:
                    print(f"\nCPU1 captures {spaceVal[2]} stones from space C!\n")
                    spaceVal[13] += spaceVal[10] + spaceVal[2]
                    spaceVal[10] = 0
                    spaceVal[2] = 0
                elif endVal == 11 and spaceVal[11] == 1 and spaceVal[1] != 0:
                    print(f"\nCPU1 captures {spaceVal[1]} stones from space B!\n")
                    spaceVal[13] += spaceVal[11] + spaceVal[1]
                    spaceVal[11] = 0
                    spaceVal[1] = 0
                elif endVal == 12 and spaceVal[12] == 1 and spaceVal[0] != 0:
                    print(f"\nCPU1 captures {spaceVal[0]} stones from space A!\n")
                    spaceVal[13] += spaceVal[12] + spaceVal[0]
                    spaceVal[12] = 0
                    spaceVal[0] = 0
                if endVal != 13:
                    playerTurn = True
                elif endVal == 13:
                    print("\nCPU1 gets an extra turn!\n")
                printChk = False
            elif cpuInp == 4:
                if spaceVal[10] <= 0:
                    break
                print("\nCPU1 moves from space C\n")
                handStart = 10
                handVal = spaceVal[10]
                spaceVal[10] = 0
                i=0
                chk = False
                chk2 = False
                chk3 = False
                while chk == False:
                    for i in range(handVal):
                        if i > 2 and chk2 == False:
                            handStart = -1
                            chk2 = True
                            break
                        elif i >= 6  and chk2 == True and chk3 == False:
                            handStart = 6
                            chk3 = True
                            break
                        elif i >= 7 and chk3 == True:
                            handStart = -1
                            chk3 = False
                            break
                        elif chk == True:
                            break
                        else:
                            moves = i+1
                            handLoc = handStart+moves
                            spaceVal[handLoc] += 1
                            handVal -= 1
                            if handVal == 0:
                                chk = True
                endVal = handLoc
                if endVal == 7 and spaceVal[7] == 1 and spaceVal[5] != 0:
                    print(f"\nCPU1 captures {spaceVal[5]} stones from space F!\n")
                    spaceVal[13] += spaceVal[7] + spaceVal[5]
                    spaceVal[7] = 0
                    spaceVal[5] = 0
                elif endVal == 8 and spaceVal[8] == 1 and spaceVal[4] != 0:
                    print(f"\nCPU1 captures {spaceVal[4]} stones from space E!\n")
                    spaceVal[13] += spaceVal[8] + spaceVal[4]
                    spaceVal[8] = 0
                    spaceVal[4] = 0
                elif endVal == 9 and spaceVal[9] == 1 and spaceVal[3] != 0:
                    print(f"\nCPU1 captures {spaceVal[3]} stones from space D!\n")
                    spaceVal[13] += spaceVal[9] + spaceVal[3]
                    spaceVal[9] = 0
                    spaceVal[3] = 0
                elif endVal == 10 and spaceVal[10] == 1 and spaceVal[2] != 0:
                    print(f"\nCPU1 captures {spaceVal[2]} stones from space C!\n")
                    spaceVal[13] += spaceVal[10] + spaceVal[2]
                    spaceVal[10] = 0
                    spaceVal[2] = 0
                elif endVal == 11 and spaceVal[11] == 1 and spaceVal[1] != 0:
                    print(f"\nCPU1 captures {spaceVal[1]} stones from space B!\n")
                    spaceVal[13] += spaceVal[11] + spaceVal[1]
                    spaceVal[11] = 0
                    spaceVal[1] = 0
                elif endVal == 12 and spaceVal[12] == 1 and spaceVal[0] != 0:
                    print(f"\nCPU1 captures {spaceVal[0]} stones from space A!\n")
                    spaceVal[13] += spaceVal[12] + spaceVal[0]
                    spaceVal[12] = 0
                    spaceVal[0] = 0
                if endVal != 13:
                    playerTurn = True
                elif endVal == 13:
                    print("\nCPU1 gets an extra turn!\n")
                printChk = False
            elif cpuInp == 5:
                if spaceVal[11] <= 0:
                    break
                print("\nCPU1 moves from space B\n")
                handStart = 11
                handVal = spaceVal[11]
                spaceVal[11] = 0
                i=0
                chk = False
                chk2 = False
                chk3 = False
                while chk == False:
                    for i in range(handVal):
                        if i > 1 and chk2 == False:
                            handStart = -1
                            chk2 = True
                            break
                        elif i >= 6  and chk2 == True and chk3 == False:
                            handStart = 6
                            chk3 = True
                            break
                        elif i >= 7 and chk3 == True:
                            handStart = -1
                            chk3 = False
                            break
                        elif chk == True:
                            break
                        else:
                            moves = i+1
                            handLoc = handStart+moves
                            spaceVal[handLoc] += 1
                            handVal -= 1
                            if handVal == 0:
                                chk = True
                endVal = handLoc
                if endVal == 7 and spaceVal[7] == 1 and spaceVal[5] != 0:
                    print(f"\nCPU1 captures {spaceVal[5]} stones from space F!\n")
                    spaceVal[13] += spaceVal[7] + spaceVal[5]
                    spaceVal[7] = 0
                    spaceVal[5] = 0
                elif endVal == 8 and spaceVal[8] == 1 and spaceVal[4] != 0:
                    print(f"\nCPU1 captures {spaceVal[4]} stones from space E!\n")
                    spaceVal[13] += spaceVal[8] + spaceVal[4]
                    spaceVal[8] = 0
                    spaceVal[4] = 0
                elif endVal == 9 and spaceVal[9] == 1 and spaceVal[3] != 0:
                    print(f"\nCPU1 captures {spaceVal[3]} stones from space D!\n")
                    spaceVal[13] += spaceVal[9] + spaceVal[3]
                    spaceVal[9] = 0
                    spaceVal[3] = 0
                elif endVal == 10 and spaceVal[10] == 1 and spaceVal[2] != 0:
                    print(f"\nCPU1 captures {spaceVal[2]} stones from space C!\n")
                    spaceVal[13] += spaceVal[10] + spaceVal[2]
                    spaceVal[10] = 0
                    spaceVal[2] = 0
                elif endVal == 11 and spaceVal[11] == 1 and spaceVal[1] != 0:
                    print(f"\nCPU1 captures {spaceVal[1]} stones from space B!\n")
                    spaceVal[13] += spaceVal[11] + spaceVal[1]
                    spaceVal[11] = 0
                    spaceVal[1] = 0
                elif endVal == 12 and spaceVal[12] == 1 and spaceVal[0] != 0:
                    print(f"\nCPU1 captures {spaceVal[0]} stones from space A!\n")
                    spaceVal[13] += spaceVal[12] + spaceVal[0]
                    spaceVal[12] = 0
                    spaceVal[0] = 0
                if endVal != 13:
                    playerTurn = True
                elif endVal == 13:
                    print("\nCPU1 gets an extra turn!\n")
                printChk = False
            elif cpuInp == 6:
                if spaceVal[12] <= 0:
                    break
                print("\nCPU1 moves from space A\n")
                handStart = 12
                handVal = spaceVal[12]
                spaceVal[12] = 0
                i=0
                chk = False
                chk2 = False
                chk3 = False
                while chk == False:
                    for i in range(handVal):
                        if i > 0 and chk2 == False:
                            handStart = -1
                            chk2 = True
                            break
                        elif i >= 6  and chk2 == True and chk3 == False:
                            handStart = 6
                            chk3 = True
                            break
                        elif i >= 7 and chk3 == True:
                            handStart = -1
                            chk3 = False
                            break
                        elif chk == True:
                            break
                        else:
                            moves = i+1
                            handLoc = handStart+moves
                            spaceVal[handLoc] += 1
                            handVal -= 1
                            if handVal == 0:
                                chk = True
                endVal = handLoc
                if endVal == 7 and spaceVal[7] == 1 and spaceVal[5] != 0:
                    print(f"\nCPU1 captures {spaceVal[5]} stones from space F!\n")
                    spaceVal[13] += spaceVal[7] + spaceVal[5]
                    spaceVal[7] = 0
                    spaceVal[5] = 0
                elif endVal == 8 and spaceVal[8] == 1 and spaceVal[4] != 0:
                    print(f"\nCPU1 captures {spaceVal[4]} stones from space E!\n")
                    spaceVal[13] += spaceVal[8] + spaceVal[4]
                    spaceVal[8] = 0
                    spaceVal[4] = 0
                elif endVal == 9 and spaceVal[9] == 1 and spaceVal[3] != 0:
                    print(f"\nCPU1 captures {spaceVal[3]} stones from space D!\n")
                    spaceVal[13] += spaceVal[9] + spaceVal[3]
                    spaceVal[9] = 0
                    spaceVal[3] = 0
                elif endVal == 10 and spaceVal[10] == 1 and spaceVal[2] != 0:
                    print(f"\nCPU1 captures {spaceVal[2]} stones from space C!\n")
                    spaceVal[13] += spaceVal[10] + spaceVal[2]
                    spaceVal[10] = 0
                    spaceVal[2] = 0
                elif endVal == 11 and spaceVal[11] == 1 and spaceVal[1] != 0:
                    print(f"\nCPU1 captures {spaceVal[1]} stones from space B!\n")
                    spaceVal[13] += spaceVal[11] + spaceVal[1]
                    spaceVal[11] = 0
                    spaceVal[1] = 0
                elif endVal == 12 and spaceVal[12] == 1 and spaceVal[0] != 0:
                    print(f"\nCPU1 captures {spaceVal[0]} stones from space A!\n")
                    spaceVal[13] += spaceVal[12] + spaceVal[0]
                    spaceVal[12] = 0
                    spaceVal[0] = 0
                if endVal != 13:
                    playerTurn = True
                elif endVal == 13:
                    print("\nCPU1 gets an extra turn!\n")
                printChk = False
        if spaceVal[0]+spaceVal[1]+spaceVal[2]+spaceVal[3]+spaceVal[4]+spaceVal[5] == 0 or spaceVal[7]+spaceVal[8]+spaceVal[9]+spaceVal[10]+spaceVal[11]+spaceVal[12] == 0:
            play = False
            print("\n")
            print(f"    CPU1                                                                                                                    {username}\n   Points                                                                                                                   Points\n_________________________________________________________________________________________________________________________________________\n|                |                |                |                |                |                |                |                |\n|                |                |                |                |                |                |                |                |\n|                |       {spaceVal[12]}        |       {spaceVal[11]}        |       {spaceVal[10]}        |       {spaceVal[9]}        |       {spaceVal[8]}        |       {spaceVal[7]}        |                |\n|                |                |                |                |                |                |                |                |\n|       {spaceVal[13]}        |_____________________________________________________________________________________________________|       {spaceVal[6]}        |\n|                |                |                |                |                |                |                |                |\n|                |                |                |                |                |                |                |                |\n|                |       {spaceVal[0]}        |       {spaceVal[1]}        |       {spaceVal[2]}        |       {spaceVal[3]}        |       {spaceVal[4]}        |       {spaceVal[5]}        |                |\n|                |                |                |                |                |                |                |                |\n|                |                |                |                |                |                |                |                |\n_________________________________________________________________________________________________________________________________________\n                      Space A          Space B          Space C          Space D          Space E          Space F\n")
            print("\n")
            break
    if spaceVal[6] > spaceVal[13]:
        posCongrats = ["That was one for the history books!","And just barely, too!","Unlocked ending 1 of 4: Victory!","Take a picture!","I\'ll alert the presses! Just kidding. They already know.","And for your prize... uh... I misplaced the trophy. Will you take an IOU?","A winner is you!",f"Oh wow! {spaceVal[6]-spaceVal[13]} is my favorite color! Er, number. My favorite number.","Did you get the world record? Or just a new pb?"]
        if dif == 1:
            posCongrats.append("But only on the lowest difficulty. Try 2 or 3 if you\'re feeling up to it!")
        elif dif == 2:
            posCongrats.append("Great job beating level 2! Now, if you want a REAL challenge, why not try level 3?")
        elif dif == 3:
            posCongrats.append("Level 3 has been conquered! Amazing!")
        congrats = posCongrats[random.randint(0,len(posCongrats)-1)]
        print(f"Congratulations, {username}! You won by {spaceVal[6]-spaceVal[13]} on difficulty level {dif}! {congrats}")
        if dif == 3 and len(difLevels) == 3:
            print(f"\nSay, player... now that you've beaten level 3, want to try the toughest level we have? enter 'difficulty 4' on the main menu to unlock level 4.")
    elif spaceVal[6] < spaceVal[13]:
        posSorry = ["Unlocked ending 3 of 4: Defeat.","Better luck next time.","Don\'t worry, I lost when I played first too. (jk but still you\'re good)","Great Job! Oh. Wait. The CPU won. Whoops.","You\'ll get it eventually.","the CPU won... but at what cost?","Wow, congratulations, CPU! you took down one of our best players!",f"For the sake of humans and CPUs... {username}! You must stay determined!","oof","Close one. You\'ll do better next time!"]
        if dif > 1:
            posSorry.append("Tough luck. If you\'re feeling overwhelmed, try lowering the difficulty level.")
        sorry = posSorry[random.randint(0,len(posSorry)-1)]
        print(f"Sorry, {username}. You lost by {spaceVal[13]-spaceVal[6]} on difficulty level {dif}. {sorry}")
    elif spaceVal[6] == spaceVal[13]:
        posWhat = ["No winner. Just like war.","That\'s never happened before. I think.","How\'d you manage that? Are you and the CPU working together?","Huh. Didn\'t see that coming.","Guess I should say something about the poetic nature of democracy, and about how I\'m going to fight this thing from my prison cell.","Unlocked ending 4 of 4: Tie?","So does that mean you both won, or neither of you did?","I guess I just keep the prize money then, huh? That's a shame.","No loser? But we needed a human sacrifice!"]
        what = posWhat[random.randint(0,len(posWhat)-1)]
        print(f"And the winner is... oh. It was a tie. {what}")
    print("\n")

def user():
    global dif, genError, difLevels, username, inputs, debug
    if dif not in difLevels:
        dif = 1
    userOpt = ""
    while userOpt != "y" and userOpt != "n":
        userOpt = input(f"\n\nYour current username is {username}. Would you like to change it? (y or n)\n")
        if userOpt == "n":
            print("\nReturning to the main menu...\n")
            return username
        elif userOpt == "y":
            userSlc = ""
            while len(userSlc) <= 0 or len(userSlc) >= 21:
                userSlc = input("\nType your new username now. Max 20 characters\n")
                if len(userSlc) <= 0:
                    print("\nYour username cannot be blank. Enter a new username.\n")
                elif len(userSlc) >= 21:
                    print("\nUsernames can only be 20 or less characters. Enter a new username.\n")
                else:
                    print(f"\nSounds good. Your name is now {userSlc}.\n")
                    return userSlc
        else:
            print(genError)


def difficulty():
    global dif, genError, difLevels, username, inputs, debug
    difOpt=""
    if dif not in difLevels:
        dif = 1
    while difOpt != "y" and difOpt != "n":
        difOpt=str(input(f"\n\nThe current difficulty level is {dif}. Would you like to change it? (y or n)\n")).lower()
        if difOpt == "n":
            print("\nReturning to main menu...\n")
            return dif
        elif difOpt == "y":
            difSlc=0
            while difSlc not in difLevels:
                if len(difLevels) == 3:
                    difSlc=int(input("\nThe difficulty options are 1, 2, and 3. If you choose 3, the computer goes first. Which one would you like?\n"))
                    if difSlc in difLevels:
                        print(f"\nThe difficulty level is now set to {difSlc}\n")
                        return difSlc
                    else:
                        print(genError)
                else:
                    difSlc=int(input("\nThe difficulty options are 1, 2, 3, and 4. If you choose 3 or 4, the computer goes first. Which one would you like?\n"))
                    if difSlc in difLevels:
                        print(f"\nThe difficulty level is now set to {difSlc}\n")
                        return difSlc
                    else:
                        print(genError)
        else:
            print(genError)

def main():
    global dif, genError, difLevels, username, inputs, debug
    posSlogans = ["Wear a mask!","Wear a mash! Yeah. You read that right.","What do you mean I forgot to hit CTRL-S?!","over 1000000 copies sold every attosecond","A game I made that I didn't really make!","new phone, who dis?","also try minceraft!","Never gonna give you up","See mom?! I told you I could do it!","I'm listening to Rhythm Heaven music while I type this.","Bottom Text"]
    slogan = posSlogans[random.randint(0,len(posSlogans)-1)]
    print(f"Welcome to Mancala: {slogan}")
    print("")
    menuOpt=""
    while menuOpt != "q":
        menuOpt = str(input("What would you like to do?\n-press p to play mancala\n-press u to change username\n-press d to change difficulty level\n-press q to quit\n")).lower()
        if menuOpt == "q":
            print("Goodbye. We'll miss you!")
        elif menuOpt == "p":
            mancala()
        elif menuOpt == "u":
            username = user()
        elif menuOpt == "d":
            dif = difficulty()
        elif menuOpt == "rhythm heaven for smash":
            print("oh, totally. Sora didn't deserve it.")
        elif menuOpt == "difficulty 4":
            difLevels.append(4)
            print("I see you've beaten level 3. You can now change to level 4 in the difficulty menu.")
        else:
            print("Sorry, we don't have that feature in Mancala. I'll send an email about it to management.")

main()
