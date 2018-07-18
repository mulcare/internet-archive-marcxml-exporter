#!/usr/bin/env python

import internetarchive
import time

collection = input('Enter Internet Archive collection ID: ')
list = internetarchive.search_items('collection:' + collection)

for book in list:
	itemid = book['identifier']
	item = internetarchive.get_item(itemid)
	marc = item.get_file(itemid + '_marc.xml')
	try:
		marc.download()
	except Exception as e:
		error_log.write('Could not download ' + itemid + ' because of error: %s\n' % e)
		print('There was an error; writing to log.')
	else:
		print('Downloading'  + itemid + '...')
		time.sleep(3)