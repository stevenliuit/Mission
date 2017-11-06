# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import MySQLdb
from django.db import models
from devops.settings import BASE_DIR
import time


class Module(models.Model):
    STATUS_OPEN = 1
    STATUS_CLOSE = 2
    STATUS = {
        STATUS_OPEN: '启用',
        STATUS_CLOSE: '禁用',
    }

    id = models.SmallIntegerField(primary_key=True)
    module_name = models.CharField(max_length=10, verbose_name=u'模块名')
    status = models.IntegerField(verbose_name=u'状态')
    list_order = models.IntegerField(verbose_name=u'排序')

    class Meta:
        managed = False
        db_table = 'module'


class PrivilegeGroup(models.Model):
    STATUS_OPEN = 1
    STATUS_CLOSE = 2
    STATUS = {
        STATUS_OPEN: '启用',
        STATUS_CLOSE: '禁用',
    }

    id = models.SmallIntegerField(primary_key=True)
    group_name = models.CharField(max_length=20, verbose_name=u'权限组名')
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'privilege_group'


class Privilege(models.Model):
    STATUS_OPEN = 1
    STATUS_CLOSE = 2
    STATUS = {
        STATUS_OPEN: '启用',
        STATUS_CLOSE: '禁用',
    }

    privilege_group = models.ForeignKey(PrivilegeGroup, on_delete=models.CASCADE, verbose_name=u'权限组')
    privilege_name = models.CharField(max_length=20, unique=True, verbose_name=u'权限名称')
    view_func = models.CharField(max_length=100, verbose_name=u'请求路径')
    request_path = models.CharField(max_length=50, verbose_name=u'VIEW名称')
    status = models.IntegerField(verbose_name=u'状态')

    class Meta:
        managed = False
        db_table = 'privilege'
        unique_together = (('request_path', 'view_func'),)


class Role(models.Model):
    STATUS_OPEN = 1
    STATUS_CLOSE = 2
    STATUS = {
        STATUS_OPEN: '启用',
        STATUS_CLOSE: '禁用',
    }

    ROLE_SUPPER = 1

    role_name = models.CharField(max_length=20, verbose_name=u'角色名称')
    description = models.CharField(max_length=200, verbose_name=u'描述')
    status = models.IntegerField(verbose_name=u'状态')

    privileges = models.ManyToManyField(
        Privilege,
        through='RolePrivilege',
        through_fields=('role', 'privilege'),
    )

    class Meta:
        managed = False
        db_table = 'role'


class RolePrivilege(models.Model):

    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    privilege = models.ForeignKey(Privilege, on_delete=models.CASCADE)

    class Meta:
        auto_created = True
        managed = False
        db_table = 'role_privilege'


class RolePrivilegeGroup(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    privilege_group = models.ForeignKey(PrivilegeGroup, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'role_privilege_group'


class Menu(models.Model):
    STATUS_OPEN = 1
    STATUS_CLOSE = 2
    STATUS = {
        STATUS_OPEN: '启用',
        STATUS_CLOSE: '禁用',
    }

    module = models.ForeignKey(Module, on_delete=models.CASCADE, db_column='module_id', verbose_name=u'模块')
    privilege = models.ForeignKey(Privilege, on_delete=models.CASCADE, db_column='privilege_id', verbose_name=u'权限', default=-1,blank=True, null=True)
    menu_name = models.CharField(max_length=10, verbose_name=u'菜单名称')
    target = models.CharField(max_length=10, verbose_name=u'跳转目标')
    target_url = models.CharField(max_length=200, blank=True, null=True, verbose_name=u'跳转URL')
    status = models.IntegerField(verbose_name=u'状态')

    class Meta:
        managed = False
        db_table = 'menu'


SERVER_TYPE = (
    (1, u'物理机'),
    (2, u'虚拟机'),
    (3, u'云主机')
)

STATUS = (
    (1, u'使用'),
    (2, u'闲置'),
    (3, u'废弃'),
    (4, u'维修')
)

ASSET_STATUS = (
    (1, u'启用'),
    (2, u'停用')
)




class Admin(models.Model):
    STATUS_OPEN = 1
    STATUS_CLOSE = 2
    STATUS = {
        STATUS_OPEN: '启用',
        STATUS_CLOSE: '禁用',
    }
    IS_SUPPER = 1

    name = models.CharField(unique=True, max_length=20, verbose_name=u'账号')
    uuid = models.CharField(max_length=32, verbose_name=u'唯一ID')
    pwd = models.CharField(max_length=32, verbose_name=u'秘密')
    user_name = models.CharField(max_length=10, blank=True, null=True, verbose_name=u'姓名')
    tel = models.CharField(unique=True, max_length=11, verbose_name=u'电话号')
    email = models.EmailField(unique=True, max_length=50, verbose_name=u'邮箱')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, db_column='role_id', verbose_name=u'角色')
    status = models.IntegerField(verbose_name=u'状态')
    last_login_ip = models.CharField(max_length=15, blank=True, null=True)
    last_login_time = models.DateTimeField(blank=True, null=True)
    is_super = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)

    # projects = models.ManyToManyField(
    #     Project,
    #     through='AdminProject',
    #     through_fields=('admin', 'project'),
    # )

    class Meta:
        managed = False
        db_table = 'admin'





class OperationLog(models.Model):
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    admin_name = models.CharField(max_length=20, blank=True, null=True)
    privilege = models.ForeignKey(Privilege, on_delete=models.CASCADE)
    request_method = models.CharField(max_length=10, default='POST')
    query_string = models.CharField(max_length=100, blank=True, null=True)
    change_data = models.CharField(max_length=500, blank=True, null=True)
    ip = models.CharField(max_length=15)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'operation_log'





class eproject(models.Model):
    pname = models.CharField(max_length=20, blank=True, verbose_name=u'业务组名')
    created_at = models.DateTimeField(auto_now_add=True)
    admin = models.ManyToManyField(
        Admin,
        through='eproject_admin',
        through_fields=('eproject', 'admin'),  # 字段

    )

    class Meta:
        managed = False
        db_table = 'eproject'

class eproject_admin(models.Model):
    eproject = models.ForeignKey(eproject, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin,on_delete=models.CASCADE)

    class Meta:
        auto_created = True
        managed = False
        db_table = 'eproject_admin'


class eserver(models.Model):
    eproject=models.ForeignKey(eproject,on_delete=models.CASCADE)
    hostname = models.CharField(max_length=100, verbose_name=u'主机名')
    host = models.CharField(max_length=100,  verbose_name=u'主机ip')
    dport = models.IntegerField(default=3306 ,verbose_name=u'数据库端口')
    hport = models.IntegerField(default=22, verbose_name=u'ssh端口')
    huser = models.CharField(max_length=100, verbose_name=u'ssh用户')
    hpassword = models.CharField(max_length=100,  verbose_name=u'ssh密码')
    descr= models.CharField(max_length=120,blank=True,  verbose_name=u'描述')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'eserver'


class eprivs(models.Model):
    dname = models.CharField(max_length=20, blank=True, verbose_name=u'username')
    dpass= models.CharField(max_length=100,  verbose_name=u'db密码')
    ptype=models.IntegerField(default=3306 ,verbose_name=u'权限类型')
    created_at = models.DateTimeField(auto_now_add=True)
    servers = models.ManyToManyField(
        eserver,
        through='eprivs_eserver',
        through_fields=('e_privs', 'e_server'),  # 字段

    )

    class Meta:
        managed = False
        db_table = 'eprivs'

class eprivs_eserver(models.Model):
    e_privs = models.ForeignKey(eprivs, on_delete=models.CASCADE)
    e_server = models.ForeignKey(eserver,on_delete=models.CASCADE)

    class Meta:
        auto_created = True
        managed = False
        db_table = 'eprivs_eserver'



class mycat_server(models.Model):
    dbname = models.CharField(max_length=50, blank=True, verbose_name=u'dbname')
    host = models.CharField(max_length=50, blank=True, verbose_name=u'host')

    class Meta:
        auto_created = True
        managed = False
        db_table = 'mycat_server'


class global_query_review_history(models.Model):
    hostname_max = models.CharField(max_length=100, blank=True, verbose_name=u'hostname')
    db_max= models.CharField(max_length=100,  verbose_name=u'dbname')
    checksum=models.BigIntegerField(verbose_name=u'hash checksum')
    sample = models.CharField(max_length=5000)
    ts_min = models.DateTimeField(auto_now_add=True)
    ts_max = models.DateTimeField(auto_now_add=True)
    ts_cnt = models.FloatField(verbose_name=u'hash checksum')
    Query_time_sum = models.FloatField(verbose_name=u'hash checksum')
    Query_time_min = models.FloatField(verbose_name=u'hash checksum')
    Query_time_max = models.FloatField(verbose_name=u'hash checksum')
    Query_time_pct_95 = models.FloatField(verbose_name=u'hash checksum')
    Query_time_stddev = models.FloatField(verbose_name=u'hash checksum')
    Query_time_median = models.FloatField(verbose_name=u'hash checksum')
    Lock_time_sum = models.FloatField(verbose_name=u'hash checksum')
    Lock_time_min = models.FloatField(verbose_name=u'hash checksum')
    Lock_time_max = models.FloatField(verbose_name=u'hash checksum')
    Lock_time_pct_95 = models.FloatField(verbose_name=u'hash checksum')
    Lock_time_stddev = models.FloatField(verbose_name=u'hash checksum')
    Lock_time_median = models.FloatField(verbose_name=u'hash checksum')

    class Meta:
        managed = False
        db_table = 'global_query_review_history'


class release(models.Model):
    releaser_id = models.IntegerField(verbose_name=u'申请用户id')
    eserver = models.ForeignKey(eserver)
    sql = models.TextField(blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    status = models.IntegerField(null=True, default=0)
    exec_time = models.DateTimeField(max_length=5000,null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'release'