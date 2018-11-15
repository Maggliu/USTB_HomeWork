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
                longtitude,latitude=temp.split('\t')
                buildingF.append(float(longtitude))
                buildingF.append(float(latitude))
            self.buildingsF.append(buildingF)
        for baseStation in baseStations:
            self.baseStationF.append([float(k) for k in baseStation.split('\t')])
        self.__findMaxAndmin()
    def __findMaxAndmin(self):
        self.maxlatitude,self.maxlongtitude=0.0,0.0
        self.minlatitude,self.minlongtitude=9999999.0,9999999.0
        for building in self.buildingsF:
            for temp in building[0::2]:
                if self.maxlongtitude<temp:
                    self.maxlongtitude=temp
                if self.minlongtitude>temp:
                    self.minlongtitude=temp
            for temp in building[1::2]:
                if self.maxlatitude<temp:
                    self.maxlatitude=temp
                if self.minlatitude>temp:
                    self.minlatitude=temp
    def getMaxlongtitude(self):
        return self.maxlongtitude
    def getMinlongtitude(self):
        return self.minlongtitude
    def getMaxLatitude(self):
        return self.maxlatitude
    def getMinLatitude(self):
        return self.minlatitude
    def getWidth(self):
        return self.maxlatitude-self.minlatitude
    def getHeight(self):
        return self.maxlongtitude-self.minlongtitude
    def getFixedBuildings(self):
        self.fixedBuildngs=[]
        for building in self.buildingsF:
            buildingFix=[]
            for temp in building:
                if building.index(temp)%2==0:
                    buildingFix.append(temp-self.minlongtitude)
                else:
                    buildingFix.append(self.maxlatitude-temp)
            self.fixedBuildngs.append(buildingFix)
        return self.fixedBuildngs
    def getFixedBaseStations(self):
        self.fixedBaseStations=[]
        for basestation in self.baseStationF:
            temp=[]
            temp.append(basestation[0]-self.minlongtitude)
            temp.append(self.maxlatitude-basestation[1])
            temp.append(basestation[2])
            temp.append(basestation[3])
            self.fixedBaseStations.append(temp)
        return self.fixedBaseStations
