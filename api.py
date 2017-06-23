# -*- coding: utf-8 -*-
from apps.models import Admin
from apps.models import OsUser, OsAuth
from apps.models import TermLog
from Crypto.Cipher import AES
from devops.settings import LOG_DIR,LOG_LEVEL
import crypt
import pyte
import pwd
import os
import subprocess
import random
from binascii import b2a_hex, a2b_hex
import hashlib
import logging
import ConfigParser
import time
import re
import datetime
import uuid
import zipfile
import json
from devops.config import DEFAULT_USERNAME



def get_object(model, **kwargs):
    """
    use this function for query
    使用改封装函数查询数据库
    """
    for value in kwargs.values():
        if not value:
            return None

    the_object = model.objects.filter(**kwargs)
    if len(the_object) == 1:
        the_object = the_object[0]
    else:
        the_object = None
    return the_object

def get_osuser(admin):
    if not isinstance(admin, Admin):
        return None

    auth_list = OsAuth.objects.filter(admin=admin).all()
    os_user_set = set()
    if auth_list:
        for auth in auth_list:
            os_user_set.add(auth.os_user)
        return os_user_set
    return None

def get_server_info(server):
    """
    获取资产的相关管理账号端口等信息
    """
    #default = get_object(Setting, name='default')
    info = {'hostname': server.hostname, 'ip': server.manage_ip}

    info['username'] = DEFAULT_USERNAME
    info['password'] = ''
    try:
        info['port'] = int(server.port)
    except TypeError:
        info['port'] = 22

    return info

def get_user_key(user):

    if isinstance(user, OsUser):
        return os.path.join(user.ssh_key, user.username)
    else:
        return None

def get_user_perm(admin):

    auth_list = OsAuth.objects.filter(admin=admin).all()
    perm_info = dict()

    asset_dict = {}
    group_dict = {}
    assets = []
    for auth in auth_list:
        for server in auth.get_auth_servers:
            server.osuser = auth.os_user
            assets.append(server)

    for asset in assets:

        asset_dict[asset.hostname + '_' + asset.osuser.username] = asset
    perm_info['asset'] = asset_dict

    asset_groups = set()
    for auth in auth_list:
        asset_groups.update(auth.osauth_asset_group.all())

    for asset_group in asset_groups:
        group_dict[asset_group.group_name] = dict(asset = [server for server in asset_group.servers]) #此处存疑，待修改
    perm_info['asset_group'] = group_dict

    return perm_info

def bash(cmd):
    """
    run a bash shell command
    执行bash命令
    """
    return subprocess.call(cmd, shell=True)

def chown(path, user, group=''):
    if not group:
        group = user
    try:
        uid = pwd.getpwnam(user).pw_uid
        gid = pwd.getpwnam(group).pw_gid
        os.chown(path, uid, gid)
    except KeyError:
        pass

def mkdir(dir_name, username='', mode=755):
    """
    insure the dir exist and mode ok
    目录存在，如果不存在就建立，并且权限正确
    """
    cmd = '[ ! -d %s ] && mkdir -p %s && chmod %s %s' % (dir_name, dir_name, mode, dir_name)
    bash(cmd)
    if username:
        chown(dir_name, username)


class PyCrypt(object):
    """
    This class used to encrypt and decrypt password.
    加密类
    """

    def __init__(self, key):
        self.key = key
        self.mode = AES.MODE_CBC

    @staticmethod
    def gen_rand_pass(length=16, especial=False):
        """
        random password
        随机生成密码
        """
        salt_key = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
        symbol = '!@$%^&*()_'
        salt_list = []
        if especial:
            for i in range(length - 4):
                salt_list.append(random.choice(salt_key))
            for i in range(4):
                salt_list.append(random.choice(symbol))
        else:
            for i in range(length):
                salt_list.append(random.choice(salt_key))
        salt = ''.join(salt_list)
        return salt

    @staticmethod
    def md5_crypt(string):
        """
        md5 encrypt method
        md5非对称加密方法
        """
        return hashlib.new("md5", string).hexdigest()

    @staticmethod
    def gen_sha512(salt, password):
        """
        generate sha512 format password
        生成sha512加密密码
        """
        return crypt.crypt(password, '$6$%s$' % salt)

    def encrypt(self, passwd=None, length=32):
        """
        encrypt gen password
        对称加密之加密生成密码
        """
        if not passwd:
            passwd = self.gen_rand_pass()

        cryptor = AES.new(self.key, self.mode, b'8122ca7d906ad5e1')
        try:
            count = len(passwd)
        except TypeError:
            raise ServerError('Encrypt password error, TYpe error.')

        add = (length - (count % length))
        passwd += ('\0' * add)
        cipher_text = cryptor.encrypt(passwd)
        return b2a_hex(cipher_text)

    def decrypt(self, text):
        """
        decrypt pass base the same key
        对称加密之解密，同一个加密随机数
        """
        cryptor = AES.new(self.key, self.mode, b'8122ca7d906ad5e1')
        try:
            plain_text = cryptor.decrypt(a2b_hex(text))
        except TypeError:
            raise ServerError('Decrypt password error, TYpe error.')
        return plain_text.rstrip('\0')

class ServerError(Exception):
    """
    self define exception
    自定义异常
    """
    pass

def set_log(level, filename='devops.log'):
    """
    return a log file object
    根据提示设置log打印
    """
    log_file = os.path.join(LOG_DIR, filename)
    if not os.path.isfile(log_file):
        os.mknod(log_file)
        os.chmod(log_file, 0777)
    log_level_total = {'debug': logging.DEBUG, 'info': logging.INFO, 'warning': logging.WARN, 'error': logging.ERROR,
                       'critical': logging.CRITICAL}
    logger_f = logging.getLogger('devops')
    logger_f.setLevel(logging.DEBUG)
    fh = logging.FileHandler(log_file)
    fh.setLevel(log_level_total.get(level, logging.DEBUG))
    formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger_f.addHandler(fh)
    return logger_f

CRYPTOR = PyCrypt('941enj9neshd1wes')
logger = set_log(LOG_LEVEL)

class TermLogRecorder(object):
    """
    TermLogRecorder
    ---
    Author: liuzheng <liuzheng712@gmail>
    This class is use for record the terminal output log.
        self.commands is pure commands list, it will have empty item '' because in vi/vim model , I made it log noting.
        self.CMD is the command with timestamp, like this {'1458723794.88': u'ls', '1458723799.82': u'tree'}.
        self.log is the all output with delta time log.
        self.vim_pattern is the regexp for check vi/vim/fg model.
    Usage:
        recorder = TermLogRecorder(user=UserObject) # or recorder = TermLogRecorder(uid=UserID)
        recoder.write(messages)
        recoder.save() # save all log into database
        # The following methods all have `user`,`uid`,args. Same as __init__
        list = recoder.list() # will give a object about this user's all log info
        recoder.load_full_log(filemane) # will get full log
        recoder.load_history(filename) # will only get the command history list
        recoder.share_to(filename,user=UserObject) # or recoder.share_to(filename,uid=UserID). will share this commands to someone
        recoder.unshare_to(filename,user=UserObject) # or recoder.unshare_to(filename,uid=UserID). will unshare this commands to someone
        recoder.setid(id) # registered this term with an id, for monitor
    """
    loglist = dict()

    def __init__(self, user=None, uid=None):
        self.log = {}
        self.id = 0
        if isinstance(user, Admin):
            self.user = user
        elif uid:
            self.user = Admin.objects.get(id=uid)
        else:
            self.user = None
        self.recoderStartTime = time.time()
        self.__init_screen_stream()
        self.recoder = False
        self.commands = []
        self._lists = None
        self.file = None
        self.filename = None
        self._data = None
        self.vim_pattern = re.compile(r'\W?vi[m]?\s.* | \W?fg\s.*', re.X)
        self._in_vim = False
        self.CMD = {}

    def __init_screen_stream(self):
        """
        Initializing the virtual screen and the character stream
        """
        self._stream = pyte.ByteStream()
        self._screen = pyte.Screen(100, 35)
        self._stream.attach(self._screen)

    def _command(self):
        for i in self._screen.display:
            if i.strip().__len__() > 0:
                self.commands.append(i.strip())
                if not i.strip() == '':
                    self.CMD[str(time.time())] = self.commands[-1]
        self._screen.reset()

    def setid(self, id):
        self.id = id
        TermLogRecorder.loglist[str(id)] = [self]

    def write(self, msg):
        """
        if self.recoder and (not self._in_vim):
            if self.commands.__len__() == 0:
                self._stream.feed(msg)
            elif not self.vim_pattern.search(self.commands[-1]):
                self._stream.feed(msg)
            else:
                self._in_vim = True
                self._command()
        else:
            if self._in_vim:
                if re.compile(r'\[\?1049', re.X).search(msg.decode('utf-8', 'replace')):
                    self._in_vim = False
                    self.commands.append('')
                self._screen.reset()
            else:
                self._command()
        """
        try:
            self.write_message(msg)
        except:
            pass
        # print "<<<<<<<<<<<<<<<<"
        # print self.commands
        # print self.CMD
        # print ">>>>>>>>>>>>>>>>"
        self.log[str(time.time() - self.recoderStartTime)] = msg.decode('utf-8', 'replace')

    def save(self, path=LOG_DIR):
        date = datetime.datetime.now().strftime('%Y%m%d')
        filename = str(uuid.uuid4())
        self.filename = filename
        filepath = os.path.join(path, 'tty', date, filename + '.zip')
        if not os.path.isdir(os.path.join(path, 'tty', date)):
            mkdir(os.path.join(path, 'tty', date), mode=777)
        while os.path.isfile(filepath):
            filename = str(uuid.uuid4())
            filepath = os.path.join(path, 'tty', date, filename + '.zip')
        password = str(uuid.uuid4())
        #print type(password)
        try:
            zf = zipfile.ZipFile(filepath, 'w', zipfile.ZIP_DEFLATED)
            zf.setpassword(password)
            zf.writestr(filename, json.dumps(self.log))
            zf.close()
            record = TermLog.objects.create(logPath=filepath, logPWD=password, filename=filename,
                                            history=json.dumps(self.CMD), timestamp=int(self.recoderStartTime))
            if self.user:
                record.user.add(self.user)
        except:
            record = TermLog.objects.create(logPath='locale', logPWD=password, log=json.dumps(self.log),
                                            filename=filename, history=json.dumps(self.CMD),
                                            timestamp=int(self.recoderStartTime))

        try:
            del TermLogRecorder.loglist[str(self.id)]
        except KeyError:
            pass

    def list(self, user=None, uid=None):
        tmp = []
        if isinstance(user, Admin):
            user = user

        else:
            user = self.user
        if user:
            self._lists = TermLog.objects.filter(user=user.id)
            for i in self._lists.all():
                tmp.append(
                    {'filename': i.filename, 'locale': i.logPath == 'locale', 'nick': i.nick, 'timestamp': i.timestamp,
                     'date': i.datetimestamp})
        return tmp

    def load_full_log(self, filename, user=None, uid=None):
        if isinstance(user, Admin):
            user = user
        elif uid:
            user = Admin.objects.get(id=uid)
        else:
            user = self.user
        if user:
            if self._lists:
                self.file = self._lists.get(filename=filename)
            else:
                self.file = TermLog.objects.get(filename=filename)
            if self.file.logPath == 'locale':
                return self.file.log
            else:
                try:
                    zf = zipfile.ZipFile(self.file.logPath, 'r', zipfile.ZIP_DEFLATED)
                    zf.setpassword(self.file.logPWD)
                    self._data = zf.read(zf.namelist()[0])
                    return self._data
                except KeyError:
                    return 'ERROR: Did not find %s file' % filename
        return 'ERROR User(None)'

    def load_history(self, filename, user=None, uid=None):
        if isinstance(user, Admin):
            user = user
        elif uid:
            user = Admin.objects.get(id=uid)
        else:
            user = self.user
        if user:
            if self._lists:
                self.file = self._lists.get(filename=filename)
            else:
                self.file = TermLog.objects.get(filename=filename)
            return self.file.history
        return 'ERROR User(None)'

    def share_to(self, filename, user=None, uid=None):
        if isinstance(user, Admin):
            user = user
        elif uid:
            user = Admin.objects.get(id=uid)
        else:
            pass
        if user:
            TermLog.objects.get(filename=filename).user.add(user)
            return True
        return False

    def unshare_to(self, filename, user=None, uid=None):
        if isinstance(user, Admin):
            user = user
        elif uid:
            user = Admin.objects.get(id=uid)
        else:
            pass
        if user:
            TermLog.objects.get(filename=filename).user.remove(user)
            return True
        return False
