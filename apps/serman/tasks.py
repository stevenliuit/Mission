# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task
import os
from apps.models import *


@shared_task
def add(x, y):
    print x + y
    return x + y


@shared_task
def pt_query_digest():
    log_name_list = os.listdir('/data/slowlog')
    for log_name in log_name_list:
        ip_name = log_name.split('_')[0]
        print ip_name
        host_name = eserver.objects.get(host=ip_name).hostname
        print host_name

        log_name = str(log_name)
        pt_command = '''
                pt-query-digest --user=dbaadmin --password=dba123qwone --history  h=10.4.89.185,D=devops,t=global_query_review_history --filter=" \$event->{Bytes} = length(\$event->{arg}) and \$event->{hostname}=\\"%s\\"" --no-report   --create-history-table  /data/slowlog/%s ''' % (host_name, log_name)

        os.system(pt_command)


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
