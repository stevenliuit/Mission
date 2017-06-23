#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#author:F.W
from devops.settings import REDIS_HOST, REDIS_PORT,QUEUE_KEY

import sys,os,redis,time,django,platform

os.environ['DJANGO_SETTINGS_MODULE'] = 'devops.settings'

setup = django.setup()

from apps.project_bak.release_api import ProjectTask
from common.utils.daemonize import Daemonize

reload(sys)

sys.setdefaultencoding('utf8')


pid = "pid/ts.pid"

class Task(object):

    def __init__(self):
        self.rcon = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT)

    def listen_task(self):
        task = self.rcon.brpop(QUEUE_KEY)

        if task:
            source = task[1]
            data = eval(source)
            ps_obj = ProjectTask(data['hosts'])
            ps_obj.push_code(repo_name=data.get('repo_name'),repo_url=data.get('repo_url'),r_id=data.get("id"),
                             tag_name=data.get('tag_name'),branch=data.get('branch'),type_env=data.get('type_env'),
                             status=data.get('status')
                             )



def run():
    print ('listen push task')
    a = Task()
    while True:
        try:
            a.listen_task()
        except redis.exceptions.ConnectionError as e:
            time.sleep(1)
            print (e)


if __name__ == '__main__':

    path = os.getcwd()
    daemon = Daemonize(app="ts", pid=pid, action=run,chdir=path)
    daemon.start()









