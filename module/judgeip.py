#coding:utf-8
# author : p0desta
import requests
import paramiko
import threading
import  time
import argparse

def split(ip): # 判断是一个IP还是一个IP段
    ips = len(ip.split('-'))
    iplist= []
    if ips == 1:
        iplist.append(ip)
        return iplist
    else:
        #print ip.split("-")[0][:-len(ip.split("-")[0].split(".")[-1])]
        ipfinal = ip.split('-')[0][:-len(ip.split('-')[0].split('.')[-1])]
        #print ipfinal
        for i in range(int(ip.split('-')[0].split('.')[-1]), int(ip.split('-')[1]) + 1):
            iplist.append(ipfinal+str(i))
        return iplist