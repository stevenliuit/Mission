#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#author:F.W

from .models import Server
from devops.settings import USERNAME,SSH_KEY
from apps.assets_del.asset_api import get_asset_data


def update_assets_info():
    server_obj = Server.objects.all()
    server_list_info =[]
    for host in server_obj:
        info = dict()
        info["hostname"] = host.hostname
        info["ip"] = host.manage_ip
        info["port"] = host.port
        info['username'] = USERNAME
        info['ssh_key'] = SSH_KEY
        server_list_info.append(info)
    print server_obj
    get_asset_data(server_list_info)