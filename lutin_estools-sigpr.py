#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os

def get_desc():
	return "festival TTS engine"

def create(target):
	my_module = module.Module(__file__, 'estools-sigpr', 'LIBRARY')
	
	my_module.add_module_depend(['eststring'])
	
	my_module.add_export_path(os.path.join(tools.get_current_path(__file__), "speech_tools/include"))
	my_module.compile_flags('c++', "-fno-implicit-templates")
	my_module.compile_flags('c++', "-DINSTANTIATE_TEMPLATES")
	
	my_module.add_src_file([
		"speech_tools/sigpr/EST_Window.cc",
		"speech_tools/sigpr/delta.cc",
		"speech_tools/sigpr/filter.cc",
		"speech_tools/sigpr/sigpr_frame.cc",
		"speech_tools/sigpr/sigpr_utt.cc",
		"speech_tools/sigpr/pitchmark.cc",
		"speech_tools/sigpr/spectrogram.cc",
		"speech_tools/sigpr/misc.cc",
		"speech_tools/sigpr/fft.cc"
		])
	
	my_module.add_src_file([
		"speech_tools/sigpr/pda/pcb_smoother.cc",
		"speech_tools/sigpr/pda/smooth_pda.cc",
		"speech_tools/sigpr/pda/pda.cc",
		"speech_tools/sigpr/pda/srpd1.3.cc"
		])
	
	
	return my_module
