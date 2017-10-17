#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
#author:F.W
from devops.settings import LOG_DIR

import logging.handlers,logging,time

#实例化handlers

filename = time.time()
LOG_FILE = LOG_DIR+"/pushCode.txt"

handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes = 100*1024*1024, backupCount = 5) # 实例化handler
# create logger
logger = logging.getLogger(__name__)
# create formatter
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
# add formatter to ch
handler.setFormatter(formatter)
# add handler to logger
logger.addHandler(handler)  # 为logger添加handler
logger.setLevel(logging.INFO)


