import music21
import scoreparser as sp
import pickle


counter = 1
for i in range(1,33):
	for j in range(1,5):
		if i < 10:
			s= ('0%d-%d' % (i, j)) 
		else:
			s= ('%d-%d' % (i, j))     
		try:
			filename = 'mXML/beethoven_pno_sonata' + s + '.xml' 
			print('processing sonata' + s)
			stream = music21.converter.parse(filename)
			notes = sp.get_note_list(stream)
			X = sp.make_pitch_range_rhythm_features(notes,stream)
			Xfile = open('Beethoven_%d_X' % counter,'wb')
			pickle.dump(X,Xfile)
			Xfile.close()
			counter += 1		
		except:
			print('no file for sonata'+s)

		