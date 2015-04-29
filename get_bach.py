# #This is a script to download all the XML files for Bach's Well Tempered Clavier

import requests

# WTC, Book 1, Preludes
for i in range(24):

	# set the URL for the file to download
	url = 'http://kern.ccarh.org/cgi-bin/ksdata?l=musedata/bach/keyboard/wtc-1&file=wtc1p'
	if i < 9:
		url += '0%d' % (i+1)
	else:
		url += '%d' % (i+1)
	url += '.krn&f=xml'

	bwvnum = 846 + i
	filename = 'mXML/bwv' + '%d.xml' % bwvnum 

	r = requests.get(url)
	f = open(filename,'w')
	f.write(r.text)
	f.close()
	print("Downloaded BWV%d" % bwvnum)

# WTC, Book 2, Preludes
for i in range(24):

	# set the URL for the file to download
	url = 'http://kern.ccarh.org/cgi-bin/ksdata?l=musedata/bach/keyboard/wtc-2&file=wtc2p'
	if i < 9:
		url += '0%d' % (i+1)
	else:
		url += '%d' % (i+1)
	url += '.krn&f=xml'

	bwvnum = 870 + i
	filename = 'mXML/bwv' + '%d.xml' % bwvnum 

	r = requests.get(url)
	f = open(filename,'w')
	f.write(r.text)
	f.close()
	print("Downloaded BWV%d" % bwvnum)

# WTC, Book 1, Fugues
for i in range(24):

	# set the URL for the file to download
	url = 'http://kern.ccarh.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-1&file=wtc1f'
	if i < 9:
		url += '0%d' % (i+1)
	else:
		url += '%d' % (i+1)
	url += '.krn&f=xml'

	bwvnum = 846 + i
	filename = 'mXML/bwv' + '%da.xml' % bwvnum 

	r = requests.get(url)
	f = open(filename,'w')
	f.write(r.text)
	f.close()
	print("Downloaded BWV%da" % bwvnum)


# WTC, Book 2, Fugues
for i in range(24):

	# set the URL for the file to download
	url = 'http://kern.ccarh.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-2&file=wtc2f'
	if i < 9:
		url += '0%d' % (i+1)
	else:
		url += '%d' % (i+1)
	url += '.krn&f=xml'

	bwvnum = 870 + i
	filename = 'mXML/bwv' + '%da.xml' % bwvnum 

	r = requests.get(url)
	f = open(filename,'w')
	f.write(r.text)
	f.close()
	print("Downloaded BWV%da" % bwvnum)
