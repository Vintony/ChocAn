#-*- coding: UTF-8 -*-
import records
import IO
import ProviderDirectory as pd
from datetime import datetime

reporttime = datetime.now().strftime('%Y-%m-%d')

def validMemberNumber(code):        #根据编号，返回该成员是否存在
    return IO.fileExist("data/member/"+code)
def validProviderNumber(code):
    return IO.fileExist("data/provider/" + code)
def validServiceCode(code):
    p=pd.ProviderDirectory()
    return p.valid(code)
def printPD():                   #返回所有服务列表
    p=pd.ProviderDirectory()
    return p.getAllItems()
def storeServiceRecord(dict):    #存储服务记录
    service=records.service(dict)
    service.store()
def addMember(dict):            #添加一个成员，下面是更新，删除
    m=records.member(dict)
    m.store()
def updateMember(number,dict):  #更新一个成员信息，输入编号和｛"更新项"：数据｝
    m=records.getMemberByNumber(number)
    m.updateItem(dict)
def delMember(number):
    m=records.getMemberByNumber(number)
    m.delRecord()
def addProvider(dict):      #教练的增删改
    p=records.provider(dict)
    p.store()
def updateProvider(number,dict):
    p=records.getProviderByNumber(number)
    p.updateItem(dict)
def delProvider(number):
    p=records.getProviderByNumber(number)
    p.delRecord()
def addServiceInPD(code,name,fee):      #在provider directory中添加服务
    print(code)
    print(name)
    print(fee)
    p=pd.ProviderDirectory()
    p.append(code,name,fee)
def addServiceRecord(dict):
    s=records.service(dict)
    s.store()
def storeMemberReport(membernumber):       #存储发送给成员的每周报告，在member report里面
    mb = records.getMemberByNumber(membernumber).getDict()
    services=records.getServicesByMemberNumber(membernumber)
    p=pd.ProviderDirectory()
    s=[]
    for service in services:
        provider=records.getProviderByNumber(service["Provider number"]).getDict()

        s.append({
            "Service date": service["Service date"],
            "Provider name": provider["Provider name"],
            "Service name": p.getServiceByCode(service["Service code"])["Service name"]
        })
    mb["Services in Member record"]=s
    print(mb)
    mr=records.MemberRecord(mb)
    mr.store()


def storeProviderReport(providernumber):      #存储发送给教练的每周报告，在provider report里面
    provider=records.getProviderByNumber(providernumber).getDict()
    services = records.getServicesByProviderNumber(providernumber)
    p = pd.ProviderDirectory()
    totalfee=0.00
    sp=[]
    numbers=len(services)
    for s in services:
        m=records.getMemberByNumber(s["Member number"]).getDict()
        f=p.getServiceByCode(s["Service code"])["Fee"]
        totalfee+=float(f[1:])
        sp.append({
            "Service date":s["Service date"],
            "Current date and time":s["Current date and time"],
            "Member name":m["Member name"],
            "Member number":s["Member number"],
            "Service code":s["Service code"],
            "Fee":f.replace("\r\n","")
        })
        sp.sort(key=cmpDate)
    provider["Services in Provider record"]=sp
    provider["Total fee for a week"]="$"+str(totalfee)
    provider["Total number of consultations"]=str(numbers).zfill(3)
    print(provider)
    pr=records.ProviderRecord(provider)
    pr.store()


def storeManagerReport():            #存储发送给经理的报告，在managerreport中
    providers=records.getProviders()
    PD = pd.ProviderDirectory()
    report={}
    providerInf=[]
    totalProvider=0
    totalConsultation=0
    totalFee=0.00
    for p in providers:
        providerNumber=p["Provider number"]
        providerName=p["Provider name"]
        serviceName=[]
        serviceCode=[]
        serviceDate=[]
        Fee=0.00
        services=records.getServicesByProviderNumber(providerNumber)
        if len(services)==0:
            continue
        for i in services:
            service=PD.getServiceByCode(i["Service code"])
            serviceName.append(service["Service name"])
            serviceCode.append(i["Service code"])
            serviceDate.append(i["Service date"])
            Fee+=float(service["Fee"][1:])
            totalConsultation+=1
        providerInf.append({
            "Provider name":providerName.replace('\n',''),
            "Provider number":providerNumber.replace('\n',''),
            "Service name":serviceName.replace('\n',''),
            "Service code":serviceCode.replace('\n',''),
            "Service date":serviceDate.replace('\n',''),
            "Fee":Fee
        })
        totalProvider+=1
        totalFee+=Fee
    report["Provider information"]=providerInf
    report["Provider counts"]=totalProvider
    report["totalConsultation"]=totalConsultation
    report["totalFee"]=totalFee

    string=""
    for i in report["Provider information"]:
        string+="Provider name:"+i["Provider name"]+"\r\n"
        string+="Provider number:"+i["Provider number"]+"\r\n"
        string+="Provider name:" + i["Provider name"] + "\r\n"
        string+="Services information:\r\n"
        for j in range(len(i["Service name"])):
            string+="   "+i["Service name"][j]+"   "
            string+="   "+i["Service code"][j]+"   "
            string+="   "+i["Service date"][j]+"   \r\n"
        string+="\r\n"
    string+="\r\n"
    string+="Provider counts:"+str(report["Provider counts"])+"\r\n"
    string+="Total consultation:"+str(report["totalConsultation"])+"\r\n"
    string+="Total fee:"+str(report["totalFee"])+"\r\n"
    IO.toFile("data/manager report/"+reporttime,string)


def storeBill():               #生成账单，包含教练名，教练编号，钱数
    providers = records.getProviders()
    PD = pd.ProviderDirectory()
    providerInf = []
    totalConsultation = 0
    for p in providers:
        providerNumber = p["Provider number"]
        providerName = p["Provider name"]
        Fee = 0
        services = records.getServicesByProviderNumber(providerNumber)
        if len(services) == 0:
            continue
        for i in services:
            service = PD.getServiceByCode(i["Service code"])
            Fee += float(service["Fee"][1:])
            totalConsultation += 1
        providerInf.append({
            "Provider name": providerName,
            "Provider number": providerNumber,
            "Fee": Fee
        })
    string=""
    for i in providerInf:
        string+=i["Provider name"]+"  "+i["Provider number"]+"  "+str(i["Fee"])+"\r\n"
    IO.toFile("data/bill/"+reporttime, string)




def cmpDate(x):
    date1=x["Service date"].split("-")
    distance=(float(date1[2]))*365+(float(date1[0]))*30+(float(date1[1]))
    return distance

# 测试
# addProvider({
#     "Provider name":"van",
#         "Provider number":"000000001",
#         "Provider street address":"asdfghjasdf",
#         "Provider city":"asdfsdaf",
#         "Provider state":"GD",
#         "Provider ZIP code":"12345"
# })
# addMember({
#     "Member name":"asf",
#     "Member number":"000000005",
#     "Member street address":"asdfasdgww",
#     "Member city":"asgwaegreg",
#     "Member state":"er",
#     "Member ZIP code":"12346"
# })
# print(printPD())
# addServiceRecord({
# "Current date and time":"5-27-2017 11:11:11",
#         "Service date":"5-22-2017",
#          "Provider number":"000000001",
#         "Member number":"000000006",
#         "Service code":"100005",
#          "Comments":"that's good."
# })
# storeProviderRecord("000000001")
# storeMemberRecord("000000001")
# storeManagerReport()
# storeBill()
# updateMember("000000004",{"Member name":"tesggg"})
# delMember("000000001")