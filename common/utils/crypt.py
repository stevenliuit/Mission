# -*- coding: utf-8 -*-

import base64

def jiami(str):
    s1 = base64.encodestring(str)
    return s1.strip('\n')

def jiemi(str):
    s2 = base64.decodestring(str)
    return s2

def md5(str):
    """
    MD5 加密函数
    """
    import hashlib
    m = hashlib.md5()
    m.update(str)

    return m.hexdigest()


def gen_rand_password(length=16, especial=False):
    """
    random password
    随机生成密码
    """
    import random

    salt_key = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
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


def gen_rand_number(length=16):
    return gen_rand_password(16).lower()


