import music21
import scoreparser as sp
import pickle

counter = 1

three_mvt_sonatas = ['01','02','03','04','05','07','08','09',
					 '10','12','13','14','15','16','17']
for s in three_mvt_sonatas:
	for i in range(1,4):
		filename = 'mXML/mozart_pno_sonata' + s +  ('-%d' % i) + '.xml'
		print('processing ', filename)
		sMozart = music21.converter.parse(filename)
		Mozart_notes = sp.get_note_list(sMozart)
		X = sp.make_pitch_range_rhythm_features(Mozart_notes,sMozart)
		Xfile = open('Mozart_%d_X' % counter,'wb')
		pickle.dump(X,Xfile)
		Xfile.close()
		counter += 1

mozart_sonata_numbers = ['06-1','06-2','06-3a','06-3b','06-3c','06-3d','06-3e',
						'06-3f','06-3g','06-3h','06-3i','06-3j','06-3k','06-3l',
						'06-3m','11-1a','11-1b','11-1c','11-1d','11-1e','11-1f','11-1g',
						'11-2','11-3']

for s in mozart_sonata_numbers:
	filename = 'mXML/mozart_pno_sonata' + s + '.xml'
	print('processing ', filename)
	sMozart = music21.converter.parse(filename)
	Mozart_notes = sp.get_note_list(sMozart)
	X = sp.make_pitch_range_rhythm_features(Mozart_notes,sMozart)
	Xfile = open('Mozart_%d_X' % counter,'wb')
	pickle.dump(X,Xfile)
	Xfile.close()
	counter += 1

sMozart = music21.converter.parse('mXML/mozart_k265.xml')
Mozart_notes = sp.get_note_list(sMozart)
X = sp.make_pitch_range_rhythm_features_varying_timesig(Mozart_notes,sMozart)
Xfile = open('Mozart_%d_X' % counter,'wb')
pickle.dump(X,Xfile)
Xfile.close()
counter += 1
