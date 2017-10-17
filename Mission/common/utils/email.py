# -*- coding: utf-8 -*-

from devops.settings import BASE_DIR, SSH_KEY_DIR, EMAIL_HOST_USER as MAIL_FROM, CURRENT_URL
from django.core.mail import send_mail


def user_add_mail(user, **kwargs):
    """
    add user send mail
    发送用户添加邮件
    """
    mail_title = u'恭喜,你的用户 %s 添加成功 Devops' % user.name
    down_url = '%s/down_key/?uuid=%s' %(CURRENT_URL, user.uuid)
    mail_msg = u"""
    Hi, %s
        您的用户名： %s
        您的权限： %s
        您的web登录密码： %s
        您的ssh密钥文件密码： %s
        密钥下载地址： %s
        说明： 请登陆跳板机后台下载密钥, 然后使用密钥登陆跳板机！
    """ % (user.name, user.name, user.role.role_name, kwargs.get('password'), kwargs.get('ssh_key_pwd'), down_url)
    send_mail(mail_title, mail_msg, MAIL_FROM, [user.email], fail_silently=False)


def fbmail(a,b,c,d):
    mail_title = u'项目%s' % a
    mail_msg = u"""
    Hi, %s
        项目： %s
        状态：%s!
    """ % (b,a,d)
    send_mail(mail_title, mail_msg, MAIL_FROM, [c], fail_silently=False)


def deploy_project_mail(title, **kwargs):
    """
    发送项目部署状态邮件
    """
    mail_title = u'%s' % title
    mail_msg = u"""
    Hi,%s
        项目 ： %s
        状态 ： %s
        版本 ： %s
        备注 ： %s

    """ % (kwargs.get('username'),kwargs.get('project_name'),kwargs.get('status'),
           kwargs.get('version'),kwargs.get('error'))
    send_mail(mail_title,message=mail_msg,from_email=MAIL_FROM,recipient_list=kwargs.get('to_mail'),fail_silently=False)


