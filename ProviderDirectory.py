import dataItem
import IO
#-*- coding: UTF-8 -*-
class ProviderDirectory:
    def __init__(self):
        self.items=["Service name","Service code","Fee"]
    def append(self,code,name,fee):
        c=dataItem.getDataItem("Service code")
        c.inputData(code)
        n = dataItem.getDataItem("Service name")
        n.inputData(name)
        f = dataItem.getDataItem("Fee")
        f.inputData(fee)
        if self.valid(code)==0:
            raise Exception("the service already exist.")
        items=self.getAllItems()
        items.append({"Service name":n.getData(),"Service code":c.getData(),"Fee":f.getData()})
        print(items)
        self.store(items)
    def sort(self):
        pd = open("data/ProviderDirectory", "r")
        lines=pd.readlines()
        lines.sort()
        pd.close()
        pd = open("data/ProviderDirectory", "w")
        for l in lines:
            if l=="\r\n":
                continue
            pd.write(l)
        pd.close()
    def getAllItems(self):
        items=[]
        f=open("data/ProviderDirectory","r")
        lines=f.readlines()
        for i in lines:
            if i=="\n":
                continue
            item={}
            i=i.split('  ')
            print(i)
            item["Service name"]=i[0]
            item["Service code"]=i[1]
            item["Fee"]=i[2].replace('\n','')
            items.append(item)
        print(items)
        return items
    def valid(self,code):
        items=self.getAllItems()
        for i in items:
            if code==i["Service code"]:
                return False
        return True
    def store(self,list):
        f = open("data/ProviderDirectory","w")
        for i in list:
            f.write(i["Service name"]+"  "+i["Service code"]+"  "+i["Fee"]+'\r\n')
        f.close()
        self.sort()
    def delItem(self,code):
        items=self.getAllItems()
        print(items)
        index=None
        for i in range(len(items)):
            if items[i]["Service code"]==code:
                index=i
                break
        del items[index]
        self.store(items)
    def getServiceByCode(self,code):
        items=self.getAllItems()
        for i in items:
            if i["Service code"]==code:
                return i



# p=ProviderDirectory()
# p.append("100000","f","$123.22")
# p.append("100001","a","$123.22")
# p.append("100002","gs","$123.22")
# p.append("100003","de","$123.22")
#p.Sort()