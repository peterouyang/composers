# script to download Chopin Mazurkas
# from kern website http://kern.ccarh.org/

import requests
import time

urlstem = 'http://kern.ccarh.org/cgi-bin/ksdata'
urlfolder = '?l=users/craig/classical/chopin/mazurka'
urlfile = '&file=mazurka'

urltail = '.krn&f=xml'

filenumbers = ['06-1','06-2','06-3','06-4','07-1','07-2','07-3','07-4','07-5',
               '17-1','17-2','17-3','17-4','24-1','24-2','24-3','24-4','30-1','30-2',
               '30-3','30-4','33-1','33-2','33-3','33-4','41-1','41-2','41-3','41-4',
               '50-1','50-2','50-3','56-1','56-2','56-3','59-1','59-2','59-3',
               '63-1','63-2','63-3','67-1','67-2','67-3','67-4','68-1','68-2',
               '68-3','68-4']

for opus in filenumbers:
  url = urlstem + urlfolder +urlfile + opus + urltail
  filename = 'mXML/chopin' + opus + '.xml'
  print("Loading Op" + opus)
  r = requests.get(url)
  f = open(filename,'w')
  f.write(r.text)
  f.close()
  print('Done!')
  time.sleep(2)

