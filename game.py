# -*- coding: utf-8 -*-

import sys
import pygame
from random import randint

#Game Initialization
pygame.init()

house = pygame.image.load("house.png")
start = pygame.image.load("start.png")
snacks = pygame.image.load("snacks.png")
fuel = pygame.image.load("fuel.png")
hotel = pygame.image.load("hotel.png")
dice = pygame.image.load("dice.png")
hanuman = pygame.image.load("hanuman.png")
ice = pygame.image.load("ice.png")
pool = pygame.image.load("pool.png")
signal = pygame.image.load("signal.png")
horse = pygame.image.load("horse.png")
taj = pygame.image.load("taj.png")
boat = pygame.image.load("boat.png")
shopping = pygame.image.load("shopping.png")
car = pygame.image.load("car.png")
traffic = pygame.image.load("traffic.png")
helicopter = pygame.image.load("helicopter.png")


boardWidth = 1300
boardHeight = 650

boxWidth = 80
boxHeight = 50

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (225,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)
BLUE = (0,0,225)
PURPLE = (255,20,255)

mousex = 0                   # x co-ordinate of the point where mouse is clicked
mousey = 0                   # y co-ordinate of the point where mouse is clicked
mouseclicked = False
mc = 0
movebutton = 0               # Button To Be Moved
p_id = 1                     # Variable To hold the turn of the player
i = 0                        # Variable helps in movement of Button
n = 0                        # Variable tells the number that appered while rolling dice
flagIMP = 0
 
c = pygame.time.Clock()      # Create A Clock Object For Timing
b = 0
tick = 20
In = 1

track = [(802,605),(721,605),(640,605),(559,605),(559,555),(559,505),(559,455),(478,455),(397,455),
         (397,505),(397,555),(397,605),(316,605),(235,605),(154,605),(73,605),(73,555),(73,505),
         (73,455),(73,405),(73,355),(73,305),(73,255),(73,205),(73,155),(73,105),(73,55),(154,55),
         (235,55),(316,55),(397,55),(478,55),(559,55),(640,55),(721,55),(721,105),(802,105),(883,105),
         (883,155),(883,205),(802,205),(721,205),(640,205),(559,205),(478,205),(397,205),(316,205),
         (235,205),(235,255),(235,305),(216,305),(397,305),(478,305),(559,305),(640,305),(721,305),
         (802,305),(883,305),(883,355),(883,405),(883,455),(883,505)]

#Creating A window And Giving Title Picnic
win = pygame.display.set_mode((boardWidth,boardHeight))
pygame.display.set_caption("PICNIC")
surf = pygame.Surface((boardWidth,boardHeight),1)

#Function To write
def renderText(string,cx,cy,fontSize,color):
    fontObj = pygame.font.Font("freesansbold.ttf",fontSize)
    textWinObj = fontObj.render(string,True,color)
    textRectObj = textWinObj.get_rect()
    textRectObj.center = (cx,cy)
    win.blit(textWinObj,textRectObj)
    
#Function To Show Roll Button
def showButtonRoll():
    pygame.draw.rect(win,WHITE,(1050,450,200,40))
    renderText("Roll",1150,470,32,BLACK)

#Functio To Show Move Button
def showButtonMove():
    pygame.draw.rect(win,WHITE,(1050,550,200,40))
    renderText("Move",1150,570,32,BLACK)

#Functio to show number that appered on dice
def showDiceBox(n):
    pygame.draw.rect(win,WHITE,(1050,400,200,40))
    renderText(str(n),1150,420,32,BLACK)

#Function to show players turn
def showTurnBox(n):
    pygame.draw.rect(win,WHITE,(1050,10,200,40))
    pygame.draw.rect(win,WHITE,(1050,10,200,40),1)
    pygame.draw.line(win,BLACK,(1170,10),(1170,50),1)
    renderText("Turn",1100,30,32,BLACK)
    renderText("P"+str(n),1210,30,32,BLACK)

#Function to draw Picnic Board        
def drawBoard():
    # Draw Board Outline
    pygame.draw.rect(win,RED,[0,0,5,boardHeight])
    pygame.draw.rect(win,RED,[995,0,5,boardHeight])
    pygame.draw.rect(win,RED,[5,boardHeight-5,995,5])
    pygame.draw.rect(win,RED,[5,0,995,5])
    
    #Draw Initial Position
    pygame.draw.rect(win,WHITE,(853,535,100,100))
    
    #Draw House
    win.blit(house,(712,452))
    #Draw Start
    win.blit(start,(600,530))
    #Draw Snacks
    win.blit(snacks,(468,530))
    #Draw Petrol Pump
    win.blit(fuel,(438,380))
    #Draw Hotel 
    win.blit(hotel,(114,530))
    #Draw Dice
    win.blit(dice,(257,480))
    #Draw Temple
    win.blit(hanuman,(114,380))
    #Draw Ice Cream
    win.blit(ice,(114,180))
    #Draw Pool Table
    win.blit(pool,(113,80))
    #Draw Signal
    win.blit(signal,(205,80))
    #Draw Horse
    win.blit(horse,(530,80))
    #Draw Taj Mahal
    win.blit(taj,(775,130))
    #Draw Boat
    win.blit(boat,(681,130))
    #Draw Shopping
    win.blit(shopping,(400,85))
    #Draw Car
    win.blit(car,(276,230))
    #Draw Petrol Pump
    win.blit(fuel,(357,330))
    #Draw Helicoptar
    win.blit(helicopter,(681,235))
    #Draw Traffic
    win.blit(traffic,(621,330))
    
    my_list = [(762,580,BLUE),(681,580,BLUE),(600,580,BLUE),(519,580,BLUE),(519,530,WHITE),
               (519,480,BLUE),(519,430,BLUE),(438,430,WHITE),(357,430,BLUE),(357,480,BLUE),
               (357,530,WHITE),(357,580,BLUE),(276,580,WHITE),(195,580,BLUE),(114,580,BLUE),
               (33,580,BLUE),(33,530,WHITE),(33,480,BLUE),(33,430,BLUE),(33,380,WHITE),(33,330,BLUE),
               (33,280,BLUE),(33,230,BLUE),(33,180,WHITE),(33,130,BLUE),(33,80,BLUE),(33,30,WHITE),
               (114,30,BLUE),(195,30,WHITE),(276,30,BLUE),(357,30,BLUE),(438,30,BLUE),(519,30,WHITE),
               (600,30,BLUE),(681,30,BLUE),(681,80,BLUE),(762,80,WHITE),(843,80,BLUE),(843,130,BLUE),
               (843,180,BLUE),(762,180,BLUE),(681,180,WHITE),(600,180,BLUE),(519,180,BLUE),
               (438,180,WHITE),(357,180,BLUE),(276,180,BLUE),(195,180,BLUE),(195,230,WHITE),
               (195,280,BLUE),(276,280,BLUE),(357,280,WHITE),(438,280,BLUE),(519,280,BLUE),
               (600,280,BLUE),(681,280,WHITE),(762,280,BLUE),(843,280,BLUE),(843,330,WHITE),
               (843,380,WHITE),(843,430,BLUE),(843,480,WHITE)]
    for item in my_list:
        if(item[2] == BLUE):
            #Draw Track
            pygame.draw.rect(win,item[2],[item[0],item[1],boxWidth,boxHeight])
            #Draw Track Outline
            pygame.draw.line(win,GREEN,(item[0],item[1]+1),(item[0]+boxWidth,item[1]+1))
            pygame.draw.line(win,GREEN,(item[0]+boxWidth,item[1]+1),(item[0]+boxWidth,item[1]+1+boxHeight))
            pygame.draw.line(win,GREEN,(item[0]+boxWidth,item[1]+1+boxHeight),(item[0],item[1]+1+boxHeight))
            pygame.draw.line(win,GREEN,(item[0],item[1]+1+boxHeight),(item[0],item[1]+1))
            
        else:
            #Draw Track
            pygame.draw.rect(win,item[2],[item[0],item[1],boxWidth,boxHeight])
            #Draw Track Outline
            pygame.draw.line(win,GREEN,(item[0],item[1]+1),(item[0]+boxWidth,item[1]+1))
            pygame.draw.line(win,GREEN,(item[0]+boxWidth,item[1]+1),(item[0]+boxWidth,item[1]+1+boxHeight))
            pygame.draw.line(win,GREEN,(item[0]+boxWidth,item[1]+1+boxHeight),(item[0],item[1]+1+boxHeight))
            pygame.draw.line(win,GREEN,(item[0],item[1]+1+boxHeight),(item[0],item[1]+1))
            if(item[0] == 519 and item[1] == 530):
                renderText("Snacks Rs. 20",item[0]+38,item[1]+25,12,BLACK)
            elif(item[0] == 438 and item[1] == 430):
                renderText("Petrol Rs. 50",item[0]+38,item[1]+25,12,BLACK)
            elif(item[0] == 357 and item[1] == 530):
                renderText("Go Home",item[0]+38,item[1]+25,12,BLACK)
            elif(item[0] == 276 and item[1] == 580):
                renderText("6 To Move",item[0]+38,item[1]+25,12,BLACK)
            elif(item[0] == 33 and item[1] == 530):
                renderText("Hotel Rs.100",item[0]+38,item[1]+25,12,BLACK)
            elif(item[0] == 33 and item[1] == 380):
                renderText("Temple",item[0]+38,item[1]+25,12,BLACK)
            elif(item[0] == 33 and item[1] == 180):
                renderText("Ice Cream",item[0]+38,item[1]+25,12,BLACK)
                renderText("Rs.50",item[0]+38,item[1]+38,12,BLACK)
            elif(item[0] == 33 and item[1] == 30):
                renderText("Pool Rs. 50",item[0]+38,item[1]+25,12,BLACK)
            elif(item[0] == 195 and item[1] == 30):
                renderText("Crossed Red Signal",item[0]+38,item[1]+25,8,BLACK)
                renderText("Miss a Turn",item[0]+38,item[1]+34,8,BLACK)
            elif(item[0] == 519 and item[1] == 30):
                renderText("Horse Riding",item[0]+38,item[1]+25,8,BLACK)
                renderText("Rs. 100",item[0]+38,item[1]+34,8,BLACK)
            elif(item[0] == 762 and item[1] == 80):
                renderText("Visited Taj Mahal",item[0]+38,item[1]+25,8,BLACK)
                renderText("Rs. 100",item[0]+38,item[1]+34,8,BLACK)
            elif(item[0] == 681 and item[1] == 180):
                renderText("Boating Rs.60",item[0]+38,item[1]+25,12,BLACK)
            elif(item[0] == 438 and item[1] == 180):
                renderText("Shopping",item[0]+38,item[1]+25,8,BLACK)
                renderText("Rs.200",item[0]+38,item[1]+34,8,BLACK)
            elif(item[0] == 195 and item[1] == 230):
                renderText("Car Battery Is",item[0]+38,item[1]+25,8,BLACK)
                renderText("Low. Miss A Turn",item[0]+38,item[1]+34,8,BLACK)
            elif(item[0] == 357 and item[1] == 280):
                renderText("Petrol Rs. 80",item[0]+38,item[1]+25,12,BLACK)
            elif(item[0] == 681 and item[1] == 280):
                renderText("Helicoptar Ride",item[0]+38,item[1]+25,8,BLACK)
                renderText("Rs. 200",item[0]+38,item[1]+34,8,BLACK)
            elif(item[0] == 843 and item[1] == 330):
                renderText("6 To Move",item[0]+38,item[1]+25,12,BLACK)
            elif(item[0] == 843 and item[1] == 380):
                renderText("6 Steps Back ",item[0]+38,item[1]+25,12,BLACK)
            elif(item[0] == 843 and item[1] == 480):
                renderText("Finish",item[0]+38,item[1]+25,12,BLACK)       
    pygame.display.flip()

#Function for Rolling Dice 
def diceroll(n,c,b,tick,In):
    kkk = 1
    location = (1010, 140)
    while kkk<15:
        if In < 15 and n == 1 and b == 1:
            filename = str(In) + ".gif"  
            img = pygame.image.load(filename)
            win.blit(img, location)
            c.tick(tick)
            In += 1
            if In == 14:
                filename = "img1.gif"  
                img = pygame.image.load(filename)
                win.blit(img, location)
                c.tick(tick)
                b = 0
                In = 1
        if In < 15 and n == 2 and b == 1:
            filename = str(In) + ".gif"  
            img = pygame.image.load(filename)
            win.blit(img, location)
            c.tick(tick)
            In += 1
            if In == 14:
                filename = "img2.gif"  
                img = pygame.image.load(filename)
                win.blit(img, location)
                c.tick(tick)
                b = 0
                In = 1
        if In < 15 and n == 3 and b == 1:
            filename = str(In) + ".gif"  
            img = pygame.image.load(filename)
            win.blit(img, location)
            c.tick(tick)
            In += 1
            if In == 14:
                filename = "img3.gif"  
                img = pygame.image.load(filename)
                win.blit(img, location)
                c.tick(tick)
                b = 0
                In = 1
        if In < 15 and n == 4 and b == 1:
            filename = str(In) + ".gif"  
            img = pygame.image.load(filename)
            win.blit(img, location)
            c.tick(tick)
            In += 1
            if In == 14:
                filename = "img4.gif"  
                img = pygame.image.load(filename)
                win.blit(img, location)
                c.tick(tick)
                b = 0
                In = 1
        if In < 15 and n == 5 and b == 1:
            filename = str(In) + ".gif"  
            img = pygame.image.load(filename)
            win.blit(img, location)
            c.tick(tick)
            In += 1
            if In == 14:
                filename = "img5.gif"  
                img = pygame.image.load(filename)
                win.blit(img, location)
                c.tick(tick)
                b = 0
                In = 1
        if In < 15 and n == 6 and b == 1:
            filename = str(In) + ".gif"  
            img = pygame.image.load(filename)
            win.blit(img, location)
            c.tick(tick)
            In += 1
            if In == 14:
                filename = "img6.gif"  
                img = pygame.image.load(filename)
                win.blit(img, location)
                c.tick(tick)
                b = 0
                In = 1
        pygame.display.flip()
        kkk+=1

#Function for Displaying Output Of Rolling Dice
def dispdiceroll(n):
    location = (1010,140)
    if n == 1:
        filename = "img1.gif"  
        img = pygame.image.load(filename)
        win.blit(img, location)
    elif n == 2:
        filename = "img2.gif"  # ensure filename is correct
        img = pygame.image.load(filename)
        win.blit(img, location)
    elif n == 3:
        filename = "img3.gif"  # ensure filename is correct
        img = pygame.image.load(filename)
        win.blit(img, location)
    elif n == 4:
        filename = "img4.gif"  # ensure filename is correct
        img = pygame.image.load(filename)
        win.blit(img, location)
    elif n == 5:
        filename = "img5.gif"  # ensure filename is correct
        img = pygame.image.load(filename)
        win.blit(img, location)
    elif n == 6:
        filename = "img6.gif"  # ensure filename is correct
        img = pygame.image.load(filename)
        win.blit(img, location)

# Button class

class Button:
    radius = 15
    center_x = 0
    center_y = 0

    def drawButton(self,color,center_x,center_y):
        self.center_x = center_x
        self.center_y = center_y
        pygame.draw.circle(win,color,(self.center_x,self.center_y),self.radius,0)
        
# class player
class Player (Button):
    score = 0                                                      # score of each player
    def __init__(self,color,track):
        self.color = color                                         # color assigned to player
        self.finalstatus = [0]                                     # final status of buttons of a player
        self.initialstatus = [0]                                   # initial status of buttons of a player
        self.track = track                                         # track on which buttons will move
        self.currentposition = [-1]                                # current position of each of the button in  track

    def placeButtons(self,position,initiated):
        '''
        method to place buttons in respective positions
        position is a list having co-ordinates as tuple for each button
        count is an integer variable tells how many ludo buttons are to be initiated
        '''
        for i in range(1):
            if(initiated[i] == position[i]):
                kkk=32
                 #print " This buttons has initiated"
            else:
                pygame.draw.circle(win,BLACK,position[i-1],16,0)
                self.drawButton(self.color,position[i][0],position[i][1])

    def makeAMove(self,current):
        '''
        method to move a button
        current is the current position of the button
        '''
        pygame.draw.circle(win,self.color,self.track[current + n],self.radius)

    def InitiateStart(self,bt_no):
        '''
        method to initiate buttons from the starting positions
        btn_no tells about which button to be initiated
        '''
        pygame.draw.circle(win,self.color,self.track[0],self.radius)


    def isInHome(self):
        '''
        method to check Whether buttons have reached to the home
        '''
        for i in range (1):
            if(self.currentposition[i] == 61 and self.finalstatus[i] != 1):
                self.score +=1
                self.finalstatus[i] = 1
                #print ('final status')
                #print (self.finalstatus)


    def displayTransitButtons(self):
        for i in range(1):
            #print i
            #print self.currentposition[i]
            if(self.currentposition[i] != -1):
                pygame.draw.circle(win,BLACK,self.track[self.currentposition[i]],16,0)
                self.drawButton(self.color,self.track[self.currentposition[i]][0],self.track[self.currentposition[i]][1])

#Instances of class player
Player1 = Player(RED, track)
Player2 = Player(GREEN, track)
Player3 = Player(YELLOW, track)
Player4 = Player(BLACK, track)


#initial positions of buttons for each player
position1 = [(878,560)]
position2 = [(918,560)]
position3 = [(878,600)]
position4 = [(918,600)]

#lists about initiated buttons of a particular player
initiated1 = [(0,0)]
initiated2 = [(0,0)]
initiated3 = [(0,0)]
initiated4 = [(0,0)]

i = 1
" Main Loop"

while True:
    drawBoard()              #Function Called To Draw Game Board
    showButtonRoll()         #Function Called To Display Roll Button
    showButtonMove()         #Function Called To Display Move Button
    dispdiceroll(n)          #Show Image Of Dice
    
    if(mc == 0):             #condition to maintain the display of number that turned up while rolling the dice
        showDiceBox(0)
    else:
        showDiceBox(n)

    showTurnBox(p_id)        #Function Called To Display The of the player
    
    # instances of class player is calling to place buttons on initial positions

    Player1.placeButtons(position1,initiated1)         # Player 1
    Player2.placeButtons(position2,initiated2)         # Player 2
    Player3.placeButtons(position3,initiated3)         # Player 3
    Player4.placeButtons(position4,initiated4)         # Player 4

    # Displaying buttons in transitions

    Player1.displayTransitButtons()                    # Player 1
    Player2.displayTransitButtons()                    # Player 2
    Player3.displayTransitButtons()                    # Player 3
    Player4.displayTransitButtons()                    # Player 4
    
    # List to store scores of each player
    scores = [Player1.score,Player2.score,Player3.score,Player4.score]
    #displayScoreBoard(scores)         # Function call to display score board
    #winingOrder(scores)               # Function call to show winning orders near scoreboard

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:               #Event is quit
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:    #Event is mouse button up is clicked
            (mousex,mousey) = event.pos             #Record x and y co-oridnate of cursor
            mouseclicked = True                     
    
    #If Roll Is Clicked
    if(mouseclicked == True and mousex >= 1050 and mousex <= 1250 and mousey >= 450 and mousey <= 490):
        mc = 1
        n = randint(1,6)                # returns a random number from 1 to 6
        b=1
        showDiceBox(n)                  # Function call to display number that turned up on dice
        mouseclicked = False            # change the status of mouse clicked event
        #dice roll starts
        diceroll(n, c, b, tick, In)
        #dice roll ends
        
    # If Move button is clicked
    elif(mouseclicked == True and mousex >= 1050 and mousex <= 1250 and mousey >= 550 and mousey <= 590):
        if(p_id == 1):
            if(Player1.finalstatus[0] == 1):
                p_id = 2                                    # If all the buttons have reached home, then change player id
            else:
                if(flagIMP == 0):
                    diff = (61 - Player1.currentposition[0])
                    flagIMP = 1
                    
                if(Player1.initialstatus[0] == 0):                   
                    if(n == 6):                         # If 6 turned up on dice
                        Player1.initialstatus[0] = 1    # change the status of button 1 for player 1
                        initiated1[0] = position1[0]    # set the button which has been initiated
                        Player1.InitiateStart(1)        # Function call to initiate the start of button1
                        mouseclicked = False            # Change the status of the event
                        Player1.currentposition[0] = 0  # set the current position of button 1
                    else:
                        p_id = 2                        # change the player-id if number is not 1 or 6
                        mouseclicked =False             # change the status of mouse  clicked event
                else:                   
                    if(i<=n):                        
                        if(i==n):                            
                            flagIMP = 0
                        if(Player1.finalstatus[0] !=1):
                            if(Player1.currentposition[0] >= 61 and n <= diff):
                                Player1.makeAMove(Player1.currentposition[0])
                                Player1.currentposition[0] +=1
                                i+=1
                            elif(Player1.currentposition[0] < 61):
                                Player1.makeAMove(Player1.currentposition[0])
                                Player1.currentposition[0] +=1
                                i+=1
                            else:
                                p_id = 2
                                i=1
                                mouseclicked = False
                        else:
                            Player1.isAtHome()
                            p_id = 2
                            mouseclicked = False
                    elif(i > n):
                        p_id = 2
                        i=1
                        mouseclicked = False
        
        elif(p_id == 2):
            if(Player2.finalstatus[0] == 1):
                p_id = 3                                    # If all the buttons have reached home, then change player id
            else:
                if(flagIMP == 0):
                    diff = (61 - Player2.currentposition[0])
                    flagIMP = 1
                    
                if(Player2.initialstatus[0] == 0):                   
                    if(n == 6):                         # If 1 or 6 turned up on dice
                        Player2.initialstatus[0] = 1    # change the status of button 1 for player 1
                        initiated2[0] = position2[0]    # set the button which has been initiated
                        Player2.InitiateStart(1)        # Function call to initiate the start of button1
                        mouseclicked = False            # Change the status of the event
                        Player2.currentposition[0] = 0  # set the current position of button 1
                    else:
                        p_id = 3                        # change the player-id if number is not 1 or 6
                        mouseclicked =False             # change the status of mouse  clicked event
                else:                   
                    if(i<=n):                        
                        if(i==n):                            
                            flagIMP = 0
                        if(Player2.finalstatus[0] !=1):
                            if(Player2.currentposition[0] >= 61 and n <= diff):
                                Player2.makeAMove(Player2.currentposition[0])
                                Player2.currentposition[0] +=1
                                i+=1
                            elif(Player2.currentposition[0] < 61):
                                Player2.makeAMove(Player2.currentposition[0])
                                Player2.currentposition[0] +=1
                                i+=1
                            else:
                                p_id = 3
                                i=1
                                mouseclicked = False
                        else:
                            Player2.isAtHome()
                            p_id = 3
                            mouseclicked = False
                    elif(i > n):
                        p_id = 3
                        i=1
                        mouseclicked = False 
                        
        elif(p_id == 3):
            if(Player3.finalstatus[0] == 1):
                p_id = 4                                    # If all the buttons have reached home, then change player id
            else:
                if(flagIMP == 0):
                    diff = (61 - Player3.currentposition[0])
                    flagIMP = 4
                    
                if(Player3.initialstatus[0] == 0):                   
                    if(n == 6):                         # If 1 or 6 turned up on dice
                        Player3.initialstatus[0] = 1    # change the status of button 1 for player 1
                        initiated3[0] = position3[0]    # set the button which has been initiated
                        Player3.InitiateStart(1)        # Function call to initiate the start of button1
                        mouseclicked = False            # Change the status of the event
                        Player3.currentposition[0] = 0  # set the current position of button 1
                    else:
                        p_id = 4                        # change the player-id if number is not 1 or 6
                        mouseclicked =False             # change the status of mouse  clicked event
                else:                   
                    if(i<=n):                        
                        if(i==n):                            
                            flagIMP = 0
                        if(Player3.finalstatus[0] !=1):
                            if(Player3.currentposition[0] >= 61 and n <= diff):
                                Player3.makeAMove(Player3.currentposition[0])
                                Player3.currentposition[0] +=1
                                i+=1
                            elif(Player3.currentposition[0] < 61):
                                Player3.makeAMove(Player3.currentposition[0])
                                Player3.currentposition[0] +=1
                                i+=1
                            else:
                                p_id = 4
                                i=1
                                mouseclicked = False
                        else:
                            Player3.isAtHome()
                            p_id = 4
                            mouseclicked = False
                    elif(i > n):
                        p_id = 4
                        i=1
                        mouseclicked = False
        elif(p_id == 4):
            if(Player4.finalstatus[0] == 1):
                p_id = 1                                    # If all the buttons have reached home, then change player id
            else:
                if(flagIMP == 0):
                    diff = (61 - Player4.currentposition[0])
                    flagIMP = 1
                    
                if(Player4.initialstatus[0] == 0):                   
                    if(n == 6):                         # If 1 or 6 turned up on dice
                        Player4.initialstatus[0] = 1    # change the status of button for player 4
                        initiated4[0] = position4[0]    # set the button which has been initiated
                        Player4.InitiateStart(1)        # Function call to initiate the start of button1
                        mouseclicked = False            # Change the status of the event
                        Player4.currentposition[0] = 0  # set the current position of button 1
                    else:
                        p_id = 1                        # change the player-id if number is not 1 or 6
                        mouseclicked =False             # change the status of mouse  clicked event
                else:                   
                    if(i<=n):                        
                        if(i==n):                            
                            flagIMP = 0
                        if(Player4.finalstatus[0] !=1):
                            if(Player4.currentposition[0] >= 61 and n <= diff):
                                Player4.makeAMove(Player4.currentposition[0])
                                Player4.currentposition[0] +=1
                                i+=1
                            elif(Player4.currentposition[0] < 61):
                                Player4.makeAMove(Player4.currentposition[0])
                                Player4.currentposition[0] +=1
                                i+=1
                            else:
                                p_id = 1
                                i=1
                                mouseclicked = False
                        else:
                            Player4.isAtHome()
                            p_id = 1
                            mouseclicked = False
                    elif(i > n):
                        p_id = 1
                        i=1
                        mouseclicked = False
        
    pygame.display.flip()