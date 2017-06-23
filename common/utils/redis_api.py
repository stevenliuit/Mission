#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

from devops.settings import REDIS_HOST, REDIS_PORT,QUEUE_KEY
import redis

r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)


def put_set(k_name,value,expire=None):

    if expire:
        r.set(k_name, value)
        return r.expire(k_name, expire)
    else:
        return r.set(k_name, value)


def get_set(k_name):
    """
    """
    return r.get(k_name)


def del_set(k_name):
    "  "
    return r.delete(k_name)


def push_task(data,key=QUEUE_KEY):
    if isinstance(data,dict):
        return r.lpush(key,data)
    else:
        return None



