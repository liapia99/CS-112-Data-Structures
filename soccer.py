#   ============================================
#   File: soccer.py
#   Date: Nov. 22, 2022
#   Using Seq. Files and functions
#   Author: Julia Piascik
#   ============================================

def getPlayers():
    playerL = []
    playerFile = open("players.dat", 'r')
    for player in playerFile:
        player = player.split()
        playerL.append(player)
    #end for player
    playerFile.close()
    return playerL
#end ftn getPlayers


def calcAvgAge(allPlayers):
    sum = 0
    c = 0
    older = 0
    younger = 0
    same = 0
    for player in allPlayers:
        c = c + 1
        age = float(player[1])
        sum = sum + age
    #end for player
    aveg = sum/c
    return aveg
#end ftn calcAvgAge


def calcAgevsAvg(allPlayers, avegAge):
    older = 0
    younger = 0
    same = 0
    for player in allPlayers:
        age = float(player[1])
        if age > avegAge:
            older = 1 + older
        else:
            if age < avegAge:
                younger = 1 + younger
            else:
                 same = 1 + same
            #endif
        #endif
     #end for player
    print("There are",older, "players that are older than the average.")
    print("There are",younger, "players that are younger than the average.")
    print("There are",same, "players that are the same age as the average.")
#end ftn calcAgevsAvg


def getNumber(allPlayers):
    n10 = 0
    n7 = 0
    n9 = 0
    for player in allPlayers:
        number = float(player[4])
        if number == 10:
            n10 = 1 + n10
        else:
            if number == 7:
                n7 = n7 + 1
            else:
                n9 = 1 + n9
            #endif
        #endif
    #end for player
    print("There are",n10,"players that uses the number 10 on their national teams jersey.")
    print("There are",n7,"players that uses the number 7 on their national teams jersey.")
    print("There is",n9,"player that is unique! He is the only player that uses the number 9.")
#end ftn getNumber

def getPosition(allPlayers):
    f = 0
    m = 0
    for player in allPlayers:
        position = str(player[3])
        if position == 'Forward':
            f = 1 + f
        else:
            if position == 'Midfielder':
                m = m + 1
            #endif
        #endif
    #end for player
    print("There are",f,"players that play the forward position on their national team.")
    print("There is",m,"player that play the midfielder position on their national team.")
    
#end ftn getPosition

    
# main program

allPlayers = getPlayers()
print ("The average age of Julia's favorite players is", calcAvgAge(allPlayers), "years.")
avegAge = calcAvgAge(allPlayers)

calcAgevsAvg(allPlayers, avegAge)

getNumber(allPlayers)

getPosition(allPlayers)

#end main program

#Execution Run:







