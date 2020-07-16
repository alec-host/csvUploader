#!/usr/bin/python2
import os
import csv
import MySQLdb
import logging
import signal

from conn.model import _import_msisdn_sys
from conn.utility import _archive_csv_file
from conn.configs.bulk_promo_settings import path_param
from conn.db_helper import create_connection,close_connection,NoResultException

log = logging.getLogger()

"""
-.routine.
"""	
def importCsvContent():
	db = create_connection()
	target = str(path_param['src_dir']+path_param['csvfile'])
	try:
		while True:
			#if(myfile.is_file)
			if(os.path.isfile(target)):
				with open(target, 'rb') as f:
					csv_data = csv.reader(f)
					for row in csv_data:
						#-.routine call.
						_import_msisdn_sys(row,db)
				f.close()
				#r-.routine call.
				_archive_csv_file()
	except MySQLdb.Error, e:
		log.error(e)
	except Exception, e:
		log.error(e)
	finally:
		try:
			if(not db):
				exit(0)
			else:
				"""
				close MySQL connection.
				"""			
				close_connection(db)
		except MySQLdb.Error, e:
			log.error(e)
			
"""
-.main method.
"""	
if __name__ == '__main__':
	try:
		importCsvContent()
	except KeyboardInterrupt:
		exit();