import music21
import scoreparser as sp
import pickle



labels = ['L001K514','L002K384','L003K502','L008K461','L009K303','L010K084','L011K534',
'L012K478','L013K060','L014K492','L015K160','L016K306','L027K238','L051K166',
'L052K165','L053K075','L054K200','L055K330','L056K281','L064K148','L101K156',
'L154K235','L166K085','L178K258','L188K525','L198K296','L240K369','L267K052',
'L301K049','L302K372','L303K170','L304K470','L305K251','L306K345','L307K269',
'L333K425','L334K122','L335K055','L336K093','L337K336','L338K450','L339K512',
'L340K476','L341K320','L342K220','L343K434','L344K114','L345K113','L346K408',
'L347K227','L348K244','L349K146','L350K498','L351K225','L400K360','L481K025',
'L503K513','L523K205']


for i,s in enumerate(labels):
	try:
		filename = 'mXML/scarlatti_' + s + '.xml'
		print('processing ', filename)
		stream = music21.converter.parse(filename)
		notes = sp.get_note_list(stream)
		X = sp.make_pitch_range_rhythm_features(notes,stream)
		Xfile = open('Scarlatti_%d_X' % i,'wb')
		pickle.dump(X,Xfile)
		Xfile.close()
	except:
		print('error on',filename)

