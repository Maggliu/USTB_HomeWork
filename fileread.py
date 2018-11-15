class FileRead:
    def __init__(self):
        self.file=open("D:\\PythonProject\\mainWork\\beijingdata.txt",mode='r')
        mesList=self.file.readlines()
        mesListSize=len(mesList)
        buildings=[]
        self.buildingsF=[]
        baseStations=[]
        self.baseStationF=[]
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
                x,y=temp.split('\t')
                buildingF.append(float(x))
                buildingF.append(float(y))
            self.buildingsF.append(buildingF)
        for baseStation in baseStations:
            self.baseStationF.append([float(k) for k in baseStation.split('\t')])
        self.__findMaxAndmin()
    def __findMaxAndmin(self):
        self.maxX,self.maxY=0.0,0.0
        self.minX,self.minY=9999999.0,9999999.0
        for building in self.buildingsF:
            for temp in building[0::2]:
                if self.maxX<temp:
                    self.maxX=temp
                if self.minX>temp:
                    self.minX=temp
            for temp in building[1::2]:
                if self.maxY<temp:
                    self.maxY=temp
                if self.minY>temp:
                    self.minY=temp
    def getMaxX(self):
        return self.maxX
    def getMinX(self):
        return self.minX
    def getMaxY(self):
        return self.maxY
    def getMinY(self):
        return self.minY
    def getWidth(self):
        return self.maxX-self.minX
    def getHeight(self):
        return self.maxY-self.minY
    def getFixedBuildings(self):
        self.fixedBuildngs=[]
        for building in self.buildingsF:
            buildingFix=[]
            for temp in building:
                if building.index(temp)%2==0:
                    buildingFix.append(temp-self.minX)
                else:
                    buildingFix.append(self.maxY-temp)
            self.fixedBuildngs.append(buildingFix)
        return self.fixedBuildngs
    def getFixedBaseStations(self):
        self.fixedBaseStations=[]
        for basestation in self.baseStationF:
            temp=[]
            temp.append(basestation[0]-self.minX)
            temp.append(self.maxY-basestation[1])
            temp.append(basestation[2])
            temp.append(basestation[3])
            self.fixedBaseStations.append(temp)
        return self.fixedBaseStations