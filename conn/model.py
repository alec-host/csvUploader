#!/usr/bin/python
"""
developer skype: alec_host
"""
from db_helper import _insert_msisdn_db

def _import_msisdn_sys(msisdn,conn=None):
	db_response = None
	if(msisdn[0] is not None and str(msisdn[0]).isdigit()):
		"""
		-.write msisdn to db.
		"""
		db_response = _insert_msisdn_db(msisdn[0],conn)
		
	return db_response