# -*- coding: utf-8 -*-
import  MySQLdb
import sys
import paramiko
####ping

dbuser='devuser'
dbpass='ESBecs00'

def mysqlping(v_port,v_host):
    try:
        db = MySQLdb.connect(user=dbuser, passwd=dbpass, db="mysql", port=v_port, host=v_host,charset="utf8")
    except Exception as e:
        return 'ERROR'
        # print "Error %d:%s"%(e.args[0],e.args[1])
    else:
        return 'SUCCESS'

##mysql grant_read
def mysqlgrant_read(v_port,v_host,tar_user,tar_pass):
    conn = MySQLdb.connect(user=dbuser, passwd=dbpass, db="mysql", port=v_port, host=v_host,charset="utf8")
    cursor = conn.cursor()
    #sql = "select '%s@%s';" %(tar_user,tar_pass)
    sql = "grant select on *.* to '%s'@'%s' identified by '%s' ;" %(tar_user,'%',tar_pass)
    n = cursor.execute(sql)
    row = cursor.fetchall()
    print row
    cursor.close()
    conn.close()

    ##mysql grant_read
def mysqlgrant_write(v_port, v_host, tar_user, tar_pass):
        conn = MySQLdb.connect(user=dbuser, passwd=dbpass, db="mysql", port=v_port, host=v_host, charset="utf8")
        cursor = conn.cursor()
        # sql = "select '%s@%s';" %(tar_user,tar_pass)
        sql = "grant all on *.* to '%s'@'%s' identified by '%s' ;" % (tar_user, '%', tar_pass)
        n = cursor.execute(sql)
        row = cursor.fetchall()
        print row
        cursor.close()
        conn.close()
# sta=mysqlping(3306,'47.93.243.162')
# print sta
# mysqlgrant_read(3306,'47.93.243.162','testuser','testuser')


def mysqlgrant_revoke(v_port, v_host, tar_user):
    conn = MySQLdb.connect(user=dbuser, passwd=dbpass, db="mysql", port=v_port, host=v_host, charset="utf8")
    cursor = conn.cursor()
    # sql = "select '%s@%s';" %(tar_user,tar_pass)
    sql = "drop user '%s'@'%s';" % (tar_user,'%')
    n = cursor.execute(sql)
    row = cursor.fetchall()
    print row
    cursor.close()
    conn.close()


##mysql grant_read
def mycat_dml(v_port,v_host,v_db,v_sql):
    conn = MySQLdb.connect(user=dbuser, passwd=dbpass, db=v_db, port=v_port, host=v_host,charset="utf8")
    cursor = conn.cursor()
    #sql = "select '%s@%s';" %(tar_user,tar_pass)
    sql = "%s" % v_sql
    n = cursor.execute(sql)
    row = cursor.fetchall()
    print row
    cursor.close()
    conn.close()
# mycat_dml(3306,'10.32.7.139','ecejmaster0','select now();')


###sshping
def sshping(vhost,vport,vuser,vpass):
    try:
        t = paramiko.Transport((vhost, vport))
        t.connect(username=vuser, password=vpass)
        sftp = paramiko.SFTPClient.from_transport(t)

    except Exception,e:
        return 'error'
    return 'success'


###推送慢日志切割脚本pt脚本至/tmp目录下
def trans_cut_slow(vhost,vport,vuser,vpass):
    try:
        t = paramiko.Transport((vhost, vport))
        t.connect(username=vuser, password=vpass)
        sftp = paramiko.SFTPClient.from_transport(t)
        sftp.put('/home/cutslowlog.perl', '/tmp/cutslowlog.perl')  ##上传
        sftp.put('/home/pt.sh', '/tmp/pt.sh')  ##上传
    except Exception,e:
        pass

# print sshping('10.4.89.183',22,'root','1234')
#


