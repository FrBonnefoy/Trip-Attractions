from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import Future
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from bs4 import BeautifulSoup as soup
import pandas as pd
import re
import random
import time
user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
headers = {'User-Agent': user_agent}
import os.path
from os import path
fhandly=open('tripurl_attr.txt')
urls=fhandly.readlines()
urls=list(dict.fromkeys(urls))
print(len(urls))
fhandly.close()
urls=list(map(lambda x: x.strip(),urls))
if path.exists("done.txt"):
    pass
else:
    fhandle2=open('done.txt','w')
    fhandle2.close()
with open('done.txt') as f1:
    done_lines=f1.readlines()
done_lines=list(map(lambda x: x.strip(),done_lines))
urls= [item for item in urls if item not in done_lines]
print(len(urls))
if path.exists("tripattr.csv"):
    pass
else:
    headers='URL\tNom\tType\tRank\tLocation\tNumber of Comments\tNote\tTéléphone\n'
    fhandle=open('tripattr.csv','w')
    fhandle.write(headers)
    fhandle.close()
def getinfo(x):
    time.sleep(random.uniform(1,2))
    r=requests.get(x,headers)
    sopa=soup(r.content,'html.parser')
    nom=''
    type=''
    rank=''
    location=''
    comments=''
    note=''
    phone=''

    c4=sopa.findAll('div',{'class':'LjCWTZdN'})

    c4_=sopa.findAll('div',{'class':'LjCWTZdN'})

    c3=sopa.findAll('div',{'class':'eQSJNhO6'})

    c3_=sopa.findAll('div',{'class':'_21dlsAZ_'})

    c2=sopa.findAll('div',{'class':'_3RTCF0T0'})

    c2_=sopa.findAll('div',{'class':'_3Hy8aRST'})

    c1=sopa.findAll('h1',{'class':'ui_header h1'})

    c1_=sopa.findAll('h1',{'class':'_3QHreJVJ'})

    c5=sopa.findAll('span',{'class':'_3WF_jKL7 _1uXQPaAr'})

    c5_=sopa.findAll('span',{'class':'reviewCount _16Nxw4iy'})

    c6=sopa.findAll('span',{'class':'_2Hy7Xxdm'})

    c6_=sopa.findAll('div',{'class':'ui_poi_review_rating'})

    c7=sopa.findAll('a',{'class':'_TF8HH3_'})

    try:
        nom=c1[0].text.strip()
    except:
        try:
            nom=c1_[0].text.strip()
        except:
            pass
    try:
        type=c2[0].text.strip()
    except:
        try:
            type=c2_[0].text.strip()
        except:
            pass
    try:
        rank=c3[0].text.strip()
    except:
        try:
            rank=c3_[0].text.strip()
        except:
            pass
    try:
        location=c4[0].text.strip()
    except:
        pass
    try:
        comments=c5[0].text.strip()
    except:
        try:
            comments=c5_[0].text.strip()
        except:
            pass
    try:
        note=c6[0].text.strip()
    except:
        try:
            temp=str(c6_[0])
            temp=re.findall(r'bubble_(\d+)',temp)
            note=int(temp[0])/10
        except:
            pass
    try:
        phone=c7[0].text.strip()
    except:
        pass
    urly = x
    varlist=[urly,nom,type,rank,location,comments,note,phone]
    to_append=varlist
    s = pd.DataFrame(to_append).T
    s.to_csv('tripattr.csv', mode='a', header=False,sep='\t',index=False)
    with open('done.txt','a') as f:
        print(urly,file=f)
    print(urly)

with ThreadPoolExecutor(max_workers=5) as executor:
    future_results = [executor.submit(getinfo, url) for url in urls]
    results=[]
    for future in as_completed(future_results):
        results.append(future.result())
