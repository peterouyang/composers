import scoreparser as sp
import music21
import pickle

counter = 1

for i in range(9):
	filename = 'mXML/chopin28-0%d.xml' % (1 + i)
	print('processing ', filename)
	sChopin = music21.converter.parse(filename)
	Chopin_notes = sp.get_note_list(sChopin)
	X = sp.make_pitch_range_rhythm_features(Chopin_notes,sChopin)
	cXfile = open('Chopin_%d_X' % counter,'wb')
	pickle.dump(X,cXfile)
	cXfile.close()
	counter += 1


for i in range(9,24):
	filename = 'mXML/chopin28-%d.xml' % (1 + i)
	print('processing ', filename)
	sChopin = music21.converter.parse(filename)
	Chopin_notes = sp.get_note_list(sChopin)
	X = sp.make_pitch_range_rhythm_features(Chopin_notes,sChopin)
	cXfile = open('Chopin_%d_X' % counter,'wb')
	pickle.dump(X,cXfile)
	cXfile.close()
	counter += 1

mazurkas = ['06-1','06-2','06-3','06-4','07-1','07-2','07-3','07-4','07-5','17-1','17-2','17-3',
			'17-4','24-1','24-2','24-3','24-4','30-1','30-2','30-3','30-4','33-1',
			'33-2','33-3','33-4','41-1','41-2','41-3','41-4',
			'50-1','50-2','50-3','56-1','56-2','56-3','59-1','59-2','59-3','63-1',
			'63-2','63-3','67-1','67-2',
			'67-3','67-4','68-1','68-2','68-3','68-4']

for i in mazurkas:
	filename = 'mXML/chopin' + i + '.xml'
	print('processing ', filename)
	s = music21.converter.parse(filename)
	some_notes = sp.get_note_list(s)
	X = sp.make_pitch_range_rhythm_features(some_notes,s)
	cXfile = open('Chopin_%d_X' % counter,'wb')
	pickle.dump(X,cXfile)
	cXfile.close()
	counter += 1


for i in range(1,10):
	try:
		sChopin = music21.converter.parse('mXML/chopin10-0%d.xml' % i)
		Chopin_notes = sp.get_note_list(sChopin)
		X=sp.make_pitch_range_rhythm_features(Chopin_notes,sChopin)
		cXfile = open('Chopin_%d_X' % counter,'wb')
		pickle.dump(X,cXfile)
		cXfile.close()
		counter += 1
	except:
		print('Job on mXML/chopin10-0%d.xml' % i, 'error')

try:
	sChopin = music21.converter.parse('mXML/chopin10-11.xml')
	Chopin_notes = sp.get_note_list(sChopin)
	X=sp.make_pitch_range_rhythm_features(Chopin_notes,sChopin)
	cXfile = open('Chopin_%d_X' % counter,'wb')
	pickle.dump(X,cXfile)
	cXfile.close()
	counter += 1
except:
	print('Job on mXML/chopin10-11.xml', 'error')

try:
	sChopin = music21.converter.parse('mXML/chopin10-12.xml')
	Chopin_notes = sp.get_note_list(sChopin)
	X=sp.make_pitch_range_rhythm_features(Chopin_notes,sChopin)
	cXfile = open('Chopin_%d_X' % counter,'wb')
	pickle.dump(X,cXfile)
	cXfile.close()
	counter += 1
except:
	print('Job on mXML/chopin10-12.xml' , 'error')



try:
	sChopin = music21.converter.parse('mXML/chopin9-1.xml')
	Chopin_notes = sp.get_note_list(sChopin)
	X=sp.make_pitch_range_rhythm_features(Chopin_notes,sChopin)
	cXfile = open('Chopin_%d_X' % counter,'wb')
	pickle.dump(X,cXfile)
	cXfile.close()
	counter += 1
except:
	print('Job on mXML/chopin9-1.xml' , 'error')
try:
	sChopin = music21.converter.parse('mXML/chopin9-2.xml')
	Chopin_notes = sp.get_note_list(sChopin)
	X=sp.make_pitch_range_rhythm_features(Chopin_notes,sChopin)
	cXfile = open('Chopin_%d_X' % counter,'wb')
	pickle.dump(X,cXfile)
	cXfile.close()
	counter += 1
except:
	print('Job on mXML/chopin9-2.xml', 'error')
try:
	sChopin = music21.converter.parse('mXML/chopin15-1.xml')
	Chopin_notes = sp.get_note_list(sChopin)
	X=sp.make_pitch_range_rhythm_features(Chopin_notes,sChopin)
	cXfile = open('Chopin_%d_X' % counter,'wb')
	pickle.dump(X,cXfile)
	cXfile.close()
	counter += 1
except:
	print('Job on mXML/chopin15-1.xml', 'error')
try:
	sChopin = music21.converter.parse('mXML/chopin15-3.xml')
	Chopin_notes = sp.get_note_list(sChopin)
	X=sp.make_pitch_range_rhythm_features(Chopin_notes,sChopin)
	cXfile = open('Chopin_%d_X' % counter,'wb')
	pickle.dump(X,cXfile)
	cXfile.close()
	counter += 1
except:
	print('Job on mXML/chopin15-3.xml', 'error')
try:
	sChopin = music21.converter.parse('mXML/chopin37-2.xml')
	Chopin_notes = sp.get_note_list(sChopin)
	X=sp.make_pitch_range_rhythm_features(Chopin_notes,sChopin)
	cXfile = open('Chopin_%d_X' % counter,'wb')
	pickle.dump(X,cXfile)
	cXfile.close()
	counter += 1
except:
	print('Job on mXML/chopin37-2.xml', 'error')
try:
	sChopin = music21.converter.parse('mXML/chopin48-1.xml')
	Chopin_notes = sp.get_note_list(sChopin)
	X=sp.make_pitch_range_rhythm_features(Chopin_notes,sChopin)
	cXfile = open('Chopin_%d_X' % counter,'wb')
	pickle.dump(X,cXfile)
	cXfile.close()
	counter += 1
except:
	print('Job on mXML/chopin48-1.xml', 'error')
try:
	sChopin = music21.converter.parse('mXML/chopin72-1.xml')
	Chopin_notes = sp.get_note_list(sChopin)
	X=sp.make_pitch_range_rhythm_features(Chopin_notes,sChopin)
	cXfile = open('Chopin_%d_X' % counter,'wb')
	pickle.dump(X,cXfile)
	cXfile.close()
	counter += 1
except:
	print('Job on mXML/chopin72-1.xml', 'error')
try:
	sChopin = music21.converter.parse('mXML/chopin62-1.xml')
	Chopin_notes = sp.get_note_list(sChopin)
	X=sp.make_pitch_range_rhythm_features(Chopin_notes,sChopin)
	cXfile = open('Chopin_%d_X' % counter,'wb')
	pickle.dump(X,cXfile)
	cXfile.close()
	counter += 1
except:
	print('Job on mXML/chopin62-1.xml', 'error')
try:
	sChopin = music21.converter.parse('mXML/chopin62-2.xml')
	Chopin_notes = sp.get_note_list(sChopin)
	X=sp.make_pitch_range_rhythm_features(Chopin_notes,sChopin)
	cXfile = open('Chopin_%d_X' % counter,'wb')
	pickle.dump(X,cXfile)
	cXfile.close()
	counter += 1
except:
	print('Job on mXML/chopin62-2.xml', 'error')

try:
	sChopin = music21.converter.parse('mXML/chopin_52.xml')
	Chopin_notes = sp.get_note_list(sChopin)
	X=sp.make_pitch_range_rhythm_features(Chopin_notes,sChopin)
	cXfile = open('Chopin_%d_X' % counter,'wb')
	pickle.dump(X,cXfile)
	cXfile.close()
	counter += 1
except:
	print('Ballade Op 52 error')

