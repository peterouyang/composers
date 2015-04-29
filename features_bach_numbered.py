import scoreparser as sp
import music21
import pickle

# make features for Book I of the WTC

counter = 1

for i in range(24):
	filename = 'mXML/bwv%d.xml' % (846 + i)
	print('processing ', filename)
	sBach = music21.converter.parse(filename)
	Bach_notes = sp.get_note_list(sBach)
	X = sp.make_pitch_range_rhythm_features(Bach_notes,sBach)
	Xfile = open('Bach_%d_X' % counter,'wb')
	pickle.dump(X,Xfile)
	Xfile.close()
	counter += 1


for i in range(24):
	filename = 'mXML/bwv%da.xml' % (846 + i)
	print('processing ', filename)
	sBach = music21.converter.parse(filename)
	Bach_notes = sp.get_note_list(sBach)
	X = sp.make_pitch_range_rhythm_features(Bach_notes,sBach)
	Xfile = open('Bach_%d_X' % counter,'wb')
	pickle.dump(X,Xfile)
	Xfile.close()
	counter += 1

for i in range(24):
	try:
		filename = 'mXML/bwv%d.xml' % (870 + i)
		print('processing ', filename)
		sBach = music21.converter.parse(filename)
		Bach_notes = sp.get_note_list(sBach)
		X = sp.make_pitch_range_rhythm_features(Bach_notes,sBach)
		Xfile = open('Bach_%d_X' % counter,'wb')
		pickle.dump(X,Xfile)
		Xfile.close()
		counter += 1
	except:
		print('error on', filename)

for i in range(24):
	try:
		filename = 'mXML/bwv%da.xml' % (870 + i)
		print('processing ', filename)
		sBach = music21.converter.parse(filename)
		Bach_notes = sp.get_note_list(sBach)
		X = sp.make_pitch_range_rhythm_features(Bach_notes,sBach)
		Xfile = open('Bach_%d_X' % counter,'wb')
		pickle.dump(X,Xfile)
		Xfile.close()
		counter += 1
	except:
		print('error on', filename)

filename = 'mXML/bach_goldberg_aria.xml'
print('processing ', filename)		
s = music21.converter.parse(filename)
notes = sp.get_note_list(s)
X = sp.make_pitch_range_rhythm_features_varying_timesig(notes,s)
fileout_name = 'bach_goldberg_aria_X'
Xfile = open('Bach_%d_X' % counter,'wb')
pickle.dump(X,Xfile)
Xfile.close()
counter += 1

for i in range(1,31):
	try:
		filename = 'mXML/bach_goldberg_var%d.xml' % i
		print('processing ', filename)		
		s = music21.converter.parse(filename)
		notes = sp.get_note_list(s)
		X = sp.make_pitch_range_rhythm_features_varying_timesig(notes,s)
		fileout_name = 'bach_goldberg_var%d_X' % i
		Xfile = open(fileout_name,'wb')
		pickle.dump(X,Xfile)
		Xfile = open('Bach_%d_X' % counter,'wb')
		pickle.dump(X,Xfile)
		Xfile.close()
		counter += 1
	except:
		print('error on', filename)

inv_numbers = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15']


for s in inv_numbers:
	try:
		filename = 'mXML/bach_invention_' + s + '.xml' 	 
		print('processing ', filename)
		strm = music21.converter.parse(filename)
		notes = sp.get_note_list(strm)
		X = sp.make_pitch_range_rhythm_features(notes,strm)
		
		Xfile = open('Bach_%d_X' % counter,'wb')
		pickle.dump(X,Xfile)
		Xfile.close()
		counter += 1
	except:
		print('error on', filename)



