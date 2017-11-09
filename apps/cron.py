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
    print datetime.datetime.now()
    servers=eserver.objects.all()
    for i in servers:
        print i.host,i.dport,i.hport
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
        try:
            ssh.connect(hostname=i.host, port=i.hport, username=i.huser, password=jiemi(i.hpassword))
            stdin, stdout, stderr = ssh.exec_command('/usr/bin/perl /tmp/cutslowlog.perl %s %d %d    > /tmp/slow_5.log && /tmp/pt.sh /tmp/slow_5.log' % (slowname,beftime,curtime))
            # print 'test1'
            # stdin, stdout, stderr = ssh.exec_command('/tmp/pt.sh /tmp/slow_5.log')
            # print 'test2'
            # stdin, stdout, stderr = ssh.exec_command('/usr/bin/pt-query-digest --user=devuser --password=ESBecs00 --history h=10.4.89.185,D=devops,t=global_query_review_history --no-report  --filter=" \$event->{Bytes} = length(\$event->{arg}) and \$event->{hostname}=\"$HOSTNAME\"" %s' % slowname)
            ssh.close()
        except Exception,e:
            print e




