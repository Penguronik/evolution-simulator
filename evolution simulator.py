import sys
import random as r
from tkinter import *
import threading
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
graph_data = open('example.txt', 'w')
graph_data.write("")
graph_data.close()


ispause = 1
isfullpause = 1
nexttime = 0
#these are the dimensions of the play area#
earthmultx = 30
earthmulty = 30
earthsize = earthmulty * earthmultx
runtime = 0
evolvecount = 0
global w

indent = 0

width = 300
height = 300

rindent = width - indent

circlesize = 16

gap = ((width - (2 * indent)) / earthmultx)

circlesize = (gap / 2)

squareready = 1


# i = 0
# while i < 16:
#    w.create_line(indent, indent + i * gap, rindent, indent + i * gap)b
#    w.create_line(indent + i * gap, indent, indent + i * gap, rindent)
#    i = i + 1
#    cx = 0
#    cy = 0
# while cy < 16 - 1:
#    while cx < 16 - 1:
#        color = r.randint(0, 3)
#        if color == 0:
#            color = "yellow"
#        if color == 1:
#            color = "blue"
#        if color == 2:
#            color = "green"
#        if color == 3:
#            color = "red"
#        w.create_oval(indent + circlesize + gap * cx, indent + circlesize + gap * cy, indent + circlesize + gap - circlesize * 2 + gap * cx, indent + circlesize + gap - circlesize * 2 + gap * cy, fill=color)
#        cx = cx + 1
#    cy = cy + 1
#    cx = 0

def tempscalevar(scalevalue):
    global temperature
    temperature = int(scalevalue)


def waterscalevar(scalevalue):
    global WIwaterchance
    WIwaterchance = int(scalevalue)


def creaturescalevar(scalevalue):
    global creaturechance
    creaturechance = int(scalevalue)


def grassscalevar(scalevalue):
    global grassstarter
    grassstarter = int(scalevalue)


def grasspercentscalevar(scalevalue):
    global grassincreasechance
    grassincreasechance = int(scalevalue)


def creatureevolutionscalevar(scalevalue):
    global evolvepercent
    evolvepercent = int(scalevalue)


class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()
        self.quit = 1

    def test(self):
        self.root.after(1000, self.loadcirclevalues)

    def loadcirclevalues(self):
        for x in range(earthmultx):
            for y in range(earthmulty):
                if creaturelist[x][y].alive == 1:
                    w.itemconfig(circlelist[x][y], fill="yellow")
                else:
                    w.itemconfig(circlelist[x][y], fill="blue")
        self.root.after(20, self.loadcirclevalues)

    def startup(self):
        global earthmulty
        global earthmultx
        global c
        global circlelist
        global reloadready
        global d
        global squarelist

        self.quit = 0

        d = w.create_rectangle(0, 0, 0, 0)
        squarelist = [d] * earthmulty
        for i in range(earthmulty):
            squarelist[i] = [d] * earthmultx
        for x in range(earthmultx):
            for y in range(earthmulty):
                d = w.create_rectangle(indent + gap * x, indent + gap * y, indent + gap + gap * x, indent + gap + gap * y, fill="red")
                squarelist[x][y] = d

        c = w.create_oval(0, 0, 0, 0)
        circlelist = [c] * earthmulty
        for i in range(earthmulty):
            circlelist[i] = [c] * earthmultx
        for x in range(earthmultx):
            for y in range(earthmulty):
                #                c = w.create_oval(indent + circlesize + gap * x, indent + circlesize + gap * y, indent + circlesize + gap - circlesize * 2 + gap * x, indent + circlesize + gap - circlesize * 2 + gap * y, fill="green")
                c = w.create_oval(indent + gap * x + (gap / 4), indent + gap * y + (gap / 4), indent + circlesize + gap * x + (gap / 4), indent + circlesize + gap * y + (gap / 4), fill="green")
                circlelist[x][y] = c

        reloadready = 1

    def pauseplay(self):
        global b
        global pausetext
        global ispause
        if pausetext == "Pause":
            ispause = 1
            bt.grid()
            pausetext = "Play"
        else:
            pausetext = "Pause"
            ispause = 0
            isfullpause = 0
            bt.grid_remove()
        b.config(text=pausetext)

    def printstatstolabel(self, event):
        #statslabeltext  = ("x:%d y:%d\n posx:%d\n posy:%d\n"%(event.x, event.y, event.x/gap, event.y/gap))
        #statslabel.config(text = statslabeltext)
        eventx = int(event.x / gap)
        eventy = int(event.y / gap)
        creaturelabel.config(text="Creature Stats: \nAlive = %d \nStamina = %d \nSense = %d \nWeight = %d \nSpeed = %d \nStrength = %d \nTemperature = %d" % (creaturelist[eventx][eventy].alive, creaturelist[eventx][eventy].stamina, creaturelist[eventx][eventy].sense, creaturelist[eventx][eventy].weight, creaturelist[eventx][eventy].speed, creaturelist[eventx][eventy].strength, creaturelist[eventx][eventy].temperature))
        earthlabel.config(text="Environment Stats: \nWater = %d \nGrass = %d \n" % (earthlist[eventx][eventy].water, earthlist[eventx][eventy].grass))

    def next(self):
        global nexttime
        nexttime = 1

    def run(self):
        global w
        global b
        global pausetext
        global statslabel
        global earthlabel
        global creaturelabel
        global bt
        global ispause
        global testtesttest
        global tempscale
        global waterscale
        global creaturescale
        global grassscale
        global grasspercentscale
        global turncountlabel
        global evolvecount
        global runtime
        global creatureevolutionscale

        testtesttest = 0
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        turncountlabel = Label(self.root, text="Evolution Count: %d \nRound Count: %d" % (evolvecount, runtime), font=("Courier New", 13))
        turncountlabel.config(text="Evolution Count: %d \nRound Count: %d" % (evolvecount, runtime))
        turncountlabel.grid(row=1, column=4)
        templabel = Label(self.root, text="Temperature", font=("", 15))
        templabel.grid(row=2, column=0)
        tempscale = Scale(self.root, orient=HORIZONTAL, length=200, from_=-1, to=1, command=tempscalevar)
        tempscale.grid(row=3, column=0)
        tempscale.set(0)
        waterlabel = Label(self.root, text="Water %", font=("", 15))
        waterlabel.grid(row=4, column=0)
        waterscale = Scale(self.root, orient=HORIZONTAL, length=200, from_=0, to=100, command=waterscalevar)
        waterscale.grid(row=5, column=0)
        waterscale.set(25)
        creaturelabel = Label(self.root, text="Creature %", font=("", 15))
        creaturelabel.grid(row=6, column=0)
        creaturescale = Scale(self.root, orient=HORIZONTAL, length=200, from_=0, to=100, command=creaturescalevar)
        creaturescale.grid(row=7, column=0)
        creaturescale.set(25)
        grasslabel = Label(self.root, text="Default Grass", font=("", 15))
        grasslabel.grid(row=8, column=0)
        grassscale = Scale(self.root, orient=HORIZONTAL, length=200, from_=0, to=100, command=grassscalevar)
        grassscale.grid(row=9, column=0)
        grassscale.set(25)
        grasspercentlabel = Label(self.root, text="Grass Increase Chance", font=("", 15))
        grasspercentlabel.grid(row=10, column=0)
        grasspercentscale = Scale(self.root, orient=HORIZONTAL, length=200, from_=0, to=100, command=grasspercentscalevar)
        grasspercentscale.grid(row=11, column=0)
        grasspercentscale.set(20)
        creatureevolutionlabel = Label(self.root, text="Evolution Rate %", font=("", 15))
        creatureevolutionlabel.grid(row=12, column=0)
        creatureevolutionscale = Scale(self.root, orient=HORIZONTAL, length=200, from_=0, to=100, command=creatureevolutionscalevar)
        creatureevolutionscale.grid(row=13, column=0)
        creatureevolutionscale.set(80)
        label = Label(self.root, text="A Visual Representation of The Evolution Simulator", font=("Helvetica", 30), fg="black")
        label.grid(row=0, column=0, columnspan=4)
        pausetext = "Play"
        b = Button(self.root, text=pausetext, command=self.pauseplay, height=5, width=15)
        b.grid(row=3, column=3)
        bt = Button(self.root, text="Next", command=self.next, height=5, width=15)
        bt.grid(row=5, column=3, sticky=N)
        statslabel = Label(self.root, text="")
        statslabel.grid(row=12, column=1, columnspan=2)
        w = Canvas(self.root, width=width, height=height)
        w.bind("<Button-1>", self.printstatstolabel)
#        w.pack(fill=BOTH, expand=YES)
        w.grid(row=3, column=1, rowspan=9, columnspan=2)
        bt.grid_remove()
        earthlabel = Label(self.root, text="", font=("", 13))
        creaturelabel = Label(self.root, text="", font=("", 13))
        earthlabel.grid(row=13, column=1, columnspan=2)
        creaturelabel.grid(row=14, column=1, columnspan=2)

        self.startup()
        self.root.mainloop()

    def createcircle(self, x, y, alive):
        if creaturelist:
            w.create_oval(x * 2, y * 2, x * 2 + 1, y * 2 + 1, fill="yellow")
        else:
            w.create_oval(x * 2, y * 2, x * 2 + 1, y * 2 + 1, fill="blue")

    def printcircles(self):
        newline = 0
        shape = ['.', '#']
        for pwy in range(earthmulty):
            for pwx in range(earthmultx):
                if creaturelist[pwx][pwy].alive == 1:
                    color = "yellow"
                if creaturelist[pwx][pwy].alive == 0:
                    color = "blue"
                # w.create_oval(indent + circlesize + gap * pwx, indent + circlesize + gap * pwy, indent + circlesize + gap - circlesize * 2 + gap * pwx, indent + circlesize + gap - circlesize * 2 + gap * pwy, fill=color)


def reloadcircle():
    for x in range(earthmultx):
        for y in range(earthmulty):
            if creaturelist[x][y].alive == 1:
                w.itemconfig(circlelist[x][y], fill="yellow", state=NORMAL)
            else:
                w.itemconfig(circlelist[x][y], fill="blue", state=HIDDEN)


def reloadsquares():
    for x in range(earthmultx):
        for y in range(earthmulty):
            if earthlist[x][y].water == 1:
                w.itemconfig(squarelist[x][y], fill="blue", state=NORMAL)
            else:
                w.itemconfig(squarelist[x][y], fill="green", state=NORMAL)


app = App()
print('Now we can continue running code while mainloop runs!')
# while True:
#    i=0
while ispause == 1:
    randomnumberrandom = 1

maxskill = 100
sfdirt = 0
sfwater = 1
sfgrass = 2

staminamax = 9000
watermax = 100
subtractstamina = 4500

temperature = tempscale.get()

#function for calculating deaths#
fights = 0
famine = 0
thirst = 0
thirstfamine = 0
allfamine = 0
allthirst = 0
allthirstfamine = 0
allfights = 0

deathstatslist = []
finalstatslist = []

speedlist = []
weightlist = []
staminalist = []
templist = []
senselist = []


def movement(wx, wy):
    i = 0
    creaturelist[wx][wy].calculateall(wx, wy)
    sensechance = creaturelist[wx][wy].senseprob()
    chanceto = r.randint(0, 100)
    if chanceto < 50:
        gotime = 0
        chanceto = r.randint(0, 100)
        if sensechance > chanceto:
            gotime = 1
        else:
            gotime = 0
    else:
        gotime = 1
    if gotime == 1:
        if wx + 1 == earthmultx and wy + 1 == earthmulty:
            chance = r.randint(0, 1)
            if chance == 0:
                z = checkcreature(wx, wy, wx - 1, wy)
                if z == 0:
                    creaturelist[wx - 1][wy].loadstats(creaturelist[wx][wy])

            if chance == 1:
                z = checkcreature(wx, wy, wx, wy - 1)
                if z == 0:
                    creaturelist[wx][wy - 1].loadstats(creaturelist[wx][wy])

            i = 1
        if wx - 1 == -1 and wy - 1 == -1:
            chance = r.randint(0, 1)
            if chance == 0:
                z = checkcreature(wx, wy, wx + 1, wy)
                if z == 0:
                    creaturelist[wx + 1][wy].loadstats(creaturelist[wx][wy])

                wx += 1
            if chance == 1:
                z = checkcreature(wx, wy, wx, wy + 1)
                if z == 0:
                    creaturelist[wx][wy + 1].loadstats(creaturelist[wx][wy])

            i = 1
        if wx - 1 == -1 and wy + 1 == earthmulty:
            chance = r.randint(0, 1)
            if chance == 0:
                z = checkcreature(wx, wy, wx + 1, wy)
                if z == 0:
                    creaturelist[wx + 1][wy].loadstats(creaturelist[wx][wy])

                wx += 1
            if chance == 1:
                z = checkcreature(wx, wy, wx, wy - 1)
                if z == 0:
                    creaturelist[wx][wy - 1].loadstats(creaturelist[wx][wy])

            i = 1
        if wx + 1 == earthmultx and wy - 1 == -1:
            chance = r.randint(0, 1)
            if chance == 0:
                z = checkcreature(wx, wy, wx - 1, wy)
                if z == 0:
                    creaturelist[wx - 1][wy].loadstats(creaturelist[wx][wy])

            if chance == 1:
                z = checkcreature(wx, wy, wx, wy + 1)
                if z == 0:
                    creaturelist[wx][wy + 1].loadstats(creaturelist[wx][wy])

            i = 1
        if i == 0:
            if wx + 1 == earthmultx:
                chance = r.randint(0, 2)
                if chance == 0:
                    z = checkcreature(wx, wy, wx - 1, wy)
                    if z == 0:
                        creaturelist[wx - 1][wy].loadstats(creaturelist[wx][wy])

                if chance == 1:
                    z = checkcreature(wx, wy, wx, wy + 1)
                    if z == 0:
                        creaturelist[wx][wy + 1].loadstats(creaturelist[wx][wy])

                if chance == 2:
                    z = checkcreature(wx, wy, wx, wy - 1)
                    if z == 0:
                        creaturelist[wx][wy - 1].loadstats(creaturelist[wx][wy])

                i = 1
            if wy + 1 == earthmulty:
                chance = r.randint(0, 2)
                if chance == 0:
                    z = checkcreature(wx, wy, wx - 1, wy)
                    if z == 0:
                        creaturelist[wx - 1][wy].loadstats(creaturelist[wx][wy])

                if chance == 1:
                    z = checkcreature(wx, wy, wx + 1, wy)
                    if z == 0:
                        creaturelist[wx + 1][wy].loadstats(creaturelist[wx][wy])

                    wx += 1
                if chance == 2:
                    z = checkcreature(wx, wy, wx, wy - 1)
                    if z == 0:
                        creaturelist[wx][wy - 1].loadstats(creaturelist[wx][wy])

                i = 1
            if wx - 1 == -1:
                chance = r.randint(0, 2)
                if chance == 0:
                    z = checkcreature(wx, wy, wx + 1, wy)
                    if z == 0:
                        creaturelist[wx + 1][wy].loadstats(creaturelist[wx][wy])

                    wx += 1
                if chance == 1:
                    z = checkcreature(wx, wy, wx, wy + 1)
                    if z == 0:
                        creaturelist[wx][wy + 1].loadstats(creaturelist[wx][wy])

                if chance == 2:
                    z = checkcreature(wx, wy, wx, wy - 1)
                    if z == 0:
                        creaturelist[wx][wy - 1].loadstats(creaturelist[wx][wy])

                i = 1
            if wy - 1 == -1:
                chance = r.randint(0, 2)
                if chance == 0:
                    z = checkcreature(wx, wy, wx - 1, wy)
                    if z == 0:
                        creaturelist[wx - 1][wy].loadstats(creaturelist[wx][wy])

                if chance == 1:
                    z = checkcreature(wx, wy, wx, wy + 1)
                    if z == 0:
                        creaturelist[wx][wy + 1].loadstats(creaturelist[wx][wy])

                if chance == 2:
                    z = checkcreature(wx, wy, wx + 1, wy)
                    if z == 0:
                        creaturelist[wx + 1][wy].loadstats(creaturelist[wx][wy])

                    wx += 1
                i = 1
        #This is for movement#
        if i == 0:
            chance = r.randint(0, 3)
            if chance == 0:
                z = checkcreature(wx, wy, wx + 1, wy)
                if z == 0:
                    creaturelist[wx + 1][wy].loadstats(creaturelist[wx][wy])

                wx += 1
            if chance == 1:
                z = checkcreature(wx, wy, wx - 1, wy)
                if z == 0:
                    creaturelist[wx - 1][wy].loadstats(creaturelist[wx][wy])

            if chance == 2:
                z = checkcreature(wx, wy, wx, wy + 1)
                if z == 0:
                    creaturelist[wx][wy + 1].loadstats(creaturelist[wx][wy])

            if chance == 3:
                z = checkcreature(wx, wy, wx, wy - 1)
                if z == 0:
                    creaturelist[wx][wy - 1].loadstats(creaturelist[wx][wy])


def alldeaths():
    global allfamine
    global allthirst
    global allthirstfamine
    global allfights
    print("overall %d creatures died from famine" % (allfamine))
    print("overall %d creatures died from thirst" % (allthirst))
    print("overall %d creatures died from thirst and famine" % (allthirstfamine))
    print("overall %d creatures died from fights" % (allfights))


def deaths():
    global famine
    global thirst
    global thirstfamine
    global fights
    global allfamine
    global allthirst
    global allthirstfamine
    global allfights
    print("%d creatures died from famine" % (famine))
    print("%d creatures died from thirst" % (thirst))
    print("%d creatures died from thirst and famine" % (thirstfamine))
    print("%d creatures died from fights" % (fights))
    allfamine += famine
    allthirst += thirst
    allthirstfamine += thirstfamine
    allfights += fights
    famine = 0
    thirst = 0
    thirstfamine = 0
    fights = 0
    froze = 0
    heatstroke = 0


def listclear():
    speedlist.clear()
    weightlist.clear()
    staminalist.clear()
    templist.clear()
    senselist.clear()


class creature:
    alive = 0
    stamina = 0  # max:7000#
    water = 0
    grass = 0  # max:1000#
    sense = 0
    weight = 0  # max:1000##effects speed and also is the main factor for if they fight or not#
    speed = 0
    strength = 0
    staminareq = 0
    temperature = 0

    def speedstats(self):
        speedlist.append(self.speed)

    def weightstats(self):
        weightlist.append(self.weight)

    def staminastats(self):
        staminalist.append(self.stamina)

    def tempstats(self):
        templist.append(self.temperature)

    def sensestats(self):
        senselist.append(self.sense)

    def alivestats(self):
        speedlist.append(self.speed)
        weightlist.append(self.weight)
        staminalist.append(self.stamina)
        templist.append(self.temperature)
        senselist.append(self.sense)

    def finalstats(self):
        finalstatslist.append(self.temperature)
        finalstatslist.append(self.speed)
        finalstatslist.append(self.weight)
        finalstatslist.append(self.sense)
        finalstatslist.append('next creature')

    def settemp(self, x, y):
        tempweight = self.weight // 10
        temptemp = earthlist[x][y].temperature + 50
        if temptemp < 33:
            temptemp = 1
        else:
            if temptemp > 66:
                temptemp = 3
            else:
                temptemp = 2
        if tempweight < 33:
            tempweight = 1
        else:
            if tempweight > 66:
                tempweight = 3
            else:
                tempweight = 2
        tempbody = tempweight + temptemp
        if (tempbody == 6) or (tempbody == 2):
            self.temperature = -1
        else:
            if (tempbody == 5) or (tempbody == 3):
                self.temperature = 0
            else:
                if tempbody == 4:
                    self.temperature = 1

    def senseprob(self):
        return self.sense // 10

    def generatestamina(self):
        global famine
        global thirst
        global thirstfamine
        self.stamina += (self.grass * 500) + (self.water * 500)
        if self.water == 0:
            self.stamina = 0
        if self.grass == 0:
            self.stamina = 0
        if self.staminareq > self.stamina:
            if self.grass * 400 == self.water * 400:
                thirstfamine += 1
            else:
                if self.grass * 400 > self.water * 400:
                    thirst += 1
                    self.stamina = 0
                else:
                    famine += 1
                    self.stamina = 0
        self.grass = 0
        self.water = 0
        self.stamina = self.stamina - subtractstamina

    def checkeatfood(self, x, y):
        if earthlist[x][y].grass > 0:
            earthlist[x][y].grass = earthlist[x][y].grass - 1
            self.grass += 1
        if earthlist[x][y].water == 1:
            self.water += 1

    def generatestats(self):
        statmin = 1
        statmax = 1000
        self.stamina = 5000
        statrand = r.randint(statmin, statmax)
        self.weight = statrand
        statrand = r.randint(statmin, statmax)
        self.speed = statrand

    def evolve(self, wx, wy):
        global evolvepercent
        #-10 ve +10 arasinda ve her stata olucak, ayni zamanda stamina required degisicegi icin weight le speed unrelated olucak unun disinda herseyin maxi 1000#
        j = 0
        i = 0
        evolvepercent = 80
        evolvechance = r.randint(0, 100)
        j = r.randint(0, 2)
        while j >= i:
            if evolvechance < evolvepercent:
                statrand = r.randint(-10, 10)
                self.weight = self.weight + statrand
                if self.weight < 1:
                    self.weight = 1
                if self.weight > 1000:
                    self.weight = 1000
                statrand = r.randint(-10, 10)
                self.speed = self.speed + statrand
                if self.speed < 1:
                    self.speed = 1
                if self.speed > 1000:
                    self.speed = 1000
                statrand = r.randint(-10, 10)
                self.sense = self.sense + statrand
                if self.sense < 1:
                    self.sense = 1
                if self.sense > 1000:
                    self.sense = 1000
            if j == 1:
                if i == 0:
                    movement(wx, wy)
            i += 1

    def calculateall(self, wx, wy):
        self.findstamreq
        self.findstrength
        self.checkeatfood(wx, wy)
        if self.stamina == 0:
            self.reset()
            creaturelist[wx][wy].finalstats()

    def findstamreq(self):
        if self.temperature == -1:
            self.staminareq = (self.weight * 3) + (self.speed * 4) + (self.sense * 2) * 10000
        else:
            if self.temperature == 0:
                self.staminareq = (self.weight * 3) + (self.speed * 4) + (self.sense * 2) + 1000
            else:
                self.staminareq = (self.weight * 3) + (self.speed * 4) + (self.sense * 2)

    def loadstats(self, old):
        self.alive = old.alive
        self.stamina = old.stamina
        self.water = old.water
        self.sense = old.sense
        self.weight = old.weight
        self.speed = old.speed
        self.strength = old.strength
        self.staminareq = old.staminareq
        self.temperature = old.temperature

    def reset(self):
        self.alive = 0
        self.stamina = 0
        self.water = 0
        self.sense = 0
        self.weight = 0
        self.speed = 0
        self.strength = 0
        self.staminareq = 0
        self.temperature = 0

    def findstrength(self):
        sta = self.stamina
        spe = self.strength
        wei = self.weight
        self.strength = (sta * 5) * (spe * 4) * (wei * 3) * self.alive

# def seewater(skill):
    # distmax = 10
   # rand =
   # dist = int(skill*(distmax/sightmax))


def fight(attackx, attacky, defensex, defensey):
    ax = attackx
    ay = attacky
    dx = defensex
    dy = defensey
    if creaturelist[ax][ay].strength > creaturelist[dx][dy].strength:
        creaturelist[dx][dy].loadstats(creaturelist[ax][ay])
        creaturelist[ax][ay].reset()
        creaturelist[dx][dy].finalstats()
    else:
        creaturelist[ax][ay].reset()
        creaturelist[dx][dy].finalstats()
    global fights
    fights += 1


def checkcreature(px, py, x, y):
    z = 0
    if creaturelist[x][y].alive == 1:
        fight(px, py, x, y)
        z = 1
    return z


def printcreatures1():
    newline = 0
    shape = ['.', '#']
    for pwy in range(earthmulty):
        for pwx in range(earthmultx):
            if pwy == newline:
                print('[%d,%d]' % (creaturelist[pwx][pwy].alive, creaturelist[pwx][pwy].stamina), end="")
            else:
                newline = newline + 1
                print('')
                print('[%d,%d]' % (creaturelist[pwx][pwy].alive, creaturelist[pwx][pwy].stamina), end="")

    print('')
# circle = App.w.create_oval(0,0,20,20)


def printcreatures():
    newline = 0
    shape = ['.', '#']
    for pwy in range(earthmulty):
        for pwx in range(earthmultx):
            if pwy == newline:
                print(creaturelist[pwx][pwy].alive, end="")
            else:
                newline = newline + 1
                print('')
                print(creaturelist[pwx][pwy].alive, end="")
        print('')


class cell:
    surface = sfdirt
    water = 0
    grass = 0
    dirt = 0
    temperature = 0


def printwater():
    newline = 0
    watershape = ['.', '#']
    for pwy in range(earthmulty):
        for pwx in range(earthmultx):
            if pwy == newline:
                print(earthlist[pwy][pwx].water, end="")
            else:
                newline = newline + 1
                print('')
                print(earthlist[pwy][pwx].water, end="")
    print('')



#this is to create the play area#
a = cell()
earthlist = [a] * earthmulty
for i in range(earthmulty):
    earthlist[i] = [a] * earthmultx
#this is the water#
for x in range(earthmultx):
    for y in range(earthmulty):
        a = cell()
        earthlist[x][y] = a


def cellcreate():
    global WOwater
    global WIwaterchance
    global earthlist
    global earthmultx
    global earthmulty
    global temperature
    for x in range(earthmultx):
        for y in range(earthmulty):
            earthlist[x][y].grass = 0
            earthlist[x][y].water = 0
            earthlist[x][y].temperature = 0
    for x in range(earthmultx):
        for y in range(earthmulty):
            earthlist[x][y].temperature = temperature
            WOwater = r.randint(0, 100)
            WIwaterchance = waterscale.get()
            if earthlist[x - 1][y].water == 1:
                WIwaterchance = WIwaterchance + 15
            if earthlist[x][y - 1].water == 1:
                WIwaterchance = WIwaterchance + 15
            if WOwater < WIwaterchance:
                earthlist[x][y].water = 1
            else:
                grassstarter = grassscale.get()
                earthlist[x][y].grass = grassstarter


cellcreate()

#this is to create the creature grid#
a = creature()
creaturelist = [a] * earthmulty
for i in range(earthmulty):
    creaturelist[i] = [a] * earthmultx
#this is for spawning the creatures#
for x in range(earthmultx):
    for y in range(earthmulty):
        a = creature()
        creaturelist[x][y] = a


def creaturecreate():
    global creaturelist
    global WOcreature
    global creaturechance
    global earthmultx
    global earthmulty
    for x in range(earthmultx):
        for y in range(earthmulty):
            creaturelist[x][y].alive = 0
            creaturelist[x][y].reset()
    for x in range(earthmultx):
        for y in range(earthmulty):
            WOcreature = r.randint(0, 100)
            creaturechance = 25
            creaturechance = creaturescale.get()
            if creaturelist[x - 1][y].alive == 1:
                creaturechance = 0
            if creaturelist[x][y - 1].alive == 1:
                creaturechance = 0
            if WOcreature < creaturechance:
                creaturelist[x][y].alive = 1


creaturecreate()


printcreatures()

# x = 0
# y = 0
# while x < earthmultx:
#    x += 1
#    while y < earthmulty:
#        y += 1
#        if creaturelist[x][y].alive == 1:
#            creaturelist[x][y].alive = 0
#            if x == earthmultx - 1:
#                pass
#            else:
#                creaturelist[x + 1][y].alive = 1

##WHILE LOOP KULLAN## ##WHILE LOOP KULLAN## ##WHILE LOOP KULLAN## ##WHILE LOOP KULLAN## ##WHILE LOOP KULLAN## ##WHILE LOOP KULLAN## ##WHILE LOOP KULLAN## ##WHILE LOOP KULLAN##
##WHILE LOOP KULLAN## ##WHILE LOOP KULLAN## ##WHILE LOOP KULLAN## ##WHILE LOOP KULLAN## ##WHILE LOOP KULLAN## ##WHILE LOOP KULLAN## ##WHILE LOOP KULLAN## ##WHILE LOOP KULLAN##


wx = 0
wy = 0
i = 0
runtimeto = 10
runtime = 0
evolvecount = 0
evolvecountto = 25
evolvecheck = 1
staminaloop = 10
allalive = 0
totalroundcount = 0
populationcounter = 0
while (evolvecount < evolvecountto):
    runtime = 0
    while (runtime < runtimeto):
        if runtime == 1:
            graph_data = open('example.txt', 'a')
            graph_data.write("%d,%d\n" % (totalroundcount, populationcounter))
            totalroundcount = totalroundcount + 1
            populationcounter = 0
            graph_data.close()
        while ispause == 1:
            if nexttime == 1:
                ispause = 0
        if nexttime == 1:
            ispause = 1
            nexttime = 0
            makinguparandomnumber = 1
        deathstatslist.append(allalive)
        allalive = 0
        checkallalive = 0
        populationcounter = 0
        wy = 0
        listclear()
        while wy < earthmulty:
            wx = 0
            while wx < earthmultx:
                i = 0
                if earthlist[wx][wy].grass < 20:
                    grasschance = r.randint(0, 100)
                    grassincreasechance = grasspercentscale.get()
                    if grasschance < grassincreasechance:
                        earthlist[wx][wy].grass += 1
                if creaturelist[wx][wy].alive == 1:
                    populationcounter += 1
                    creaturelist[wx][wy].alivestats()
                    allalive += 1
                    if runtime == staminaloop:
                        if staminaloop > runtimeto - 10:
                            staminaloop = 0
                        else:
                            creaturelist[wx][wy].generatestamina()
                    if evolvecount == 0:
                        if runtime == 0:
                            creaturelist[wx][wy].generatestats()
                    else:
                        if evolvecount == evolvecheck:
                            if runtime > 0:
                                evolvecheck += 1
                            else:
                                creaturelist[wx][wy].evolve(wx, wy)
                    creaturelist[wx][wy].calculateall(wx, wy)
                    sensechance = creaturelist[wx][wy].senseprob()
                    creaturelist[wx][wy].settemp(wx, wy)
                    chanceto = r.randint(0, 100)
                    if chanceto < 50:
                        gotime = 0
                        chanceto = r.randint(0, 100)
                        if sensechance > chanceto:
                            gotime = 1
                        else:
                            gotime = 0
                    else:
                        gotime = 1
                    if gotime == 1:
                        if wx + 1 == earthmultx and wy + 1 == earthmulty:
                            chance = r.randint(0, 1)
                            if chance == 0:
                                z = checkcreature(wx, wy, wx - 1, wy)
                                if z == 0:
                                    creaturelist[wx - 1][wy].loadstats(creaturelist[wx][wy])
                                    creaturelist[wx][wy].reset()
                            if chance == 1:
                                z = checkcreature(wx, wy, wx, wy - 1)
                                if z == 0:
                                    creaturelist[wx][wy - 1].loadstats(creaturelist[wx][wy])
                                    creaturelist[wx][wy].reset()
                            i = 1
                        if wx - 1 == -1 and wy - 1 == -1:
                            chance = r.randint(0, 1)
                            if chance == 0:
                                z = checkcreature(wx, wy, wx + 1, wy)
                                if z == 0:
                                    creaturelist[wx + 1][wy].loadstats(creaturelist[wx][wy])
                                    creaturelist[wx][wy].reset()
                                wx += 1
                            if chance == 1:
                                z = checkcreature(wx, wy, wx, wy + 1)
                                if z == 0:
                                    creaturelist[wx][wy + 1].loadstats(creaturelist[wx][wy])
                                    creaturelist[wx][wy].reset()
                            i = 1
                        if wx - 1 == -1 and wy + 1 == earthmulty:
                            chance = r.randint(0, 1)
                            if chance == 0:
                                z = checkcreature(wx, wy, wx + 1, wy)
                                if z == 0:
                                    creaturelist[wx + 1][wy].loadstats(creaturelist[wx][wy])
                                    creaturelist[wx][wy].reset()
                                wx += 1
                            if chance == 1:
                                z = checkcreature(wx, wy, wx, wy - 1)
                                if z == 0:
                                    creaturelist[wx][wy - 1].loadstats(creaturelist[wx][wy])
                                    creaturelist[wx][wy].reset()
                            i = 1
                        if wx + 1 == earthmultx and wy - 1 == -1:
                            chance = r.randint(0, 1)
                            if chance == 0:
                                z = checkcreature(wx, wy, wx - 1, wy)
                                if z == 0:
                                    creaturelist[wx - 1][wy].loadstats(creaturelist[wx][wy])
                                    creaturelist[wx][wy].reset()
                            if chance == 1:
                                z = checkcreature(wx, wy, wx, wy + 1)
                                if z == 0:
                                    creaturelist[wx][wy + 1].loadstats(creaturelist[wx][wy])
                                    creaturelist[wx][wy].reset()
                            i = 1
                        if i == 0:
                            if wx + 1 == earthmultx:
                                chance = r.randint(0, 2)
                                if chance == 0:
                                    z = checkcreature(wx, wy, wx - 1, wy)
                                    if z == 0:
                                        creaturelist[wx - 1][wy].loadstats(creaturelist[wx][wy])
                                        creaturelist[wx][wy].reset()
                                if chance == 1:
                                    z = checkcreature(wx, wy, wx, wy + 1)
                                    if z == 0:
                                        creaturelist[wx][wy + 1].loadstats(creaturelist[wx][wy])
                                        creaturelist[wx][wy].reset()
                                if chance == 2:
                                    z = checkcreature(wx, wy, wx, wy - 1)
                                    if z == 0:
                                        creaturelist[wx][wy - 1].loadstats(creaturelist[wx][wy])
                                        creaturelist[wx][wy].reset()
                                i = 1
                            if wy + 1 == earthmulty:
                                chance = r.randint(0, 2)
                                if chance == 0:
                                    z = checkcreature(wx, wy, wx - 1, wy)
                                    if z == 0:
                                        creaturelist[wx - 1][wy].loadstats(creaturelist[wx][wy])
                                        creaturelist[wx][wy].reset()
                                if chance == 1:
                                    z = checkcreature(wx, wy, wx + 1, wy)
                                    if z == 0:
                                        creaturelist[wx + 1][wy].loadstats(creaturelist[wx][wy])
                                        creaturelist[wx][wy].reset()
                                    wx += 1
                                if chance == 2:
                                    z = checkcreature(wx, wy, wx, wy - 1)
                                    if z == 0:
                                        creaturelist[wx][wy - 1].loadstats(creaturelist[wx][wy])
                                        creaturelist[wx][wy].reset()
                                i = 1
                            if wx - 1 == -1:
                                chance = r.randint(0, 2)
                                if chance == 0:
                                    z = checkcreature(wx, wy, wx + 1, wy)
                                    if z == 0:
                                        creaturelist[wx + 1][wy].loadstats(creaturelist[wx][wy])
                                        creaturelist[wx][wy].reset()
                                    wx += 1
                                if chance == 1:
                                    z = checkcreature(wx, wy, wx, wy + 1)
                                    if z == 0:
                                        creaturelist[wx][wy + 1].loadstats(creaturelist[wx][wy])
                                        creaturelist[wx][wy].reset()
                                if chance == 2:
                                    z = checkcreature(wx, wy, wx, wy - 1)
                                    if z == 0:
                                        creaturelist[wx][wy - 1].loadstats(creaturelist[wx][wy])
                                        creaturelist[wx][wy].reset()
                                i = 1
                            if wy - 1 == -1:
                                chance = r.randint(0, 2)
                                if chance == 0:
                                    z = checkcreature(wx, wy, wx - 1, wy)
                                    if z == 0:
                                        creaturelist[wx - 1][wy].loadstats(creaturelist[wx][wy])
                                        creaturelist[wx][wy].reset()
                                if chance == 1:
                                    z = checkcreature(wx, wy, wx, wy + 1)
                                    if z == 0:
                                        creaturelist[wx][wy + 1].loadstats(creaturelist[wx][wy])
                                        creaturelist[wx][wy].reset()
                                if chance == 2:
                                    z = checkcreature(wx, wy, wx + 1, wy)
                                    if z == 0:
                                        creaturelist[wx + 1][wy].loadstats(creaturelist[wx][wy])
                                        creaturelist[wx][wy].reset()
                                    wx += 1
                                i = 1
                        #This is for movement#
                        if i == 0:
                            chance = r.randint(0, 3)
                            if chance == 0:
                                z = checkcreature(wx, wy, wx + 1, wy)
                                if z == 0:
                                    creaturelist[wx + 1][wy].loadstats(creaturelist[wx][wy])
                                    creaturelist[wx][wy].reset()
                                wx += 1
                            if chance == 1:
                                z = checkcreature(wx, wy, wx - 1, wy)
                                if z == 0:
                                    creaturelist[wx - 1][wy].loadstats(creaturelist[wx][wy])
                                    creaturelist[wx][wy].reset()
                            if chance == 2:
                                z = checkcreature(wx, wy, wx, wy + 1)
                                if z == 0:
                                    creaturelist[wx][wy + 1].loadstats(creaturelist[wx][wy])
                                    creaturelist[wx][wy].reset()
                            if chance == 3:
                                z = checkcreature(wx, wy, wx, wy - 1)
                                if z == 0:
                                    creaturelist[wx][wy - 1].loadstats(creaturelist[wx][wy])
                                    creaturelist[wx][wy].reset()
                wx += 1
            wy += 1
        print("")
        printcreatures()

        if reloadready == 1:
            if squareready == 1:
                reloadsquares()
                squareready = 0
            reloadcircle()

        #    reloadready = 0\

        runtime += 1
        if allalive < 2:
            print('evolvecount:%d, runtime:%d' % (evolvecount, runtime))
            runtime = runtimeto
            evolvecount = evolvecountto
        turncountlabel.config(text="Evolution Count: %d \nRound Count: %d" % (evolvecount, runtime))
    evolvecount += 1
    evolvecountto += 1
    deaths()
    print('')
alldeaths()
print(deathstatslist)
print(allalive)
print(finalstatslist)
print('stamina')
print(staminalist)
print('weight')
print(weightlist)
print('speed')
print(speedlist)
print('sense')
print(senselist)
print('temperature')
print(templist)
# printwater()
lengthoflist = len(deathstatslist)
i = 0
while i < lengthoflist:
    print(deathstatslist[i])
    i += 1
