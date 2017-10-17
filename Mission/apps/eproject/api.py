# -*- coding: utf-8 -*-
import  MySQLdb
####ping
def mysqlping(v_port,v_host):
    try:
        db = MySQLdb.connect(user='root', passwd='ESBecs00', db="mysql", port=v_port, host=v_host,charset="utf8")
    except Exception as e:
        return 'ERROR'
        # print "Error %d:%s"%(e.args[0],e.args[1])
    else:
        return 'SUCCESS'

##mysql grant_read
def mysqlgrant_read(v_port,v_host,tar_user,tar_pass):
    conn = MySQLdb.connect(user='root', passwd='ESBecs00', db="mysql", port=v_port, host=v_host,charset="utf8")
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
        conn = MySQLdb.connect(user='root', passwd='ESBecs00', db="mysql", port=v_port, host=v_host, charset="utf8")
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

##mysql grant_read
def mycat_dml(v_port,v_host,v_db,v_sql):
    conn = MySQLdb.connect(user='dbaadmin', passwd='PDwkWb11GwdUhrxh', db=v_db, port=v_port, host=v_host,charset="utf8")
    cursor = conn.cursor()
    #sql = "select '%s@%s';" %(tar_user,tar_pass)
    sql = "%s" % v_sql
    n = cursor.execute(sql)
    row = cursor.fetchall()
    print row
    cursor.close()
    conn.close()
# mycat_dml(3306,'10.32.7.139','ecejmaster0','select now();')

