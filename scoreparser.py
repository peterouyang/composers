import music21 as mus

# define decomposition of beats into primary and secondary beats
#
# any note not on one of these beats put in tertiary class
#
# NB a little arbitrary for 5,7,10,11
#
beat_class = {	2:  ([1.0],[2.0]),
				3:  ([1.0],[2.0,3.0]),
				4:  ([1.0,3.0],[2.0,4.0]),
				5:  ([1.0],[2.0,3.0,4.0,5.0]),
				6:  ([1.0,4.0],[2.0,3.0,5.0,6.0]),
				7:  ([1.0],[2.0,3.0,4.0,5.0,6.0]),
				8:  ([1.0,5.0],[3.0,7.0]),
				9:  ([1.0], [4.0,7.0]),
				10: ([1.0,6.0],[3.0,4.0,8.0,9.0]),
				11: ([1.0],[6.0,7.0]),
				12: ([1.0,7.0],[4.0,10.0]),
				24: ([1.0,13.0],[7.0,19.0])}

# get time signature for every bar. Place in a dict indexed by bar number
#
# NB: this assumes time signature is the same for all parts, which might
# not be true for 20th/21st century music
def get_time_sig_dict(stream):
	time_sig_dict = {}

	num_measures = stream.parts[0]. \
					getElementsByClass(mus.stream.Measure)[-1]. \
					measureNumber

	for i in range(num_measures):
		tmp = stream.measure(i+1).flat. \
				getElementsByClass(mus.meter.TimeSignature)[0]
		num_beats = int(tmp.barDuration.quarterLength/tmp.beatDuration.quarterLength)
		time_sig_dict[i+1] = [num_beats,float(tmp.beatDuration.quarterLength)]

	return time_sig_dict

def get_time_sig_measure(stream, measure_num):
	tmp = stream.measure(measure_num).flat. \
			getElementsByClass(mus.meter.TimeSignature)[0]

	num_beats = int(tmp.barDuration.quarterLength/tmp.beatDuration.quarterLength)

	return [num_beats, float(tmp.beatDuration.quarterLength)] 


# get all the notes
#
# NB may later want to add functionality for notes tied over the bar line
# and extra conditions for grace notes
#
# note entries are recorded as a list
# [<measureNumber>, <beat>, <duration>, <pitchClass>, <octave>]
#
# pitchclass is between 0 and 11; C-natural is 0
# octave is the standard defn where C4 is middle C
# beat is location in the bar (1.0 is downbeat, etc)
# duration is length of note measured in quarter notes
def get_note_list(stream):
	note_stream = stream.flat.getElementsByClass(mus.note.Note);
	num_notes = len(note_stream);
	note_list=[];

	# get notes encoded as regular notes
	for i in range(num_notes):
		this_note = note_stream[i];
	# the condition that measureNumber is not zero removes the upbeat
		if this_note.isGrace == False and this_note.measureNumber != 0:
			note_list += [[this_note.measureNumber, 
							this_note.beat,
							float(this_note.quarterLength),
							this_note.pitchClass, 
							this_note.octave]]

	# get notes that are encoded as chords
	chord_stream = stream.flat.getElementsByClass(mus.chord.Chord);
	num_chords = len(chord_stream)
	notes_from_chords = [];

	for i in range(num_chords):
		this_chord = chord_stream[i]
		num_notes_in_chord = len(this_chord.pitches)
		if this_chord.isGrace == False and this_chord.measureNumber != 0:
			for j in range(num_notes_in_chord):
				this_note = chord_stream[i].pitches[j]
				notes_from_chords += [[this_chord.measureNumber, this_chord.beat,
									 float(this_chord.duration.quarterLength),
									 this_note.pitchClass,
									 this_note.octave]]

	note_list += notes_from_chords

	note_list.sort()

	return note_list

# function returns a list of lists
# each sublist represents one bar
def make_features(notelist, stream):

	current_measure = 0
	piece_data = []
	[num_beats,beat_length] = get_time_sig_measure(stream,1)
	[strong,weak] = beat_class[num_beats]
	# data structure contains 72 (0-71) pitch bins
	# each note contributes an entry

	for i, note in enumerate(notelist):
		if note[0] != current_measure:
			piece_data += [[0] * 216]
			current_measure = note[0]
		if note[4] <= 1:
			note_number = note[3]
		elif note[4] >= 6:
			note_number = note[3] + 60
		else:
			note_number = note[3] + 12*(note[4] - 1)
		
		if note[1] in strong:
			piece_data[-1][note_number] += note[2]
		elif note[1] in weak:
			piece_data[-1][note_number + 72] += note[2]
		else:
			piece_data[-1][note_number + 144] += note[2]

	return piece_data


# version of make_features when time signature changes throughout
# piece.
#
# NB somewhat slow, because of music21 implementation
#  
# So if time signature is fixed, better to use make_features()
#
def make_features_varying_timesig(notelist, stream):

	current_measure = 0
	piece_data = []
	[num_beats,beat_length] = get_time_sig_measure(stream,1)
	[strong,weak] = beat_class[num_beats]
	# data structure contains 72 (0-71) pitch bins
	# each note contributes an entry

	for i, note in enumerate(notelist):
		if note[0] != current_measure:
			piece_data += [[0] * 216]
			current_measure = note[0]
			[num_beats,beat_length] = get_time_sig_measure(stream,current_measure)
			[strong,weak] = beat_class[num_beats]
		if note[4] <= 1:
			note_number = note[3]
		elif note[4] >= 6:
			note_number = note[3] + 60
		else:
			note_number = note[3] + 12*(note[4] - 1)
		
		if note[1] in strong:
			piece_data[-1][note_number] += note[2]
		elif note[1] in weak:
			piece_data[-1][note_number + 72] += note[2]
		else:
			piece_data[-1][note_number + 144] += note[2]

	return piece_data


def reduce_pitch_range_4_octaves(featurelist):
	if len(featurelist[0]) != 216:
		print('Features wrong size')
		return []

	new_feature_list = []

	for old_measure in featurelist:
		new_measure = [0] * 144 
		# first group
		for i in range(12):
			new_measure[i] += old_measure[i]
		for i in range(12,60):
			new_measure[i-12] += old_measure[i]
		for i in range(60,72):
			new_measure[i-24] += old_measure[i]
		# second group
		for i in range(72,84):
			new_measure[i-24] += old_measure[i]
		for i in range(84,132):
			new_measure[i-36] += old_measure[i]
		for i in range(132,144):
			new_measure[i-48] += old_measure[i]
		# third group
		for i in range(144,156):
			new_measure[i-48] += old_measure[i]
		for i in range(156,204):
			new_measure[i-60] += old_measure[i]
		for i in range(204,216):
			new_measure[i-72] += old_measure[i]
		new_feature_list += [new_measure]

	return new_feature_list

def reduce_pitch_range_1_octave(featurelist):
	if len(featurelist[0]) != 216:
		print('Features wrong size')
		return []

	new_feature_list = []
	for old_measure in featurelist:
		new_measure = [0] * 36 
		
		for i in range(3):
			for j in range(6):
				for k in range(12):
					new_measure[12*i+k] += old_measure[72*i+12*j+k]
		new_feature_list += [new_measure]

	return new_feature_list

def eliminate_beat_location(featurelist):
	n_features = int(len(featurelist[0])/3)

	new_feature_list = []
	for old_measure in featurelist:
		new_measure = [0] * n_features 
		
		for i in range(3):
			for j in range(n_features):
				new_measure[j] += old_measure[j + n_features*i]
		new_feature_list += [new_measure]

	return new_feature_list

def transpose_pitch_features(pitch_data, half_steps):
	''' code to transpose pitch features.  It's assumed that we are
	working with a 12-dimensional pitch feature vector'''
	tmp_data = [0]*12
	for i, p in enumerate(pitch_data):
		tmp_data[(i+half_steps) % 12]  = p

	return tmp_data

#
# note entries are recorded as a list
# [<measureNumber>, <beat>, <duration>, <pitchClass>, <octave>]
#
# pitchclass is between 0 and 11; C-natural is 0
# octave is the standard defn where C4 is middle C
# beat is location in the bar (1.0 is downbeat, etc)
# duration is length of note measured in quarter notes


def duration_type(beat_fraction):
	if beat_fraction > 1:
		return 0
	elif beat_fraction <= 1 and beat_fraction > 0.75:
		return 1
	elif beat_fraction <= 0.75 and beat_fraction > 0.5:
		return 2
	elif beat_fraction <= 0.5 and beat_fraction > 0.34:
		return 3
	elif beat_fraction <= 0.34 and beat_fraction > 0.25:
		return 4
	elif beat_fraction <= 0.25 and beat_fraction > 0.17:
		return 5
	elif beat_fraction <= 0.17 and beat_fraction > 0.13:
		return 6
	else:
		return 7

def make_pitch_range_rhythm_features(notelist, stream):

	current_measure = 0
	piece_data = []
	[num_beats,beat_length] = get_time_sig_measure(stream,1)

	for i, note in enumerate(notelist):
		if note[0] != current_measure:
			# 24 bins for pitches on & off beat

			piece_data += [[0] * 24 + [0] * 8 + [0] * 16]
			current_measure = note[0]

		beat = note[1]
		duration = note[2]
		pitchclass = note[3]
		octave = note[4]

		if int(beat) - beat == 0:# and octave < 4:
			piece_data[-1][pitchclass] += duration/beat_length
			piece_data[-1][32 + duration_type(duration/beat_length)] += 1
		# elif int(beat) - beat == 0 and octave >= 4:
		# 	piece_data[-1][pitchclass] += duration/beat_length
		# 	piece_data[-1][48 + duration_type(duration/beat_length)] += 1
		# elif int(beat) - beat != 0 and octave < 4:
		# 	piece_data[-1][pitchclass + 12] += duration/beat_length
		# 	piece_data[-1][40 + duration_type(duration/beat_length)] += 1
		else:
			piece_data[-1][pitchclass + 12] += duration/beat_length
			#piece_data[-1][56 + duration_type(duration/beat_length)] += 1
			piece_data[-1][40 + duration_type(duration/beat_length)] += 1
		if octave <= 7 and octave >= 0:
			piece_data[-1][24 + octave] += duration/beat_length
		elif octave < 0:
			piece_data[-1][24] += duration/beat_length
		else:
			piece_data[-1][31] += duration/beat_length

	return piece_data



def make_pitch_range_rhythm_features_varying_timesig(notelist, stream):

	current_measure = 0
	piece_data = []
	[num_beats,beat_length] = get_time_sig_measure(stream,1)

	for i, note in enumerate(notelist):
		if note[0] != current_measure:
			# 24 bins for pitches on & off beat

			piece_data += [[0] * 24 + [0] * 8 + [0] * 16]
			current_measure = note[0]
			[num_beats,beat_length] = get_time_sig_measure(stream,current_measure)


		beat = note[1]
		duration = note[2]
		pitchclass = note[3]
		octave = note[4]

		if int(beat) - beat == 0:# and octave < 4:
			piece_data[-1][pitchclass] += duration/beat_length
			piece_data[-1][32 + duration_type(duration/beat_length)] += 1
		# elif int(beat) - beat == 0 and octave >= 4:
		# 	piece_data[-1][pitchclass] += duration/beat_length
		# 	piece_data[-1][48 + duration_type(duration/beat_length)] += 1
		# elif int(beat) - beat != 0 and octave < 4:
		# 	piece_data[-1][pitchclass + 12] += duration/beat_length
		# 	piece_data[-1][40 + duration_type(duration/beat_length)] += 1
		else:
			piece_data[-1][pitchclass + 12] += duration/beat_length
			#piece_data[-1][56 + duration_type(duration/beat_length)] += 1
			piece_data[-1][40 + duration_type(duration/beat_length)] += 1
		if octave <= 7 and octave >= 0:
			piece_data[-1][24 + octave] += duration/beat_length
		elif octave < 0:
			piece_data[-1][24] += duration/beat_length
		else:
			piece_data[-1][31] += duration/beat_length

	return piece_data
