# script to download Beethoven's piano sonatas
# There are 32 piano sonatas, with 2-4 movements.

import requests
import time

urlstem = 'http://kern.ccarh.org/cgi-bin/ksdata'
urlfolder = '?l=users/craig/classical/beethoven/piano/sonata'
urlfile = '&file=sonata'
urltail = '.krn&f=xml'


for i in range(1,33):
  for j in range(1,5):
    if i < 10:
      s= ('0%d-%d' % (i, j)) 
    else:
      s= ('%d-%d' % (i, j))     
    url = urlstem+urlfolder+urlfile+s+urltail
    try:
      filename = 'mXML/beethoven_pno_sonata' + s + '.xml' 
      print('downloading sonata' + s)
      r = requests.get(url)
      f = open(filename,'w')
      f.write(r.text)
      f.close()
    except:
      print('no file downloaded for sonata'+s)
    time.sleep(2)


#http://kern.humdrum.org/cgi-bin/ksdata
#?l=users/craig/classical/beethoven/piano/sonata&file=sonata01-1.krn&f=xml