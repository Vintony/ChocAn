import re
import types
class dataItem:
    def __init__(self,name,restrict):
        self.name=name
        self.restrict=restrict
        self.data=""
        if restrict is None:
            raise Exception("the data item of " + self.name + " is not defined!")
    def inputData(self,data):
        pattern=re.compile(self.restrict)
        match=pattern.match(data)
        if match is None:
            raise Exception("the data format of "+self.name+" "+data+" is not legal!")
        self.data=data

    def getData(self):
        return self.data
    def toString(self):
        return self.name+":"+self.data+'\r\n'

class MultiItem():
    def __init__(self,name,elements):
        self.name=name
        self.elements=elements
        self.data=[]
    def inputData(self,data):
        for dict in data:
            d={}
            for element in self.elements:
                di=getDataItem(element)
                di.inputData(dict[element])
                d[element]=di
            self.data.append(d)
    def getData(self):
        data=self.data
        for i in data:
            for j in i:
                i[j]=i[j].getData()
        return data
    def toString(self):
        str=self.name+":\r\n"
        for i in self.data:
            for j in i:
                 str+=j+":"+i[j].getData()+"\r\n"
            str+="\r\n"
        return str
DEFINATION={
    "Member name":"^(\w|\s){0,25}$",
    "Member number":"^\d{9}$",
    "Member street address":"^.{0,25}$",
    "Member city":"^(\w|\s){0,14}$",
    "Member state":"^.{2}$",
    "Member ZIP code":"^\d{5}$",
    "Provider name":"^(\w|\s){0,25}$",
    "Provider number":"^\d{9}$",
    "Provider street address":"^.{0,25}$",
    "Provider city":"^.{0,14}$",
    "Provider state":"^\w{2}$",
    "Provider ZIP code":"^\d{5}$",
    "Current date and time":"(\d{1,2})-(\d{1,2})-(\d{4})\s(\d{2}):(\d{2}):(\d{2})",
    "Service code":"^\d{6}$",
    "Service date":"([0-9]{1,2})-([0-9]{1,2})-([0-9]{4})",
    "Service name":"^(\w|\s){0,25}$",
    "Comments":"^(\w|\s|\'|\.){0,100}$",
    "Fee":"^\$\d{1,3}\.\d+$",
    "Total fee for a week":"^\$\d{1,5}\.\d+$",
    "Total number of consultations":"^\d{3}$",
    "Services in Member record":["Service date","Provider name","Service name"],
    "Services in Provider record":["Service date","Current date and time","Member name","Member number","Service code","Fee"],
}
def getDataItem(dataName):
    if dataName != "Services in Member record" and dataName != "Services in Provider record" :
        return dataItem(dataName, DEFINATION[dataName])
    else:
        return MultiItem(dataName,DEFINATION[dataName])



# pattern=re.compile(
#     "^\$\d+\.\d{2}$"
# )
# match=pattern.match("$11.32")
# print match