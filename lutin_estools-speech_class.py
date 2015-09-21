#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os

def get_desc():
	return "festival TTS engine"

def create(target):
	my_module = module.Module(__file__, 'estools-speech_class', 'LIBRARY')
	
	my_module.add_module_depend(['eststring'])
	
	my_module.add_export_path(os.path.join(tools.get_current_path(__file__), "speech_tools/include"))
	my_module.compile_flags('c++', "-fno-implicit-templates")
	my_module.compile_flags('c++', "-DINSTANTIATE_TEMPLATES")
	
	my_module.add_src_file([
		"speech_tools/speech_class/EST_Wave.cc",
		"speech_tools/speech_class/EST_track_aux.cc",
		"speech_tools/speech_class/EST_wave_temp.cc",
		"speech_tools/speech_class/EST_wave_cuts.cc",
		"speech_tools/speech_class/ssff.cc",
		"speech_tools/speech_class/esps_io.cc",
		"speech_tools/speech_class/esps_utils.cc",
		"speech_tools/speech_class/EST_wave_io.cc",
		"speech_tools/speech_class/EST_wave_utils.cc",
		"speech_tools/speech_class/EST_TrackMap.cc",
		"speech_tools/speech_class/EST_Track.cc",
		"speech_tools/speech_class/wave_t.cc",
		"speech_tools/speech_class/track_t.cc",
		"speech_tools/speech_class/EST_wave_aux.cc",
		"speech_tools/speech_class/EST_TrackFile.cc",
		"speech_tools/speech_class/EST_WaveFile.cc"
		])
	
	
	return my_module
