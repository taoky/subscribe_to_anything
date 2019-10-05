```
apt-get install python3 python3-dev python3-pip mysql-server mysql-client libmysqlclient-dev libxml2-dev
pip3 install -r requirements.txt
mysql -u root -p
CREATE DATABASE sta;
GRANT ALL ON sta.* to 'sta'@'localhost' identified by 'sta';
cp config/example.py config/default.py
./run.py
```

zzh1996: 「我觉得这个项目很糟糕，建议重写一个」

所以不改了，等我有空时候重新整一个吧。目前这个 repo 删掉了注册账户的功能，加入了 Dockerfile，并让它能使用最新的模块跑起来。

已知的安全问题：密码明文存储、SSRF。
