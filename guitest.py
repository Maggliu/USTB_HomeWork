import tkinter as tk
filet=open("D:\\PythonProject\\mainWork\\beijingdata.txt",mode='r')
mesList=filet.readlines()
mesListSize=len(mesList)
buildings=[]
buildingsF=[]
baseStations=[]
baseStationsF=[]
fixBuidingsF=[]
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
print(buildingsF[1])
master=tk.Tk()
cav=tk.Canvas(master,height=3320/5,width=5700/5)
cav.grid(row=0,column=0,rowspan=22,columnspan=22)
left=tk.Button(master=master,width=5,text="左移")
left.grid(row=17,column=25,rowspan=2,columnspan=2)
def moveRight(event):
    cav.move("building",50,0)
right=tk.Button(master=master,width=5,text="右移")
right.bind('<Button-1>',moveRight)
right.grid(row=17,column=29,rowspan=2,columnspan=2)
top=tk.Button(master=master,width=5,text="上移")
top.grid(row=16,column=27,rowspan=2,columnspan=2)
down=tk.Button(master=master,width=5,text="下移")
down.grid(row=18,column=27,rowspan=2,columnspan=2)
zoom=tk.Button(master=master,width=5,text="放大")
zoom.grid(row=20,column=29,rowspan=2,columnspan=2)
suoxia=tk.Button(master=master,width=5,text="缩小")
suoxia.grid(row=20,column=25,rowspan=2,columnspan=2)
#img=cav.create_image(image.width()/2,image.height()/2,image=image)
for building in buildingsF:
    cav.create_polygon([k/5 for k in building],fill="",outline="black")
cav.addtag_all("building")
tk.mainloop()