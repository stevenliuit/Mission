#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
from common.utils.redis_api import *
from devops.settings import REDIS_HOST, REDIS_PORT
import redis

r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)


class Locks:
    """
    发布锁锁
    """

    def __init__(self, name):
        self.name = name

    def set_lock(self,value=1,expire=None):
        if expire:
            r.set(self.name,value=value,expire=expire)
        else:
            return r.set(self.name, value=value)

    def get_lock(self):
        r.get(self.name)

    def del_lock(self):
        r.delete(self.name)
