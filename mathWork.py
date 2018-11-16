import math
from fileread import *
class MathWork:
    def __init__(self,hotnoise,wide,gate,f,baseStations):
        self.gate=gate
        self.const0=46.3
        self.const1=33.9
        self.f=f
        self.const2=13.82
        self.Cm=3
        self.const3=44.9
        self.const4=6.55
        self.hotnoise=hotnoise
        self.wide=wide
        self.baseStations=baseStations
    def getCoverD(self):
        dList=[]
        for baseStation in self.baseStations:
            lgd=(-self.gate+baseStation[3]-self.const0-self.const1*math.log10(self.f)+self.const2*math.log10(baseStation[2])-self.Cm)/(self.const3-self.const4*math.log10(baseStation[2]))
            dList.append(10**lgd*1000)
        return dList
    def getSi(self,x0,y0,x1,y1,ht,Pbi):
        d=self.__getDistance(x0,y0,x1,y1)/1000
        Si=Pbi-self.const0-self.const1*math.log10(self.f)+self.const2*math.log10(ht)-(self.const3-self.const4*math.log10(ht))*math.log10(d)-self.Cm
        return Si
    def getAllsi(self,x0,y0):
        siList=[]
        for baseStation in self.baseStations:
            temp=self.getSi(x0,y0,baseStation[0],baseStation[1],baseStation[2],baseStation[3])
            siList.append(temp)
        return siList
    def __getDistance(self,x0,y0,x1,y1):
        temp=(x0-x1)**2+(y0-y1)**2
        return math.sqrt(temp)
    def getMaxDownload(self,x0,y0):
        siList=self.getAllsi(x0,y0)
        maxSi=max(siList)
        maxSimW=self.dBmTomW(maxSi)
        siListmW=[self.dBmTomW(k) for k in siList]
        hotNoisemW=self.dBmTomW(self.hotnoise)*self.wide
        temp=self.wide*math.log2(1+maxSimW/(sum(siListmW)-maxSimW+hotNoisemW))
        return temp
    def dBmTomW(self,dBm):
        return 10**(dBm/10)
    def getAllMaxDownload(self,x0,y0,steep,width,height):
        downloadDic={}
        rangeX=int(width/steep)
        rangeY=int(height/steep)
        for x in range(rangeX):
            for y in range(rangeY):
                downloadDic[(x,y)]=self.getMaxDownload(x0+steep*x,y0+steep*y)
        return downloadDic
#filrea=FileRead()
#mathwork=MathWork(-174,15000,-110,900,filrea.getFixedBaseStations())
