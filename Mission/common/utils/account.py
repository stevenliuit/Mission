# -*- coding: utf-8 -*-
import os

from devops.settings import BASE_DIR, SSH_KEY_DIR, EMAIL_HOST_USER as MAIL_FROM, CURRENT_URL
from django.core.mail import send_mail


def bash(cmd):
    """
    run a bash shell command
    执行bash命令
    """
    try:
        import subprocess
    except:
        return None
    return subprocess.call(cmd, shell=True)


def gen_ssh_key(username, password='', key_dir='user', authorized_keys=True, home="/home", length=2048):
    """
    generate a user ssh key in a property dir
    生成一个用户ssh密钥对
    """
    import platform

    if platform.system() != 'Linux':
        return None

    from os import mkdir, chown

    key_dir = os.path.join(SSH_KEY_DIR, key_dir)

    private_key_file = os.path.join(key_dir, username+'.pem')
    if not os.path.exists(key_dir):
        mkdir(key_dir)
    if os.path.isfile(private_key_file):
        os.unlink(private_key_file)
    bash('echo -e  "y\n"|ssh-keygen -t rsa -f %s -b %s -P "%s"' % (private_key_file, length, password))

    if authorized_keys:
        auth_key_dir = os.path.join(home, username, '.ssh')
        if not os.path.exists(auth_key_dir):
            mkdir(auth_key_dir)

        authorized_key_file = os.path.join(auth_key_dir, 'authorized_keys')
        with open(private_key_file+'.pub') as pub_f:
            with open(authorized_key_file, 'w') as auth_f:
                auth_f.write(pub_f.read())
        os.chmod(authorized_key_file, 0600)
        # chown(authorized_key_file, username, username)
        try:
            import pwd
            uid = pwd.getpwnam(username).pw_uid
            gid = pwd.getpwnam(username).pw_gid
            os.chown(authorized_key_file, uid, gid)
        except:
            pass


def get_ssh_key(username, key_dir='user'):
    key_dir = os.path.join(SSH_KEY_DIR, key_dir)

    private_key_file = os.path.join(key_dir, username+'.pem')

    if not os.path.isfile(private_key_file):
        private_key_file = ''

    return private_key_file


def server_add_user(username, ssh_key_pwd=''):
    """
    add a system user in jumpserver
    在jumpserver服务器上添加一个用户
    """
    import platform

    # if platform.system() != 'Linux':
    #     return None


    bash("sudo useradd -s '%s' '%s'" % (os.path.join(BASE_DIR, 'bin/init.sh'), username))
    gen_ssh_key(username, ssh_key_pwd)


def user_add_mail(user):
    """
    add user send mail
    发送用户添加邮件
    """
    mail_title = u'恭喜,你的运维自动化账号添加成功'
    mail_msg = u"""
    Hi, %s
        您的用户名： %s
        您的角色： %s
    """ % (user.user_name, user.name,user.role.role_name)
    send_mail(mail_title, mail_msg, MAIL_FROM, [user.email], fail_silently=False)


def server_del_user(username):
    """
    delete a user from jumpserver linux system
    删除系统上的某用户
    """
    bash('userdel -r -f %s' % username)
    bash('rm -f %s/%s_*.pem' % (os.path.join(SSH_KEY_DIR, 'user'), username))
    bash('rm -f %s/%s.pem*' % (os.path.join(SSH_KEY_DIR, 'user'), username))


def is_authenticated(request):
    from apps.models import Admin
    try:
        current_admin_id = request.session['current_admin_id']
        current_role_id = request.session['current_role_id']
        admin = Admin.objects.get(id=current_admin_id, role_id=current_role_id)
        if not admin:
            del request.session['current_admin_id']
            del request.session['current_role_id']

            return False
    except:
        request.session.flush()
        return False

    return True


def get_admin_privileges(admin_id):
    from apps.models import Admin, Role, Privilege

    try:
        admin_id = int(admin_id)
        admin = Admin.objects.get(id=admin_id)
        if admin.role_id == Role.ROLE_SUPPER:
            privileges = Privilege.objects.all()
        else:
            privileges = admin.role.privileges.all()
    except:
        return None

    return privileges


