#-*- coding: UTF-8 -*-
import dataItem
import IO
import ProviderDirectory as pd
from datetime import datetime

reporttime = datetime.now().strftime('%Y-%m-%d')
class record:
    def __init__(self):
        self.items={}
        self.itemnames=[]
        self.storepath=""
    def creatRecord(self,datas):

        for i in self.itemnames:
            item = dataItem.getDataItem(i)
            item.inputData(datas[item.name])
            self.items[item.name] = item

    def show(self):
        for i in self.itemnames:
            print(self.items[i].toString())
    def updateItem(self,dict):
        IO.delFile(self.storepath)
        for i in dict:
            self.items[i].inputData(dict[i])
        self.store()
    def getDict(self):
        dict={}
        for i in self.items:
            dict[i]=self.items[i].getData()
        return dict
    def store(self):
        str=""
        for i in self.itemnames:
            str+=self.items[i].toString()
        IO.toFile(self.storepath,str)
    def delRecord(self):
        IO.delFile(self.storepath)

class provider(record):
    def __init__(self,datas):
        record.__init__(self)
        self.itemnames=[
        "Provider name",
        "Provider number",
        "Provider street address",
        "Provider city",
        "Provider state",
        "Provider ZIP code"
        ]
        record.creatRecord(self,datas)
        self.storepath="data/provider/"+self.items["Provider number"].getData()

class member(record):

    def __init__(self,datas):
        record.__init__(self)
        self.itemnames=[
        "Member name",
        "Member number",
        "Member street address",
        "Member city",
        "Member state",
        "Member ZIP code"
    ]
        record.creatRecord(self,datas)
        self.storepath="data/member/" + self.items["Member number"].getData()
class service(record):
    def __init__(self,datas):
        record.__init__(self)
        self.itemnames=[
        "Current date and time",
        "Service date",
         "Provider number",
        "Member number",
        "Service code",
         "Comments"
        ]
        record.creatRecord(self,datas)
        self.storepath="data/services record/"+self.items["Member number"].getData()+"-"+self.items["Service code"].getData()+"-"+self.items["Service date"].getData()
    def valid(self):
        p=pd.ProviderDirectory()
        s=p.getServiceByCode(self.items["Service code"].getData())
        if s is None:
            raise Exception("this service is not exist in Provider Directory.")
class MemberRecord(record):
    def __init__(self, datas):
        record.__init__(self)
        self.itemnames = [
                "Member name",
                "Member number",
                "Member street address",
                "Member city",
                "Member state",
                "Member ZIP code",
                "Services in Member record"
            ]
        record.creatRecord(self, datas)
        self.storepath="data/member report/"+self.items["Member name"].getData()+" "+reporttime

class ProviderRecord(record):
    def __init__(self, datas):
        record.__init__(self)
        self.itemnames = [
                "Provider name",
                "Provider number",
                "Provider street address",
                "Provider city",
                "Provider state",
                "Provider ZIP code",
                "Services in Provider record",
                "Total fee for a week",
                "Total number of consultations"
            ]
        record.creatRecord(self, datas)
        self.storepath="data/provider report/"+self.items["Provider name"].getData()+" "+reporttime


def getProviders():         #返回所有provider记录
    return IO.getAllfile("data/provider")

def getProviderByNumber(number):   #根据编号 返回一个provider记录 （字典形式）
    if IO.fileExist("data/provider/" + number):
        p=provider(IO.getDict("data/provider/" + number))
        return p
    else:
        raise Exception("this provider did not exist.")
def getMembers():           #返回所有成员
    return IO.getAllfile("data/member")

def getMemberByNumber(number):    #根据编号返回成员
    if IO.fileExist("data/member/" + number):
        m = member(IO.getDict("data/member/" + number))
        return m
    else:
        raise Exception("this member did not exist.")
def getServices():        #返回所有服务
    return IO.getAllfile("data/services record")

def getServicesByProviderNumber(number):      #根据教练编号返回对应服务
    temp=IO.getAllfile("data/services record")
    result=[]
    for i in temp:
        if i["Provider number"] == number:
            result.append(i)
    return result

def getServicesByMemberNumber(number):     #根据成员编号返回对应服务
    Services=IO.getAllfile("data/services record")
    result=[]
    for i in Services:
        if i["Member number"] == number:
            result.append(i)
    return result


# Services={
#                 "Member name":"sb",
#                 "Member number":"123456789",
#                 "Member street address":"37 st",
#                 "Member city":"london",
#                 "Member state":"SB",
#                 "Member ZIP code":"12345",
#                 "Services in Member record":[
#                     {
#                         "Service date":"12-22-2017 12:22:43",
#                         "Provider name":"dick",
#                         "Service name":"ass ass in"
#                     },
#                     {
#                         "Service date":"12-21-2017 12:22:43",
#                         "Provider name":"dick",
#                         "Service name":"ass ass in"
#                     }
#
#                 ]
# }
# mr=MemberRecord(Services)
# mr.show()
# mr.store()


