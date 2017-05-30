#-*- coding: UTF-8 -*-
import json
import os
def toJson(path,dict):           #根据字典生成json
    fp = open(path, 'w')
    dict=json.dumps(dict,ensure_ascii=False)
    fp.write(dict)
    fp.close()

def getJson(path):          #从文件读，返回字典
    f = open(path)
    s = json.load(f)
    return s
def toFile(path,str):
    f=open(path,"w")
    f.write(str)
    f.close()
def getDict(path):
    result={}
    f=open(path)
    for i in f:
        if len(i)<5:
            continue
        print(str(i))
        i=i.split(':',1)
        result[i[0]]=i[1].replace("\n","")
    return result

def delFile(path):
    try:
        os.remove(path)
    except Exception:
        return
def getAllfile(dir):
    result=[]
    try:
        for filenames in os.walk(dir):
            for f in filenames[2]:
                d=getDict(filenames[0]+"/"+f)
                result.append(d)
    except Exception:
        return None
    return result
def fileExist(path):
    return os.path.exists(path)