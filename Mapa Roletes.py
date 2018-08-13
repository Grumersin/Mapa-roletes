import turtle
import math


def llegenda(tortuga,x,y,paraula):
    tortuga.penup()
    tortuga.goto(x,y)
    tortuga.pendown()
    tortuga.begin_fill()
    tortuga.fillcolor("white")
    tortuga.setheading(270)
    tortuga.forward(30)
    tortuga.left(90)
    tortuga.forward(30)
    tortuga.left(90)
    tortuga.forward(30)
    tortuga.left(90)
    tortuga.forward(30)
    tortuga.end_fill()
    tortuga.penup()
    tortuga.setheading(270)
    tortuga.forward(30)
    tortuga.setheading(0)
    tortuga.forward(45)
    tortuga.write(paraula,font=("Arial",20))   



def dibuixar(xr,yr):
    global punter
    global mapa
    global coord_usat
    global moures
    global creu
    global teulada
    global casa
    global campanar
    global castell
    global poble
    global ciutat
    global arbre
    global bosc
    global boscos
    global lbosc
    global muntanya
    global serra
    global lserra
    global compc
    global compp
    global compci
    global compb
    global compm
    global compa
    global compt
    global compll
    global click
    global clicks
       
#INTENT DE UNDO
#    if xr<230 and xr>200 and yr<370 and yr>340:
#        punter.color("darkkhaki")
#        punter.fillcolor("darkkhaki")
#        punter.begin_fill()
#        if compp==True:
#            punter.goto(coord_usat[0][0],coord_usat[0][1])
#            poble(casa,campanar,punter,10,teulada)
#            
#        if compci==True:
#            punter.goto(coord_usat[0][0],coord_usat[0][1])
#            ciutat(casa,campanar,punter,10,teulada,castell)
#            
#        if compb==True:
#            punter.goto(coord_usat[0][0],coord_usat[0][1])
#            bosc(arbre,punter,10)            
#            
#        if compa==True:
#            punter.goto(coord_usat[0][0],coord_usat[0][1])
#            port(punter,10)
#            
#        if compm==True:
#            punter.goto(coord_usat[0][0],coord_usat[0][1])
#            muntanya(punter,10)
#        punter.end_fill()
#        punter.color("black")
#        coord_usat=[]
        
    if (xr<-690 and xr>-720 and yr<370 and yr>340) or (xr<-520 and xr>-550 and yr<370 and yr>340) or (xr<-370 and xr>-400 and yr<370 and yr>340) or (xr<-220 and xr>-250 and yr<370 and yr>340) or (xr<80 and xr>50 and yr<370 and yr>340) or (xr<-70 and xr>-100 and yr<370 and yr>340) or (xr<230 and xr>200 and yr<370 and yr>340) or (xr<280 and xr>250 and yr<370 and yr>340) or (xr<380 and xr>350 and yr<370 and yr>340):
        compc=False
        compp=False
        compci=False
        compb=False
        compm=False
        compa=False
        compt=False
        if click==True:
            punter.color("white")
            creu(punter,clicks[0][0],clicks[0][1])
            punter.color("black")
        click=True
        
    if compc==True:
        if len(coord_usat)==0:
            punter.penup()
            punter.goto(xr,yr)
            punter.pendown()
            coord_usat.append([xr,yr])
            punter.begin_fill()
            punter.fillcolor("darkkhaki")
        else:
            if abs(abs(xr)-abs(coord_usat[0][0]))<7 and abs(abs(yr)-abs(coord_usat[0][1]))<7:
                punter.goto(coord_usat[0][0],coord_usat[0][1])
                punter.end_fill()
                punter.penup()
                coord_usat=[]
                compc=False
                punter.color("white")
                creu(punter,-720,370)
                punter.color("black")
                click=False
            else:
                punter.goto(xr,yr)
                
    if compll==True:
        if len(coord_usat)==0:
            punter.penup()
            punter.goto(xr,yr)
            punter.pendown()
            coord_usat.append([xr,yr])
            punter.begin_fill()
            punter.fillcolor("deepskyblue")
        else:
            if abs(abs(xr)-abs(coord_usat[0][0]))<7 and abs(abs(yr)-abs(coord_usat[0][1]))<7:
                punter.goto(coord_usat[0][0],coord_usat[0][1])
                punter.end_fill()
                punter.penup()
                coord_usat=[]
                compll=False
                punter.color("white")
                creu(punter,250,370)
                punter.color("black")
                click=False
            else:
                punter.goto(xr,yr)
    
    if compp==True:
        punter.penup()
        punter.goto(xr-10,yr+30)
        punter.pendown()
        poble(casa,campanar,punter,10,teulada)
        compp=False
#        coord_usat.append([xr,yr]) #Això és per l'undo
        punter.color("white")
        creu(punter,-550,370)
        punter.color("black")
        click=False
    
    if compci==True:
        punter.penup()
        punter.goto(xr-10,yr)
        punter.pendown()
        ciutat(casa,campanar,punter,10,teulada,castell)
        compci=False
#        coord_usat.append([xr,yr])#Això és per l'undo
        punter.color("white")
        creu(punter,-400,370)
        punter.color("black")
        click=False
            
    if compb==True:        
        if len(lbosc)!=0:
            if lbosc[0][0]==xr and lbosc[0][1]==yr:
                punter.penup()
                punter.goto(lbosc[0][0],lbosc[0][1])
                punter.pendown()
                bosc(arbre,punter,10)
                compb=False
#                coord_usat.append([xr,yr])#Això és per l'undo
                punter.color("white")
                creu(punter,-250,370)
                punter.color("black")
                click=False
                lbosc=[]
            else:
                punter.penup()
                punter.goto(lbosc[0][0],lbosc[0][1])
                punter.pendown()
                boscos(bosc,arbre,punter,10,lbosc[0][0],lbosc[0][1],xr,yr)
                compb=False
#                coord_usat.append([xr,yr])#Això és per l'undo
                punter.color("white")
                creu(punter,-250,370)
                punter.color("black")
                click=False
                lbosc=[]
        else:
            lbosc.append([xr,yr])
        
    if compm==True:
        if len(lserra)!=0:
            if lserra[0][0]==xr and lserra[0][1]==yr:
                punter.penup()
                punter.goto(lserra[0][0],lserra[0][1])
                muntanya(punter,10)
                compm=False
#                coord_usat.append([xr,yr])#Això és per l'undo
                punter.color("white")
                creu(punter,50,370)
                punter.color("black")
                click=False
                lserra=[]
            else:
                punter.penup()
                punter.goto(lserra[0][0],lserra[0][1])
                serra(muntanya,punter,10,lserra[0][0],lserra[0][1],xr,yr)
                compm=False
#                coord_usat.append([xr,yr])#Això és per l'undo
                punter.color("white")
                creu(punter,50,370)
                punter.color("black")
                click=False
                lserra=[]
        else:
            lserra.append([xr,yr])
        
    if compa==True:
        punter.penup()
        punter.goto(xr,yr)
        punter.pendown()
        port(punter,10)
        compa=False
#        coord_usat.append([xr,yr])#Això és per l'undo
        punter.color("white")
        creu(punter,-100,370)
        punter.color("black")
        click=False
        

    if compt==True:
        punter.penup()
        punter.goto(xr,yr)
        punter.pendown()
        text=turtle.textinput("Nom","Quin nom li vols posar?")
        punter.write(text,False,"center",("Arial",20,"bold italic")) 
        punter.penup()
        compt=False
        punter.color("white")
        creu(punter,350,370)
        punter.color("black")
        click=False
        
#--------------------------------------------------------------            
    if xr<-690 and xr>-720 and yr<370 and yr>340: #Continent
        clicks=[]
        compc=True
        compp=False
        compci=False
        compb=False
        compm=False
        compa=False
        compt=False
        compll=False
        creu(punter,-720,370)
        coord_usat=[]
        clicks.append([-720,370])
        
    if xr<-520 and xr>-550 and yr<370 and yr>340: #Poble
        clicks=[]
        compc=False
        compp=True
        compci=False
        compb=False
        compm=False
        compa=False
        compt=False
        compll=False
        creu(punter,-550,370)
        clicks.append([-550,370])
        
    if xr<-370 and xr>-400 and yr<370 and yr>340: #Ciutat
        clicks=[]
        compc=False
        compp=False
        compci=True
        compb=False
        compm=False
        compa=False
        compt=False
        compll=False
        creu(punter,-400,370)
        clicks.append([-400,370])
        
    if xr<-220 and xr>-250 and yr<370 and yr>340: #Bosc
        clicks=[]
        compc=False
        compp=False
        compci=False
        compb=True
        compm=False
        compa=False
        compt=False
        compll=False
        creu(punter,-250,370)
        clicks.append([-250,370])
        
    if xr<80 and xr>50 and yr<370 and yr>340: #Muntanyes
        clicks=[]
        compc=False
        compp=False
        compci=False
        compb=False
        compm=True
        compa=False
        compt=False
        compll=False
        creu(punter,50,370)
        clicks.append([50,370])
        
    if xr<-70 and xr>-100 and yr<370 and yr>340: #Port
        clicks=[]
        compc=False
        compp=False
        compci=False
        compb=False
        compm=False
        compa=True
        compt=False
        compll=False
        creu(punter,-100,370)
        clicks.append([-100,370])
        
    if xr<380 and xr>350 and yr<370 and yr>340: #Text
        compc=False
        compp=False
        compci=False
        compb=False
        compm=False
        compa=False
        compt=True
        compll=False
        creu(punter,350,370)
        clicks.append([350,370])
        
    if xr<280 and xr>250 and yr<370 and yr>340: #Llac
        clicks=[]
        compc=False
        compp=False
        compci=False
        compb=False
        compm=False
        compa=False
        compt=False
        compll=True
        creu(punter,250,370)
        coord_usat=[]
        clicks.append([250,370])
        


def creu(tortuga,x,y):
    tortuga.penup()
    tortuga.goto(x,y)
    tortuga.setheading(360-45)
    tortuga.pendown()
    tortuga.forward(30*math.sqrt(2))
    tortuga.penup()
    tortuga.setheading(90)
    tortuga.forward(30)
    tortuga.setheading(180+45)
    tortuga.pendown()
    tortuga.forward(30*math.sqrt(2))
    tortuga.penup()
    

def teulada(tortuga,mida):
    tortuga.setheading(45)
    tortuga.begin_fill()
    tortuga.forward(mida/2*math.sqrt(2))
    tortuga.right(90)
    tortuga.forward(mida/2*math.sqrt(2))
    tortuga.fillcolor("red")
    tortuga.end_fill()

def casa(tortuga,mida,teulada):
    tortuga.pendown()
    tortuga.begin_fill()
    tortuga.setheading(270)
    tortuga.forward(mida)
    tortuga.left(90)
    tortuga.forward(mida)
    tortuga.left(90)
    tortuga.forward(mida)
    tortuga.left(90)
    tortuga.forward(mida)
    tortuga.fillcolor("brown")
    tortuga.end_fill()
    teulada(tortuga,mida)
    tortuga.penup()
    tortuga.setheading(360/5*2)
    
def campanar(tortuga,mida,teulada):
    tortuga.pendown()
    tortuga.begin_fill()
    tortuga.setheading(270)
    tortuga.forward(mida*4)
    tortuga.left(90)
    tortuga.forward(mida)
    tortuga.left(90)
    tortuga.forward(mida*4)
    tortuga.left(90)
    tortuga.forward(mida)
    tortuga.fillcolor("brown")
    tortuga.end_fill()
    teulada(tortuga,mida)
    tortuga.penup()
    tortuga.setheading(270)
    tortuga.forward(mida/2)
    tortuga.right(90)
    tortuga.forward(mida/2)
    tortuga.pendown()
    tortuga.begin_fill()
    tortuga.circle(mida/3)
    tortuga.fillcolor("moccasin")
    tortuga.end_fill()
    tortuga.penup()
    
def poble(casa,campanar,tortuga,mida,teulada):
    tortuga.pendown()
    campanar(tortuga,mida,teulada)
    tortuga.setheading(270)
    tortuga.forward(mida*2)
    tortuga.setheading(0)
    tortuga.forward(mida*1.5)
    for i in range(5):
        tortuga.setheading(180)
        tortuga.forward(mida)
        casa(tortuga,mida,teulada)
        tortuga.left(i*360/5)
        tortuga.forward(mida)  
    tortuga.penup()
    
    
def castell(tortuga,mida,teulada):
    tortuga.setheading(0)
    tortuga.pendown()
    tortuga.begin_fill()
    tortuga.forward(3*mida)
    tortuga.left(90)
    tortuga.forward(mida*3)
    tortuga.left(90)
    tortuga.forward(mida)
    tortuga.left(90)
    tortuga.forward(mida)
    tortuga.right(90)
    tortuga.forward(mida)
    tortuga.right(90)
    tortuga.forward(mida)
    tortuga.left(90)
    tortuga.forward(mida)
    tortuga.left(90)
    tortuga.forward(3*mida)
    tortuga.fillcolor("grey")
    tortuga.end_fill()
    tortuga.penup()
    tortuga.setheading(0)
    tortuga.forward(2*mida)
    tortuga.left(90)
    tortuga.forward(mida*3)
    tortuga.pendown()
    teulada(tortuga,mida)
    tortuga.penup()
    tortuga.setheading(180)
    tortuga.forward(3*mida)
    tortuga.pendown()
    teulada(tortuga,mida)
    tortuga.setheading(180)
    tortuga.penup()
    
def ciutat(casa,campanar,tortuga,mida,teulada,castell):
    castell(tortuga,mida,teulada)
    tortuga.forward(mida*2)
    tortuga.left(90)
    tortuga.forward(mida)
    poble(casa,campanar,tortuga,mida,teulada)
    tortuga.setheading(0)
    tortuga.forward(mida*3)
    tortuga.left(90)
    tortuga.forward(3*mida)
    poble(casa,campanar,tortuga,mida,teulada)
    tortuga.setheading(180)
    tortuga.forward(4*mida)
    tortuga.right(90)
    tortuga.forward(mida)
    poble(casa,campanar,tortuga,mida,teulada)
    
def arbre(tortuga,mida):
    tortuga.setheading(270)
    tortuga.pendown()
    tortuga.begin_fill()
    tortuga.fillcolor("brown")
    tortuga.forward(mida/2)
    tortuga.left(90)
    tortuga.forward(mida/2)
    tortuga.left(90)
    tortuga.forward(mida/2)
    tortuga.left(90)
    tortuga.forward(mida/2)
    tortuga.end_fill()
    tortuga.begin_fill()
    tortuga.fillcolor("darkgreen")
    tortuga.forward(mida)
    tortuga.setheading(45)
    tortuga.forward(mida*1.5)
    tortuga.setheading(180)
    tortuga.forward(mida/2)
    tortuga.setheading(45)
    tortuga.forward(mida)
    tortuga.setheading(180)
    tortuga.forward(mida/3)
    tortuga.setheading(45)
    tortuga.forward(mida/2)
    tortuga.setheading(315)
    tortuga.forward(mida/2)
    tortuga.setheading(180)
    tortuga.forward(mida/3)
    tortuga.setheading(315)
    tortuga.forward(mida)
    tortuga.setheading(180)
    tortuga.forward(mida/2)
    tortuga.setheading(315)
    tortuga.forward(mida*1.5)
    tortuga.setheading(180)
    tortuga.forward(mida*1.5)
    tortuga.end_fill()
    tortuga.penup()
    
def bosc(arbre,tortuga,mida):
    tortuga.pendown()
    for i in range(5):
        arbre(tortuga,mida)
        tortuga.left(i*360/5)
        tortuga.forward(mida*1.5)  
    tortuga.penup()
    
def boscos(bosc,arbre,tortuga,mida,x1,y1,x2,y2):
    tortuga.penup()
    nmun=math.ceil((math.sqrt((x2-x1)**2+(y2-y1)**2))/(mida*4))
    tortuga.goto(x1,y1)
    cont=0
    while cont<nmun:
        cont+=1
        bosc(arbre,tortuga,mida)
        if y2>y1:
            tortuga.setheading(360/(2*math.pi)*math.acos((x2-x1)/math.sqrt((x2-x1)**2+(y2-y1)**2)))
        else:
            tortuga.setheading(-360/(2*math.pi)*math.acos((x2-x1)/math.sqrt((x2-x1)**2+(y2-y1)**2)))
        tortuga.forward(mida*4)
    
def muntanya(tortuga,mida):
    tortuga.penup()
#    tortuga.setheading(180)
#    tortuga.forward(mida*1.8)
    tortuga.setheading(60)
    tortuga.pendown()
    tortuga.begin_fill()
    tortuga.fillcolor("silver")
    tortuga.forward(mida*4)
    tortuga.setheading(300)
    tortuga.forward(mida*4)
    tortuga.end_fill()
    tortuga.penup()
    tortuga.left(180)
    tortuga.forward(mida*8/3)
    tortuga.begin_fill()
    tortuga.fillcolor("snow")
    tortuga.color("snow")
    tortuga.pendown()
    tortuga.forward(mida*4/3)
    tortuga.setheading(240)
    tortuga.forward(mida*4/3)
    tortuga.setheading(0)
    tortuga.forward(math.cos(math.pi/3)*mida*8/3)
    tortuga.end_fill()
    tortuga.penup()
    tortuga.color("black")
    
def serra(muntanya, tortuga,mida,x1,y1,x2,y2):
    tortuga.penup()
    nmun=math.ceil((math.sqrt((x2-x1)**2+(y2-y1)**2))/(mida*2*math.sqrt(2)))
    tortuga.goto(x1,y1)
    cont=0
    while cont<nmun:
        cont+=1
        muntanya(tortuga,mida)
        tortuga.setheading(180)
        tortuga.forward(math.cos(math.pi/3)*mida*4/3)
        tortuga.setheading(270)
        tortuga.forward(4*math.sqrt(3)/3*mida)
        if y2>y1:
            tortuga.setheading(360/(2*math.pi)*math.acos((x2-x1)/math.sqrt((x2-x1)**2+(y2-y1)**2)))
        else:
            tortuga.setheading(-360/(2*math.pi)*math.acos((x2-x1)/math.sqrt((x2-x1)**2+(y2-y1)**2)))
        tortuga.forward(mida*2*math.sqrt(2))
        tortuga.setheading(180)
        tortuga.forward(mida*2)
    
def port(tortuga,mida):
    tortuga.setheading(170)
    tortuga.pendown()
    tortuga.begin_fill()
    tortuga.fillcolor("chocolate")
    tortuga.forward(mida*2)
    tortuga.setheading(50)
    tortuga.forward(mida)
    tortuga.setheading(350)
    tortuga.forward(mida*3)
    tortuga.setheading(230)
    tortuga.forward(mida*3)
    tortuga.setheading(170)
    tortuga.forward(mida)
    tortuga.setheading(50)
    tortuga.forward(mida*3)    
    tortuga.end_fill()
    tortuga.setheading(170)
    tortuga.forward(mida*0.5)
    tortuga.setheading(230)
    tortuga.forward(mida)
    tortuga.setheading(170)
    tortuga.forward(mida*0.5)
    tortuga.setheading(50)
    tortuga.forward(mida)
    tortuga.setheading(170)
    tortuga.forward(mida*0.5)
    tortuga.setheading(230)
    tortuga.forward(mida)
    tortuga.setheading(350)
    tortuga.forward(mida*2.5)
    tortuga.setheading(230)
    tortuga.forward(mida*0.5)
    tortuga.setheading(170)
    tortuga.forward(mida)
    tortuga.setheading(230)
    tortuga.forward(mida*0.5)
    tortuga.setheading(350)
    tortuga.forward(mida)
    tortuga.setheading(230)
    tortuga.forward(mida*0.5)
    tortuga.setheading(170)
    tortuga.forward(mida)
    tortuga.penup()
    
    


mapa=turtle.Screen()
mapa.setup(1400,600)
mapa.bgcolor("deepskyblue")
mapa.title("Mapa")

punter=turtle.Turtle()
punter.speed(0)
punter.penup()
punter.hideturtle()

    
llegenda(punter,-720,370,"continent")
llegenda(punter,-550,370,"poble")
llegenda(punter,-400,370,"ciutat")
llegenda(punter,-250,370,"bosc")
llegenda(punter,-100,370,"port")
llegenda(punter,50,370,"muntanyes")
llegenda(punter,250,370,"llac")
llegenda(punter,350,370,"text")




coord_usat=[]
compc=False
compp=False
compci=False
compb=False
compm=False
compa=False
compt=False
compll=False
click=False
clicks=[]
lserra=[]
lbosc=[]
mapa.onscreenclick(dibuixar)


turtle.done()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    