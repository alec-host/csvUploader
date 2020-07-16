#!/usr/bin/python

import os
import sys
import logging
import ConfigParser

current_dir = os.path.join("C:/", "Python27/workspace")
CONFIG_FILE = current_dir + '/betvantage/conn/configs/bulk_promo.conf'

print(CONFIG_FILE)

config = ConfigParser.ConfigParser()
config.read(CONFIG_FILE)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("bulk_promo")
logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)
hdlr = logging.FileHandler(config.get("logger", "log_file"))
hdlr = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)

host   = config.get("mysql", "host")
port   = config.get("mysql", "port")
user   = config.get("mysql", "user")
passwd = config.get("mysql", "password")
db     = config.get("mysql", "database")
connection_timeout = config.get("mysql", "connection_timeout")
mysql_params = {'host':host, 'port':port, 'user':user, 'passwd':passwd, 'db':db, 'connection_timeout':connection_timeout}

src_dir = config.get("path", "src_dir")
dst_dir = config.get("path", "dst_dir")
csvfile = config.get("path", "csvfile")
path_param = {'src_dir':src_dir, 'dst_dir':dst_dir, 'csvfile': csvfile}