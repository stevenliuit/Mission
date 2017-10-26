#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#author:JC
import time
import datetime
import paramiko
import  MySQLdb
from common.utils.crypt import jiemi
from apps.models import *
dbuser='devuser'
dbpass='ESBecs00'


def getname():
    print '123'

###切割慢日志
def cut_slow_log():
    dtime = datetime.datetime.now()
    curtime = time.mktime(dtime.timetuple())
    beftime = curtime - 300
    servers=eserver.objects.all()
    for i in servers:
        print i.host,i.dport,i.hport,i.huser,jiemi(i.hpassword),curtime,beftime
        conn = MySQLdb.connect(user=dbuser, passwd=dbpass, db="mysql", port=i.dport, host=i.host, charset="utf8")
        cursor = conn.cursor()
        sql = "show global variables like 'slow_query_log_file';"
        n = cursor.execute(sql)
        row = cursor.fetchall()
        slowname = row[0][1]
        print slowname
        cursor.close()
        conn.close()

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.load_system_host_keys()
        ssh.connect(hostname=i.host, port=i.hport, username=i.huser, password=jiemi(i.hpassword))
        stdin, stdout, stderr = ssh.exec_command('/usr/bin/perl /tmp/cutslowlog.perl %s %d %d    > /tmp/slow_5.log' % (slowname,beftime,curtime))
        status = stdout.read()
        print status



cut_slow_log()


