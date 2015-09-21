#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os

def get_desc():
	return "festival TTS engine"

def create(target):
	my_module = module.Module(__file__, 'estools-intonation', 'LIBRARY')
	
	my_module.add_module_depend(['eststring'])
	
	my_module.add_export_path(os.path.join(tools.get_current_path(__file__), "speech_tools/include"))
	my_module.compile_flags('c++', "-fno-implicit-templates")
	my_module.compile_flags('c++', "-DINSTANTIATE_TEMPLATES")
	
	my_module.add_src_file([
		"speech_tools/intonation/tilt/tilt_analysis.cc",
		"speech_tools/intonation/tilt/tilt_synthesis.cc",
		"speech_tools/intonation/tilt/tilt_utils.cc"
		])
	
	return my_module
