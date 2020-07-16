#!/usr/bin/python
"""
developer skype: alec_host
"""
import os
import shutil
from configs.bulk_promo_settings import path_param

def _archive_csv_file():

	files = os.listdir(path_param['src_dir'])
	files.sort()
	
	for file in files:
		if file.endswith(".csv"):
			src = path_param['src_dir']+file
			dst = path_param['dst_dir']+file
			
			if(os.path.exists(src)):
				try:
					os.rename(src,src)
					shutil.move(src,dst)
				except OSError, e:
					print('Not allowed')