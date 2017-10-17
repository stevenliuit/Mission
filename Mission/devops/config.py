#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import ConfigParser

env = ConfigParser.ConfigParser()

MY_BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) + '/config/'
#print MY_BASE_DIR

if os.path.isfile(os.path.join(MY_BASE_DIR, 'env.conf')):
    env.read(os.path.join(MY_BASE_DIR, 'env.conf'))
else:
    env.read(os.path.join(MY_BASE_DIR, 'dev.env.conf'))

DEFAULT_USERNAME = env.get('user', 'username')

SSH_PRIVATE_KEY_PATH = env.get('user', 'ssh_key_path')
