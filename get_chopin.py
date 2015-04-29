# script to download the Chopin Preludes

import requests
for i in range(24):
	p = 1 + i

	# set the URL for the file to download and the filename
	filename = 'mXML/chopin28-'  
	url = 'http://kern.ccarh.org/cgi-bin/ksdata?l=users/craig/classical/chopin/prelude&file=prelude28-'
	
	if p < 10:
		url += '0%d.krn&f=xml' % p
		filename += '0%d.xml' % p
	else:
		url += '%d.krn&f=xml' % p
		filename += '%d.xml' % p

	r = requests.get(url)
	f = open(filename,'w')
	f.write(r.text)
	f.close()
	print("Downloaded Chopin Op 28 No. %d" % p)