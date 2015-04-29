# script to download bach 2-part inventions

import requests
import time

urlstem = 'http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/inventions&file=inven'
inv_numbers = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15']
urltail = '.krn&f=xml'

for s in inv_numbers:
	url = urlstem + s + urltail

	filename = 'mXML/bach_invention_' + s + '.xml' 
	 
	r = requests.get(url)
	f = open(filename,'w')
	f.write(r.text)
	f.close()
	print('Done!')
	time.sleep(2)

