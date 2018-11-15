import math
from fileread import *
class MathWork:
    def __init__(self,gate,f):
        self.gate=gate
        self.const0=46.3
        self.const1=33.9
        self.f=f
        self.const2=13.82
        self.Cm=3
        self.const3=44.9
        self.const4=6.55
    def getCoverD(self,ht,Pbi):
        lgd=(self.gate-Pbi+self.const0+self.const1*math.log10(self.f)+self.const2*math.log10(ht)-self.Cm)/(self.const3-self.const4*math.log10(ht))
        return 10**lgd*1000
    def getSi(self,x0,y0,x1,y1,ht,Pbi):
        d=self.__getDistance(x0,y0,x1,y1)/1000
        Si=Pbi-self.const0-self.const1*math.log10(self.f)-self.const2*math.log10(ht)+(self.const3-self.const4*math.log10(ht))*math.log10(d)+self.Cm
        return Si
    def getRSRP(self,x0,y0,baseStations):
        maxSic=-9999999
        for baseStation in baseStations:
            temp=self.getSi(x0,y0,baseStation[1],baseStation[0],baseStation[2],baseStation[3])
            if temp>maxSic:
                maxSic=temp
        return maxSic
    def __getDistance(self,x0,y0,x1,y1):
        temp=(x0-x1)**2+(y0-y1)**2
        return math.sqrt(temp)
filereader=FileRead()
mathwork=MathWork(-110,900)
print(mathwork.getCoverD(filereader.getFixedBaseStations()[0][2],filereader.getFixedBaseStations()[0][3]))
print(mathwork.getRSRP(0,0,filereader.getFixedBaseStations()))