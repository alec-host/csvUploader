#!/usr/bin/python
"""
developer skype: alec_host
"""
import os
import sys
import time
import signal
import json
import ast
import eventlet
import logging
import MySQLdb
import MySQLdb.cursors

from datetime import datetime
from configs.bulk_promo_settings import logger,mysql_params
from db_conn import DB,NoResultException,NoServiceIDException

eventlet.monkey_patch()

db = DB()
			
"""
-=================================================
-.mark load as queued.
-=================================================	
"""	
def _insert_msisdn_db(msisdn,conn):
	jsString = None
	idateNow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	
	try:
		sql = """
			  INSERT
			  INTO
			 `tbl_subscription`
			  (`msisdn`,`date_created`)
			  VALUES
			  ('%s','%s')
			  ON
			  DUPLICATE KEY 
			  UPDATE 
			 `date_modified` = '%s'
			  """ % (msisdn,idateNow,idateNow)
			  
		print(msisdn + " uploaded to db ...")
		
		params = ()

		db.execute_query(conn,sql,params)
		
		jsString = {"ERROR":"0","RESULT":"SUCCESS","MESSAGE":"Insert complete"}
		
		conn.commit()
	except Exception,e:
		logger.error(e)
		raise
	
	return jsString
	
"""
-========================================================================================================================================================================================================

-========================================================================================================================================================================================================
"""
			
"""
#-.db routine connection.
"""
def create_connection(): 
	try:
		connection = MySQLdb.connect(host=mysql_params['host'],\
					 user=mysql_params['user'], passwd=mysql_params['passwd'],\
					 db=mysql_params['db'], cursorclass=MySQLdb.cursors.DictCursor)
	except(MySQLdb.Error, e):
		logger.error(e)
		raise
	return connection
"""	
#-.db close connection.
"""
def close_connection(connection):
	try:
		connection.close()
	except(MySQLdb.Error, e):
		logger.error(e)
		raise
