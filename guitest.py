import tkinter as tk
filet=open("D:\\PythonProject\\mainWork\\beijingdata.txt",mode='r')
mesList=filet.readlines()
mesListSize=len(mesList)
buildings=[]
buildingsF=[]
baseStations=[]
baseStationsF=[]
fixBuidingsF=[]
leftClick='<Button-1>'
count=0
while mesListSize-count>0:
    temp=mesList[count].split("\t")
    if temp[1]==' buildings ':
        buildings.append(mesList[count+1:int(temp[2])+1+count])
        count+=int(temp[2])+1
    else:
        baseStations.append(mesList[count+1])
        count+=2
for building in buildings:
    buildingF=[]
    for temp in building:
        longtitude,latitude=temp.split('\t')
        buildingF.append(float(longtitude)-440510.738801)
        buildingF.append(4430450.163423-float(latitude))
    buildingsF.append(buildingF)
for baseStation in baseStations:
    baseStationsF.append([float(k) for k in baseStation.split('\t')])
fixedBaseStations=[]
for basestation in baseStationsF:
    temp=[]
    temp.append(basestation[0]-440510.738801)
    temp.append(4430450.163423-basestation[1])
    temp.append(basestation[2])
    temp.append(basestation[3])
    fixedBaseStations.append(temp)
master=tk.Tk()
cav=tk.Canvas(master,height=3320/5,width=5700/5)
cav.grid(row=0,column=0,rowspan=22,columnspan=22)
def moveRight(event):
    cav.move("building",50,0)
def moveLeft(event):
    cav.move("building",-50,0)
def moveUp(event):
    cav.move("building",0,-50)
def moveDown(event):
    cav.move("building",0,50)
def zoomM(event):
    cav.scale('building',3320/25,5700/25,1.1,1.1)
def little(event):
    cav.scale('building',3320/25,5700/25,0.9,0.9)
left=tk.Button(master=master,width=5,text="左移")
left.bind(leftClick,moveLeft)
left.grid(row=17,column=25,rowspan=2,columnspan=2)
right=tk.Button(master=master,width=5,text="右移")
right.bind(leftClick,moveRight)
right.grid(row=17,column=29,rowspan=2,columnspan=2)
up=tk.Button(master=master,width=5,text="上移")
up.bind(leftClick,moveUp)
up.grid(row=16,column=27,rowspan=2,columnspan=2)
down=tk.Button(master=master,width=5,text="下移")
down.bind(leftClick,moveDown)
down.grid(row=18,column=27,rowspan=2,columnspan=2)
zoom=tk.Button(master=master,width=5,text="放大")
zoom.bind(leftClick,zoomM)
zoom.grid(row=20,column=29,rowspan=2,columnspan=2)
suoxia=tk.Button(master=master,width=5,text="缩小")
suoxia.bind(leftClick,little)
suoxia.grid(row=20,column=25,rowspan=2,columnspan=2)
for building in buildingsF:
    cav.create_polygon([k/5 for k in building],fill="",outline="black")
for base in fixedBaseStations:
    cav.create_oval(base[0]/5-5,base[1]/5-5,base[0]/5+5,base[1]/5+5,fill='red')
cav.addtag_all("building")
tk.mainloop()