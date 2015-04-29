# script to download all the mozart sonatas

import requests
import time

urlstem = 'http://kern.ccarh.org/cgi-bin/ksdata'
urlfolder = '?l=users/craig/classical/mozart/piano/sonata'
urlfile = '&file=sonata'

urltail = '.krn&f=xml'
#example
#
#http://kern.ccarh.org/cgi-bin/ksdata?l=users/craig/classical/mozart/piano/sonata
#      &file=sonata01-1.krn&f=xml

three_mvt_sonatas = ['01','02','03','04','05','07','08','09',
										 '10','12','13','14','15','16','17']


for s in three_mvt_sonatas:
	print("Downloading Mozart Sonata No" + s)
	for i in range(1,4):
		url = urlstem + urlfolder +urlfile + s + ('-%d' % i) +  urltail
		filename = 'mXML/mozart_pno_sonata' + s + ('-%d' % i) + '.xml' 
	 
		r = requests.get(url)
		f = open(filename,'w')
		f.write(r.text)
		f.close()
	print('Done!')
	time.sleep(2)

# sonatas 6 and 11 are in 3 movements, but have theme-and-variations which
# are split by variation.
#
# sonata #6 is: 1,2,3a-m
# sonata #11 is: 1a-g,2,3

mozart_sonata_numbers = ['06-1','06-2','06-3a','06-3b','06-3c','06-3d','06-3e',
						'06-3f','06-3g','06-3h','06-3i','06-3j','06-3k','06-3l',
						'06-3m','11-1a','11-1b','11-1c','11-1d','11-1e','11-1f','11-1g',
						'11-2','11-3']

for s in mozart_sonata_numbers:
	print("Downloading Mozart Sonata No" + s)

	url = urlstem + urlfolder +urlfile + s +  urltail
	filename = 'mXML/mozart_pno_sonata' + s + '.xml' 
 
	r = requests.get(url)
	f = open(filename,'w')
	f.write(r.text)
	f.close()
	print('Done!')
	time.sleep(2)



	