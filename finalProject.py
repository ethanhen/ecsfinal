#TextGame
#finalProject.py
#Ethan Hensley 
#ethensle
#3

from random import *
from graphics import *
from random import *





class Item:

    def __init__(self,name):
        self.name=name

    def add(self,amount=1):

        save = open('savegame.txt', 'r')
        saveData = save.readlines()
        save.close()

        if (self.name+'\n') in saveData:
            x = saveData.index((self.name+'\n'))
            saveData[x+1] = amount + int(saveData[x+1])
            saveData[x+1] = str(saveData[x+1]) + '\n'
            save = open('savegame.txt', 'w')

            for x in saveData:
                
                save.write(x)
            save.close()

        else:
            save = open('savegame.txt', 'a+')
            save.write('\n'+self.name+'\n'+str(amount))

    def drop(self,amount=1):

        save = open('savegame.txt', 'r')
        saveData = save.readlines()
        save.close()

        if (self.name+'\n') in saveData:
            x = saveData.index((self.name+'\n'))
            a = int(saveData[x+1]) - amount
            saveData[x+1] = str(a) + '\n'
            save = open('savegame.txt', 'w')

            for x in saveData:
                
                save.write(x)
            save.close()

        else:
            return 0

    def check(self):

        save = open('savegame.txt', 'r')
        saveData = save.readlines()
        save.close()

        if (self.name+'\n') in saveData:
            return 1
        else:
            return 0

class Player:

    def __init__(self):
        self.location_x, self.location_y = -1,0

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(1)
        print(roomtext(self.location_x, self.location_y))

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)


def roomtext(x,y):
    if x == -1 and y == 0:
        return "You are standing west of a run-down shack. There is nothing to the North, West, or South."
    elif x == 0 and y== 0:
        return "You enter the shack. There are doors to your North, South, and East. A sword lays at your feet."
    elif x == 0 and y== 1:
        return "Behind the door lurks an evil troll."
    elif x == 1 and y== 0:
        return "Some coins, long forgotten, sit on the floor."
    elif x == 0 and y== -1:
        return "The passage extends further to the South."
    elif x == 0 and y==-2:
        return "A grotesque spider drops from the ceiling above. You can see an exit beyond it."
    elif x == 0 and y== -3:
        return "You have exited the house. Thanks for playing!"


def saveGameCheck():
    file = open('savegame.txt', 'r')
    saveData = file.readlines()
    file.close()

    #0 is a new game, 1 is a existing game
    if int(saveData[0]) == 0:
        return 0
    elif int(saveData[0]) == 1:
        return 1

def menuScreen(win):
    title = Text(Point(0,7), 'Welcome to TextGame!')
    title.setSize(36)
    title.setTextColor('white')
    title.draw(win)

    startButton = Rectangle(Point(-2.5,2), Point(2.5,4.5))
    startButton.setFill('gray')
    startButton.draw(win)
    startButtonLabel = Text(Point(0,3.25), 'New Game')
    startButtonLabel.setSize(20)
    startButtonLabel.draw(win)

    endButton = Rectangle(Point(-2,-8), Point(2,-6))
    endButton.setFill('gray')
    endButton.draw(win)
    endButtonLabel = Text(Point(0,-7), 'Close')
    endButtonLabel.setSize(20)
    endButtonLabel.draw(win)

    if saveGameCheck() == 1:
        loadButton = Rectangle(Point(-2.5,-1.5), Point(2.5,1))
        loadButton.setFill('gray')
        loadButton.draw(win)
        loadButtonLabel = Text(Point(0,-0.25), 'Load Game')
        loadButtonLabel.setSize(20)
        loadButtonLabel.draw(win)

    return 0
def cls(win):
    for item in win.items[:]:
        item.undraw()
    win.update()
def checkMenuClick(win):

    click = win.getMouse()
    x=click.getX()
    y=click.getY()

    if(-2.5 <= x <= 2.5 and 2 <= y <= 4.5):
        return 1
    elif(-2.5 <= x <= 2.5 and -1.5 <= y <= 1 and os.stat("savegame.txt").st_size != 0):
        return 2
    elif(-2 <= x <= 2 and -8 <= y <= -6):
        return 3
    else:
        return 0
def checkNewGameClick(win):

    #IMS
    click = win.getMouse()
    x=click.getX()
    y=click.getY()

    if(-2.6 <= x <= -0.1 and -5 <= y <= -4):
        return 1
    elif(0.1 <= x <= 2.6 and -5 <= y <= -4):
        return 2
    else:
        return 0
def checkGoClick(win):

    click = win.getMouse()
    x=click.getX()
    y=click.getY()

    if(8.5 <= x <= 11.75 and -8.5 <= y <= -7):
        return 1
    else:
        return 0
def gameScreen(win,savestate):
    terminal = Rectangle(Point(-15.5,-6.5), Point(8,8.5))
    terminal.setFill('black')
    terminal.setOutline('white')
    terminal.setWidth(5)
    terminal.draw(win)

    map = Rectangle(Point(8.5,3), Point(15.5,8.5))
    map.setFill('black')
    map.setOutline('white')
    map.setWidth(5)
    map.draw(win)

    inv = Rectangle(Point(8.5,-6.5), Point(15.5,2.5))
    inv.setFill('black')
    inv.setOutline('white')
    inv.setWidth(5)
    inv.draw(win)

    entryBox = Rectangle(Point(-15.5,-8.5), Point(8,-7))
    entryBox.setFill('black')
    entryBox.setOutline('white')
    entryBox.setWidth(5)
    entryBox.draw(win)

    go = Rectangle(Point(8.5,-8.5), Point(11.75,-7))
    go.setFill('grey')
    go.draw(win)

    goText = Text(Point(10.125,-7.75), 'GO')
    goText.setSize(20)
    goText.draw(win)

    if savestate==1:
        save = Rectangle(Point(12.25,-8.5), Point(15.5,-7))
        save.setFill('grey')
        save.draw(win)

        saveText = Text(Point(13.875,-7.75), 'Save Game')
        saveText.setSize(18)
        saveText.draw(win)

    entry = Entry(Point(-3.75,-7.75), 100)
    entry.draw(win)

    return entry
def warning(win):

    warning = Text(Point(0,-3), 'Warning! This will erase your current savegame! Are you sure you want to continue?')
    warning.setFill('red')
    warning.setSize(20)
    warning.draw(win)

    yesButton = Rectangle(Point(-2.6,-5), Point(-0.1,-4))
    yesButton.setFill('gray')
    yesButton.draw(win)
    yesButtonLabel = Text(Point(-1.35,-4.5), 'Yes')
    yesButtonLabel.setSize(18)
    yesButtonLabel.draw(win)

    noButton = Rectangle(Point(0.1,-5), Point(2.6,-4))
    noButton.setFill('gray')
    noButton.draw(win)
    noButtonLabel = Text(Point(1.35,-4.5), 'No')
    noButtonLabel.setSize(20)
    noButtonLabel.draw(win)
def getText(win,entry):
    #IEB
    text=entry.getText()

    return text
def playerAlive():
    #IFL
    file = open('savegame.txt', 'r')
    data = file.readlines()
    file.close()
    
    data = [x.replace('\n', '') for x in data]

    index = data.index('health')

    if int(data[index+1]) > 0:
        return 1
    elif int(data[index+1]) <= 0:
        return 0

def printer(win,output,type,count):

    #OTXT
    if type == -1:

        game='>>>{0:<100}'.format(output)

        out = Text(Point(-3.75,8-count),game)
        out.setSize(11)
        out.setFace('courier')
        out.setFill('white')
        out.draw(win)

    if type == 1:

        game='{0:<102}'.format(output)

        out = Text(Point(-3.75,8-count),game)
        out.setSize(11)
        out.setFace('courier')
        out.setFill('white')
        out.draw(win)

    return 0
def game(win,load,text,count):
    printer(win,text,1,count/2)
    out = parse(win,text)
    printer(win,out,-1,(count/2)+0.5)     
def resetSave():
    #OFL
    file = open('savegame.txt', 'w')
    file.write('0\nhealth\n10')
    file.close()

    return 0
def parse(win,input):

    inList = input.split(' ')

    if 'the' in inList:
        inList.remove('the')
    if 'a' in inList:
        inList.remove('a')
    if 'with' in inList:
        inList.remove('with')


    if 'take' in inList:
        name = inList[len(inList)-1]

        a = Item(name)

        a.add()

        out = 'You take the '+name

        return out

    elif 'move' in inList:
        direction = inList[len(inList)-1]

        if direction == 'east':
            a = Player().move_east()
            print(a)
            return str()
        elif direction == 'north':
            return str(Player().move_north)
        elif direction == 'west':
            return str(Player().move_west)
        elif direction == 'south':
            return str(Player().move_south)

    elif 'drop' in inList:
        name = inList[len(inList)-1]

        a = Item(name)

        a.drop()

        out = 'You dropped your '+name

        return out

    elif 'kill' in inList:
        target = inList[len(inList)-2]
        weapon = inList[len(inList)-1]

        print(target,weapon)

        a = Item(weapon)

        if a.check() == 1:

            out = 'You kill '+target+' with '+weapon

            return out

        else:
            out = "You don't have a "+weapon+'!'

            return out

    else:
        out = "Sorry, I don't understand that yet."

        return out
def changeGameState():

    save = open('savegame.txt', 'r')
    saveData = save.readlines()
    save.close()

    saveData[0]='1\n'

    save = open('savegame.txt', 'w')

    for x in saveData:

        save.write(x)
def invPrint(win):

    save = open('savegame.txt', 'r')
    saveData = save.readlines()
    save.close()

    saveData = [x.replace('\n', '') for x in saveData]

    saveData.pop(0)

    text = 'Health: '+saveData[1]
    text1 = '{0:<30}'.format(text)

    out = Text(Point(12.25,2),text1)
    out.setSize(11)
    out.setFace('courier')
    out.setFill('white')
    out.draw(win)

    saveData.pop(0)
    saveData.pop(0)

    if len(saveData) != 0:

        for i in range(0,len(saveData),2):

            text = saveData[i]+': '+saveData[i+1]

            text1 = '{0:<30}'.format(text)

            out = Text(Point(12.25,(1.5-(i/4))),text1)
            out.setSize(11)
            out.setFace('courier')
            out.setFill('white')
            out.draw(win)

    return out
        

def main():
    #GW
    win=GraphWin('Text Game', 1280,720)
    win.setBackground('black')
    win.setCoords(-16,-9,16,9)

    #FNC
    menuScreen(win)

    closeGame=0

    go=0

    text=''

    while(closeGame==0):

        clickValue=0

        while(clickValue==0):
            clickValue = checkMenuClick(win)

        #new game with savegame
        if clickValue==1 and saveGameCheck() == 1:
            
            warning(win)

            clickValueNext=0

            while(clickValueNext==0):
                clickValueNext=checkNewGameClick(win)

            #override savegame and start new game
            if clickValueNext==1:
                resetSave()
                cls(win)
                changeGameState()
                eb = gameScreen(win,1)

                printer(win,roomtext(-1,0),-1,0)
                while playerAlive() == 1:

                    for i in range(1,28,2):
                    
                        items = invPrint(win)

                    

                        while go == 0:
                            go=checkGoClick(win)
                        go=0
                        text = getText(win,eb)
                        game(win,0,text,i)

                    cls(win)
                    eb = gameScreen(win,1)
            
            #go back to main menu
            elif clickValueNext==2:
                cls(win)
                menuScreen(win)

        #new game with no savegame
        elif clickValue==1:
            cls(win)
            changeGameState()
            eb = gameScreen(win,1)
            
            printer(win,room['0'],-1,0)
            while playerAlive() == 1:

                for i in range(1,28,2):
                    
                    items = invPrint(win)

                    

                    while go == 0:
                        go=checkGoClick(win)
                    go=0
                    text = getText(win,eb)
                    game(win,0,text,i)

                cls(win)
                eb = gameScreen(win,1)

        #load game
        elif clickValue==2:
            cls(win)
            changeGameState()
            eb = gameScreen(win,1)
            
            printer(win,room['0'],-1,0)
            while playerAlive() == 1:

                for i in range(1,28,2):
                    
                    items = invPrint(win)

                    

                    while go == 0:
                        go=checkGoClick(win)
                    go=0
                    text = getText(win,eb)
                    game(win,0,text,i)

                cls(win)
                eb = gameScreen(win,1)

        elif clickValue==3:
            win.close()    

main() 