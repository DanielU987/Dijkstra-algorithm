from cmath import sqrt
from dis import dis
from operator import le
from tkinter import *
import math
import time
import datetime
file = open("MapXml.xml")
root = Tk()
canvas = Canvas(root, width=1000, height=1000)
canvas.pack()
masX = []
masY = []
idl = []
kuda1 = []
to1 = []
lanes = []
speed= []
mass = []
speed1= []
mass1 = []
neighborPoints = []
sosFrom = []
sosTo = []
VisitedPoints = []
ReturnPoints = []
sosFrom2 = []
sosTo2 = []
distanceAr= []
Allvisisted=[]
i = -1
est=0
nextP = 0
posRoutes = 0

state = 0
u = 0
prov=0
prov2=0
abv=0
delet=0
tupik=0
distance= 0

time1=0
time1Ar=[]

#perehod = 0
BgColors = {'start': '#3333ff',
            'finish': '#99ff66',
            'maybe': '#cc3399',
            'error': '#99ff66',
            'visited': '#b3b3ff',
            'Next': '#00ffff',
            'Point': '#c0c0c0',
            'Current': '#ffff00'}
StatusNames = {'alpha': 'Начало пути',
               'omega': 'Конец пути',
               'beta': 'Обычный узел',
               'gamma': 'Узел, возможный для перехода',
               'charlie': 'Исключенный',
               'delta': 'Избранный для перехода',
               'foxtrot': 'Посещенный узел',
               'cupcake': 'Текущий'}
mapWidth = 1000
mapHeight = 1000
fonsize = 14
borderWidth = 2
wayWidth = 4


class Example:
    def __init__(self, Width, Height, Size, Name, From, To):
        self.X = Width
        self.Y = Height
        self.Razmer = Size
        self.tid = Name
        self.Ot = From
        self.Kuda = To

        otk = self.Ot - 1
        kuda = self.Kuda - 1
        tid = self.tid
        x = self.X
        y = self.Y
        height = self.Razmer
        k = 0
        defolt = 200
        r = height*4
        for k in range(len(lanes)):
            canvas.create_line(masX[idl.index(kuda1[k])]+r+10, masY[idl.index(kuda1[k])]+r+10, masX[idl.index(to1[k])]+r+10,masY[idl.index(to1[k])]+r+10, width=2, arrow=LAST, activefill='lightgreen', arrowshape="10 20 10")
            #canvas.pack()
            #canvas.update()
            #print(masX[kuda1[k-1]],masY[kuda1[k]-1], masX[to1[k]-1],masY[to1[k]-1])
            #print("A",kuda1[k-1],to1[k-1],k)
            #print("B",idl.index(k+1),k)
            #print(idl.index(kuda1[k]))
            #time.sleep(1)
            
        for i in range(len(masX)):
            canvas.create_oval(masX[i]+r, masY[i]+r,
                               masX[i]+20+r, masY[i]+20+r, fill="orange")
            canvas.create_text(masX[i]+r+10, masY[i]+r+10,
                               text=idl[i], justify=CENTER, font="Verdana 14")


for line in file:
    if line.find('<point ') > -1:
        # print(line)
        x = int(line[line.find('x="')+3:line.find('"', line.find('x="')+4)])
        y = int(line[line.find('y="')+3:line.find('"', line.find('y="')+4)])
        m = int(line[line.find('m="')+3:line.find('"', line.find('m="')+4)])
        tid = int(line[line.find('id="') +4:line.find('"', line.find('id="')+4)])
        mass.append(m)
        masX.append(x)
        masY.append(y)
        idl.append(tid)
    if line.find('<route ') > -1:
        lin = int(line[line.find('from="') +6:line.find('"', line.find('from="')+7)])
        to = int(line[line.find('to="')+4:line.find('"', line.find('to="')+5)])
        lid = int(line[line.find('id="') +4:line.find('"', line.find('id="')+4)])
        v = int(line[line.find('v="')+3:line.find('"', line.find('v="')+4)])
        kuda1.append(lin)
        to1.append(to)
        lanes.append(lid)
        speed.append(v)
        Parametri = Example(x, y, m, tid, lin, to)
#print(lanes)
#print(len(masX),len(masY),len(kuda1),len(to1))
r = m*4
#print(idl)
#print(mass)
#print(speed)
#print(lanes)
# kuda1.sort()
#print(idl)
#print(idl.index(17))
#print(masX,len(masX))
#print(masY)
#print(idl,len(idl))
#print("")
#print(kuda1)
#print(to1)

r2 = max(to1)
t = int(input("Начальная точка"))-1
l = int(input("Конечная точка"))

do = l
#print(do)
canvas.create_oval(masX[idl.index(t+1)]+r, masY[idl.index(t+1)]+r, masX[idl.index(t+1)]+20+r,
                   masY[idl.index(t+1)]+20+r, fill=BgColors['start'])
canvas.create_text(masX[idl.index(t+1)]+r+10, masY[idl.index(t+1)]+r+10,
                   text=idl[idl.index(t+1)], justify=CENTER, font="Verdana 14")

if l > r2:
    l = r2
canvas.create_oval(masX[idl.index(l)]+r, masY[idl.index(l)]+r, masX[idl.index(l)] +
                   20+r, masY[idl.index(l)]+20+r, fill=BgColors['finish'])
canvas.create_text(masX[idl.index(l)]+r+10, masY[idl.index(l)]+r+10,
                   text=idl[idl.index(l)], justify=CENTER, font="Verdana 14")

#print(masX)
#print(masY)
print(kuda1)
print(to1)
ub=0
if idl.index(t+1)==idl.index(l):
    u+=1
    print("Точка назначения равна точке назначения")
    ub+=1
while ub <1:
    for i in range(len(kuda1)):  # Откуда можно перейти куда
        if to1[i] == kuda1[kuda1.index(do)]:
            sosFrom.append(to1[to1.index(do)])
            sosTo.append(kuda1[i])
            # print("AA",do)
    #print("sosFrom",sosFrom,"sosTo",sosTo)
    for i in range(len(to1)):  # Соседи у точек в которые можно перейти
        for j in range(len(sosTo)):
            if to1[i] == sosTo[j]:
                sosFrom2.append(sosTo[j])
                sosTo2.append(kuda1[i])
    for ib in range(len(sosTo)):
        if sosTo[ib] == t+1:
            print("1Переход из ", sosFrom[0], "в ", sosTo[ib])
            if sosFrom[0] not in VisitedPoints:
                    VisitedPoints.append(nextP)
                    prov=0
            VisitedPoints.append(sosTo[ib])
            print("Мы пришли в точку ", t+1)
            ub += 1
            #print(ub,u)
    #print("sosFrom2",sosFrom2,"sosTo2",sosTo2) 
    for i in sosTo: #Удаление тупиков
        if i not in sosFrom2:
            if i == t:
                continue
            #canvas.create_oval(masX[idl.index(sosTo[i])]+r, masY[idl.index(sosTo[i])]+r, masX[idl.index(sosTo[i])]+20+r, masY[idl.index(sosTo[i])]+20+r, fill=BgColors['error'])
            #canvas.create_text(masX[idl.index(sosTo[i])]+r+10, masY[idl.index(sosTo[i])]+r+10,text=idl[idl.index(sosTo[i])], justify=CENTER, font="Verdana 14")
            else:
                sosTo.pop(sosTo.index(i))
    for i in sosTo2: #Удаление возвратов
        if i in sosFrom:
            #canvas.create_oval(masX[idl.index(sosTo2[i])]+r, masY[idl.index(sosTo2[i])]+r, masX[idl.index(sosTo2[i])]+20+r, masY[idl.index(sosTo2[i])]+20+r, fill=BgColors['error'])
            #canvas.create_text(masX[idl.index(sosTo2[i])]+r+10, masY[idl.index(sosTo2[i])]+r+10,text=idl[idl.index(sosTo2[i])], justify=CENTER, font="Verdana 14")

            sosTo.pop(sosTo2.index(i))
    #print(sosFrom2)
    if sosFrom2==[]:
        ub+=1
        print("У пункта назначения нету входящих путей")
        u+=1       


    if ub < 1:
        
        if len(sosTo)>1:
            for i in range(len(sosTo)):
                if sosTo[i] not in VisitedPoints:
                    est+=1
                    nextP=sosTo[i]
                    if sosFrom[0] not in VisitedPoints:
                        VisitedPoints.append(sosFrom[0])
                        prov=0
                    print("2Переход из ", sosFrom[0], "в ", nextP)
                    
                    break
                elif sosTo[i] in VisitedPoints:
                    est-=1
            if est<0:
                if sosFrom[0] not in VisitedPoints:
                    VisitedPoints.append(sosFrom[0])
                    prov=0
                if sosTo[0] not in VisitedPoints:
                    VisitedPoints.append(sosTo[0])
                    prov=0
                nextP=sosTo[0]
                print("3Переход из ", sosFrom[0], "в ", nextP)
                
        else:
            if sosTo!=[]:
                if sosFrom[0] not in VisitedPoints:
                        VisitedPoints.append(sosFrom[0])
                        prov=0
                        
                nextP=sosTo[0]
                
                print("4Переход из ", sosFrom[0], "в ", nextP)

                    
            else:
                if do+1 not in VisitedPoints:
                        VisitedPoints.append(do+1)
                        prov=0
                do = l
                print("reset4")
                abv=1
        if abv!=1:
            if idl.index(sosTo[0]) == idl.index(l+1):
                do = l         
                print("reset3")
            elif sosFrom2 == []:            
                do = l
                print("reset2")
                #VisitedPoints.append(sosTo[0])
            else:
                do = nextP
                print("reset1")
            ReturnPoints=[]
            for i in range(len(VisitedPoints)):
                ReturnPoints.append(VisitedPoints[i])
        #print(VisitedPoints)          
        # print(sosTo)
        # print(nextP)
        # print(posRoutes,VisitedRoutes)
        sosTo2.clear()
        sosFrom2.clear()
        sosTo.clear()
        sosFrom.clear()
        est=0
        abv=0
        #time.sleep(1)
sosTo2.clear()
sosFrom2.clear()
sosTo.clear()
sosFrom.clear()
est=0
abv=0
VisitedPoints.clear()
do = t 

while u < 1:  # sosTo[0] != l

    for i in range(len(to1)):  # Откуда можно перейти куда
        if kuda1[i] == to1[to1.index(do+1)]:
            sosFrom.append(kuda1[kuda1.index(do+1)])
            sosTo.append(to1[i])
            # print("AA",do)
    for i in range(len(kuda1)):  # Соседи у точек в которые можно перейти
        for j in range(len(sosTo)):
            if kuda1[i] == sosTo[j]:
                sosFrom2.append(sosTo[j])
                sosTo2.append(to1[i])
                # print(i)
    for i3 in range(len(sosTo)):
        if sosTo[i3] == l:
            if sosFrom[0] not in VisitedPoints:
                    VisitedPoints.append(nextP)
            VisitedPoints.append(sosTo[i3])
            
            Allvisisted.append(nextP)
            Allvisisted.append(sosTo[i3])
            for i in range(len(VisitedPoints)):
                canvas.create_oval(masX[idl.index(VisitedPoints[i])] +r, masY[idl.index(VisitedPoints[i])]+r, masX[idl.index(VisitedPoints[i])]+20+r, masY[idl.index(VisitedPoints[i])]+20+r, fill=BgColors['visited'])
                canvas.create_text(masX[idl.index(VisitedPoints[i])]+r+10, masY[idl.index(VisitedPoints[i])]+r+10,text=idl[idl.index(VisitedPoints[i])], justify=CENTER, font="Verdana 14")
            canvas.create_oval(masX[idl.index(VisitedPoints[-1])] +r, masY[idl.index(VisitedPoints[-1])]+r, masX[idl.index(VisitedPoints[-1])]+20+r, masY[idl.index(VisitedPoints[-1])]+20+r, fill=BgColors['Current'])
            canvas.create_text(masX[idl.index(VisitedPoints[-1])]+r+10, masY[idl.index(VisitedPoints[-1])]+r+10,text=idl[idl.index(VisitedPoints[-1])], justify=CENTER, font="Verdana 14")
            
            canvas.create_oval(masX[idl.index(sosFrom[0])]+r, masY[idl.index(sosFrom[0])]+r, masX[idl.index(sosFrom[0])]+20+r, masY[idl.index(sosFrom[0])]+20+r, fill=BgColors['visited'])
            canvas.create_text(masX[idl.index(sosFrom[0])]+r+10, masY[idl.index(sosFrom[0])]+r+10,text=idl[idl.index(sosFrom[0])], justify=CENTER, font="Verdana 14")

            canvas.create_line(masX[idl.index(sosFrom[0])]+r+10, masY[idl.index(sosFrom[0])]+r+10, masX[idl.index(sosTo[i3])] +r+10, masY[idl.index(sosTo[i3])]+r+10, width=2, fill="green", arrow=LAST, arrowshape="10 20 10")
            #canvas.create_oval(masX[idl.index(sosTo[0])] +r, masY[idl.index(sosTo[0])]+r, masX[idl.index(sosTo[0])]+20+r, masY[idl.index(sosTo[0])]+20+r, fill=BgColors['Current'],outline='green')
            #canvas.create_text(masX[idl.index(sosTo[0])]+r+10, masY[idl.index(sosTo[0])]+r+10,text=idl[idl.index(sosTo[0])], justify=CENTER, font="Verdana 14")   

            print("1Переход из ", sosFrom[0], "в ", sosTo[i3])
            
            print("Мы пришли в точку ", l)
            #canvas.pack()
            #canvas.update()
            u+=1
            #break
            
    # print("sosFrom2",sosFrom2,"sosTo2",sosTo2)
    # print("sosFrom",sosFrom,"sosTo",sosTo)


    if u < 1:
        def ochistka():
            print("o4istka")
            for k in range(len(lanes)):
                canvas.create_line(masX[idl.index(kuda1[k])]+r+10, masY[idl.index(kuda1[k])]+r+10, masX[idl.index(to1[k])]+r+10,masY[idl.index(to1[k])]+r+10, width=2, arrow=LAST, activefill='lightgreen', arrowshape="10 20 10")

            for i in range(len(masX)):
                canvas.create_oval(masX[i]+r, masY[i]+r,
                                masX[i]+20+r, masY[i]+20+r, fill="orange")
                canvas.create_text(masX[i]+r+10, masY[i]+r+10,
                                text=idl[i], justify=CENTER, font="Verdana 14")
                                
            canvas.create_oval(masX[idl.index(t+1)]+r, masY[idl.index(t+1)]+r, masX[idl.index(t+1)]+20+r,
                            masY[idl.index(t+1)]+20+r, fill=BgColors['start'])
            canvas.create_text(masX[idl.index(t+1)]+r+10, masY[idl.index(t+1)]+r+10,
                            text=idl[idl.index(t+1)], justify=CENTER, font="Verdana 14")
            canvas.create_oval(masX[idl.index(l)]+r, masY[idl.index(l)]+r, masX[idl.index(l)] +
                20+r, masY[idl.index(l)]+20+r, fill=BgColors['finish'])
            canvas.create_text(masX[idl.index(l)]+r+10, masY[idl.index(l)]+r+10,
                            text=idl[idl.index(l)], justify=CENTER, font="Verdana 14")
        def paint():
            #for i in range(len(sosFrom)):
            #    canvas.create_oval(masX[idl.index(sosFrom[i])] +r, masY[idl.index(sosFrom[i])]+r, masX[idl.index(sosFrom[i])]+20+r, masY[idl.index(sosTo[i])]+20+r, fill=BgColors['maybe'])
            #    canvas.create_text(masX[idl.index(sosFrom[i])]+r+10, masY[idl.index(sosFrom[i])]+r+10,text=idl[idl.index(sosFrom[i])], justify=CENTER, font="Verdana 14")
            #    print(sosTo[i])
            #for i in range(len(sosTo)):
            #    canvas.create_oval(masX[idl.index(sosTo[i])] +r, masY[idl.index(sosTo[i])]+r, masX[idl.index(sosTo[i])]+20+r, masY[idl.index(sosTo[i])]+20+r, fill=BgColors['maybe'])
            #    canvas.create_text(masX[idl.index(sosTo[i])]+r+10, masY[idl.index(sosTo[i])]+r+10,text=idl[idl.index(sosTo[i])], justify=CENTER, font="Verdana 14")
            #    print(sosTo[i])
            canvas.create_line(masX[idl.index(sosFrom[0])]+r+10, masY[idl.index(sosFrom[0])]+r+10, masX[idl.index(sosTo[0])] +r+10, masY[idl.index(sosTo[0])]+r+10, width=2, fill="green", arrow=LAST, arrowshape="10 20 10")
            canvas.create_oval(masX[idl.index(sosFrom[0])] +r, masY[idl.index(sosFrom[0])]+r, masX[idl.index(sosFrom[0])]+20+r, masY[idl.index(sosFrom[0])]+20+r, fill=BgColors['Current'])
            canvas.create_text(masX[idl.index(sosFrom[0])]+r+10, masY[idl.index(sosFrom[0])]+r+10,text=idl[idl.index(sosFrom[0])], justify=CENTER, font="Verdana 14")

            canvas.create_oval(masX[idl.index(sosTo[0])] +r, masY[idl.index(sosTo[0])]+r, masX[idl.index(sosTo[0])]+20+r, masY[idl.index(sosTo[0])]+20+r, fill=BgColors['Next'])
            canvas.create_text(masX[idl.index(sosTo[0])]+r+10, masY[idl.index(sosTo[0])]+r+10,text=idl[idl.index(sosTo[0])], justify=CENTER, font="Verdana 14")


        if len(sosTo)>1:
            for i in range(len(sosTo)):
                if sosTo[i] not in VisitedPoints and sosFrom2!=[]:
                    est+=1
                    nextP=sosTo[i]
                    if sosFrom[0] not in VisitedPoints:
                        VisitedPoints.append(sosFrom[0])
                        #speed1.append(speed[idl.index(sosFrom[0])])
                        #mass1.append(mass[idl.index(sosFrom[0])])
                    Allvisisted.append(sosFrom[0])    
                    #print(speed[idl.index(sosFrom[0])])
                    print("4Переход из ", sosFrom[0], "в ", nextP)
                    for i1 in range(len(sosFrom)):
                        canvas.create_oval(masX[idl.index(sosFrom[i1])] +r, masY[idl.index(sosFrom[i1])]+r, masX[idl.index(sosFrom[i1])]+20+r, masY[idl.index(sosFrom[i])]+20+r, fill=BgColors['maybe'])
                        canvas.create_text(masX[idl.index(sosFrom[i1])]+r+10, masY[idl.index(sosFrom[i1])]+r+10,text=idl[idl.index(sosFrom[i1])], justify=CENTER, font="Verdana 14")
                        
                    for i2 in range(len(sosTo)):
                        canvas.create_oval(masX[idl.index(sosTo[i2])] +r, masY[idl.index(sosTo[i2])]+r, masX[idl.index(sosTo[i2])]+20+r, masY[idl.index(sosTo[i2])]+20+r, fill=BgColors['maybe'])
                        canvas.create_text(masX[idl.index(sosTo[i2])]+r+10, masY[idl.index(sosTo[i2])]+r+10,text=idl[idl.index(sosTo[i2])], justify=CENTER, font="Verdana 14")
                    #canvas.create_oval(masX[idl.index(sosFrom[0])] +r, masY[idl.index(sosFrom[0])]+r, masX[idl.index(sosFrom[0])]+20+r, masY[idl.index(sosFrom[0])]+20+r, fill=BgColors['Current'])
                    #canvas.create_text(masX[idl.index(sosFrom[0])]+r+10, masY[idl.index(sosFrom[0])]+r+10,text=idl[idl.index(sosFrom[0])], justify=CENTER, font="Verdana 14")

                    canvas.create_oval(masX[idl.index(sosTo[i])] +r, masY[idl.index(sosTo[i])]+r, masX[idl.index(sosTo[i])]+20+r, masY[idl.index(sosTo[i])]+20+r, fill=BgColors['Next'],outline='green')
                    canvas.create_text(masX[idl.index(sosTo[i])]+r+10, masY[idl.index(sosTo[i])]+r+10,text=idl[idl.index(sosTo[i])], justify=CENTER, font="Verdana 14")
                    canvas.create_line(masX[idl.index(sosFrom[0])]+r+10, masY[idl.index(sosFrom[0])]+r+10, masX[idl.index(sosTo[i])] +r+10, masY[idl.index(sosTo[i])]+r+10, width=2, fill="green", arrow=LAST, arrowshape="10 20 10")
                    break
                elif sosTo[i] in VisitedPoints:
                    est-=1
            if est<0:
                if sosFrom[0] not in VisitedPoints:
                    VisitedPoints.append(sosFrom[0])
                    #speed1.append(speed[idl.index(sosFrom[0])])
                    #mass1.append(mass[idl.index(sosFrom[0])])
                    
                    
                if sosTo[0] not in VisitedPoints:
                    VisitedPoints.append(sosTo[0])
                    
                   #speed1.append(speed[idl.index(sosFrom[0])])
                   #mass1.append(mass[idl.index(sosFrom[0])])
                Allvisisted.append(sosTo[0])
                Allvisisted.append(sosFrom[0])
                nextP=sosTo[0]
                paint()
                canvas.create_line(masX[idl.index(sosFrom[0])]+r+10, masY[idl.index(sosFrom[0])]+r+10, masX[idl.index(sosTo[0])] +r+10, masY[idl.index(sosTo[0])]+r+10, width=2, fill="green", arrow=LAST, arrowshape="10 20 10")                
                print("5Переход из ", sosFrom[0], "в ", nextP)
                
        else:
            if sosTo!=[]:
                if sosFrom[0] not in VisitedPoints:
                        VisitedPoints.append(sosFrom[0])
                        #speed1.append(speed[idl.index(sosFrom[0])])
                        #mass1.append(mass[idl.index(sosFrom[0])])
                Allvisisted.append(sosFrom[0])        
                nextP=sosTo[0]
                print("6Переход из ", sosFrom[0], "в ", nextP)
                paint()
                canvas.create_line(masX[idl.index(sosFrom[0])]+r+10, masY[idl.index(sosFrom[0])]+r+10, masX[idl.index(sosTo[0])] +r+10, masY[idl.index(sosTo[0])]+r+10, width=2, fill="green", arrow=LAST, arrowshape="10 20 10")
            else:
                if do+1 not in VisitedPoints:
                        VisitedPoints.append(do+1)
                        Allvisisted.append(do+1)
                        #speed1.append(speed[idl.index(do+1)])
                        #mass1.append(mass[idl.index(do+1)])
                        
                do = t
                abv=1
                ochistka()
    
        if abv!=1:
            if idl.index(sosTo[0]) == idl.index(t+1):
                do = t         
                ochistka()
            elif sosFrom2 == []:            
                do = t
                Allvisisted.append(sosTo[0])
                VisitedPoints.append(sosTo[0])
                #speed1.append(speed[idl.index(sosTo[0])])
                #mass1.append(mass[idl.index(sosTo[0])])
                ochistka()
                tupik+=1
                if tupik>1:
                    if ReturnPoints[-1] == VisitedPoints[-1]:
                        print("До пункта назначения невозможно добраться(Тупик)")
                        u+=1
                        break

            else:
                do = nextP-1
            ReturnPoints=[]
            for i in range(len(VisitedPoints)):
                ReturnPoints.append(VisitedPoints[i])

    
    #print(VisitedPoints)    
    canvas.create_oval(masX[idl.index(t+1)]+r, masY[idl.index(t+1)]+r, masX[idl.index(t+1)]+20+r,
                   masY[idl.index(t+1)]+20+r, fill=BgColors['start'])
    canvas.create_text(masX[idl.index(t+1)]+r+10, masY[idl.index(t+1)]+r+10,
                    text=idl[idl.index(t+1)], justify=CENTER, font="Verdana 14")

    canvas.create_oval(masX[idl.index(l)]+r, masY[idl.index(l)]+r, masX[idl.index(l)] +
                    20+r, masY[idl.index(l)]+20+r, fill=BgColors['finish'])
    canvas.create_text(masX[idl.index(l)]+r+10, masY[idl.index(l)]+r+10,
                    text=idl[idl.index(l)], justify=CENTER, font="Verdana 14")
    #canvas.create_oval(masX[idl.index(VisitedPoints[-1])] +r, masY[idl.index(VisitedPoints[-1])]+r, masX[idl.index(VisitedPoints[-1])]+20+r, masY[idl.index(VisitedPoints[-1])]+20+r, fill=BgColors['Current'])
    #canvas.create_text(masX[idl.index(VisitedPoints[-1])]+r+10, masY[idl.index(VisitedPoints[-1])]+r+10,text=idl[idl.index(VisitedPoints[-1])], justify=CENTER, font="Verdana 14")
    #canvas.create_oval(masX[idl.index(sosTo[0])] +r, masY[idl.index(sosTo[0])]+r, masX[idl.index(sosTo[0])]+20+r, masY[idl.index(sosTo[0])]+20+r, fill=BgColors['Next'],outline='green')
    #canvas.create_text(masX[idl.index(sosTo[0])]+r+10, masY[idl.index(sosTo[0])]+r+10,text=idl[idl.index(sosTo[0])], justify=CENTER, font="Verdana 14")   

    canvas.create_oval(masX[idl.index(sosFrom[0])] +r, masY[idl.index(sosFrom[0])]+r, masX[idl.index(sosFrom[0])]+20+r, masY[idl.index(sosFrom[0])]+20+r, fill=BgColors['Current'],outline='green')
    canvas.create_text(masX[idl.index(sosFrom[0])]+r+10, masY[idl.index(sosFrom[0])]+r+10,text=idl[idl.index(sosFrom[0])], justify=CENTER, font="Verdana 14")   
    canvas.pack()
    canvas.update()
    for i in range(len(masX)):
        canvas.create_oval(masX[i]+r, masY[i]+r,
                        masX[i]+20+r, masY[i]+20+r, fill="orange")
        canvas.create_text(masX[i]+r+10, masY[i]+r+10,
                        text=idl[i], justify=CENTER, font="Verdana 14")
    for i in range(len(VisitedPoints)):
            canvas.create_oval(masX[idl.index(VisitedPoints[i])] +r, masY[idl.index(VisitedPoints[i])]+r, masX[idl.index(VisitedPoints[i])]+20+r, masY[idl.index(VisitedPoints[i])]+20+r, fill=BgColors['visited'])
            canvas.create_text(masX[idl.index(VisitedPoints[i])]+r+10, masY[idl.index(VisitedPoints[i])]+r+10,text=idl[idl.index(VisitedPoints[i])], justify=CENTER, font="Verdana 14")
    
    #print(mass1,speed1)
    
    # print(sosTo)
    # print(nextP)
    # print(posRoutes,VisitedRoutes)
    sosTo2.clear()
    sosFrom2.clear()
    sosTo.clear()
    sosFrom.clear()
    est=0
    abv=0
    time.sleep(2)
    # u+=1
#print(min(speed1))
print(Allvisisted)
if u>=1:
    for i in VisitedPoints:
        mass1.append(mass[idl.index(i)])
        speed1.append(speed[idl.index(i)])
    for i in range(len(Allvisisted)):
        x1 = abs(masX[idl.index(Allvisisted[i])])
        y1 = abs(masY[idl.index(Allvisisted[i])])
        x2 = abs(masX[idl.index(Allvisisted[i]+1)])
        y2 = abs(masY[idl.index(Allvisisted[i]+1)])
        #print(x1,x2,y1,y2)
        #print(round(((x2 * x2)-(x1*x1)) + ((y2*y2) - (y1*y1))))
        distance = round(math.sqrt(abs(((x2 * x2)-(x1*x1)) + ((y2*y2) - (y1*y1)))))
        distanceAr.append(distance)
        
    time1Sum=0
    for i in range(len(distanceAr)):
        time1= distanceAr[0]/speed1[0]
        time1Ar.append(time1)
    time1Sum= round(sum(time1Ar))
    #print(VisitedPoints)
    #print(speed1)
    #print(mass1)
    
#   a = min(speed1)
#   summa = sum(mass1)
#   #print(summa)
#   second =str(datetime.timedelta(seconds=time1Sum))
#   #second = (time1Sum*3600) % 60
#   #time1 = round(math.sqrt(a * a + summa * summa),2)
#   print("Минимальная скорость ",a," м/с")
#   print("Подсчет масс всех путей ", summa, " кг")
#   print ("Время в пути " + str(second)) #second[5:7]
# print(k)
# print(sosFrom)
# print(sosTo)


