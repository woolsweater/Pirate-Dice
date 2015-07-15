# coding: utf-8

import ui
from random import randint
from collections import Counter

numCrew = 1
numDice = 1
capPresent = False
matePresent = False
daggerPlayed = False
rootView = None 
crewNumberLabel = None
hitsLabel = None
rollsView = None

def addCrew(sender):
    global numCrew
    if numCrew < 15:
        numCrew += 1
    updateNumDice()

def subtractCrew(sender):
    global numCrew
    if numCrew > 0:
        numCrew -= 1
        updateNumDice()
        
def setCapPresent(sender):
    global capPresent
    capPresent = sender.value
    updateNumDice()

def setMatePresent(sender):
    global matePresent
    matePresent = sender.value
    updateNumDice()
    
def setDaggerPlayed(sender):
    global daggerPlayed
    daggerPlayed = sender.value
    updateNumDice()

def updateNumDice():
    global numDice
    global crewNumberLabel
    
    crewNumberLabel = rootView["crewNumberLabel"]
    crewNumberLabel.text = str(numCrew)
    
    numDice = numCrew + 2 * (int(capPresent)+ int(matePresent) + int(daggerPlayed))
    
    rollButton = rootView["rollButton"]
    rollButton.title = "Roll {} {}".format(numDice, "die" if numDice == 1 else "dice")

def rollEm(sender):
    rolls = [randint(1, 6) for i in range(numDice)]
    rollsView.text = formatRolls(sorted(rolls))
    rolls = Counter(rolls)
    skulls = rolls[1]
    pairs = [rolls[r]//2 for r in range(2,7)]
    
    hits = skulls + sum(pairs)
    hitsLabel.text = "{} hit{}".format(hits, "" if hits == 1 else "s")

def formatRolls(rolls):
    # Space character at index 0, then Unicode points 
    # for skull and crossbones and each successive die face
    dieFaces = u"\u0020\u2620\u2681\u2682\u2683\u2684\u2685"
    return " ".join(dieFaces[r] for r in rolls)
    
def clearRoll(sender):
    hitsLabel.text = ""
    rollsView.text = ""
    
# Modes: Combat, cannons, retreating, plundering
#TODO: Clear button
    
rootView = ui.load_view("Pirate Dice")
hitsLabel = rootView["hitsLabel"]
rollsView = rootView["rollsView"]

rootView["captainSwitch"].value = capPresent
rootView["mateSwitch"].value = matePresent
rootView["daggerSwitch"].value = daggerPlayed
# will not persist if set in IB
rootView["daggerLabel"].number_of_lines = 2
updateNumDice()
rootView.present()
