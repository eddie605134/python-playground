import pandas as pd 
import os
import re

data=""
with open("F:\\近五年刑事資料庫\\正則練習\\臺灣臺北地方法院民事判決.txt","r",encoding="utf-8") as f:
  data=f.read()
#配對頭
data=data.replace("\n","").replace("\t","").replace(" ","")
result=re.findall("(台|臺)(.*?)(事實及理由|事實與理由|事實|理由)",data,flags=re.S)
temp1=str(result[0]).replace("(","").replace(")","").replace(",","").replace("'","").replace(" ","")


#配對尾
result3=re.search("(中　　華　　民　　國)(.*?)({})".format(data[-10:-1]),data,flags=re.S)
temp2=str(result3[0]).replace("(","").replace(")","").replace(",","").replace("'","").replace(" ","")

#去頭去尾
data=data.replace(temp1,"")
data=data.replace(temp2,"")
print(data)