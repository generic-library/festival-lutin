#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os

def get_desc():
	return "festival TTS engine"

def create(target):
	my_module = module.Module(__file__, 'eststring', 'LIBRARY')
	my_module.add_src_file([
		"speech_tools/base_class/string/EST_String.cc",
		"speech_tools/base_class/string/EST_Regex.cc",
		"speech_tools/base_class/string/EST_Chunk.cc",
		"speech_tools/base_class/string/regexp.cc",
		"speech_tools/base_class/string/regerror.c",
		"speech_tools/base_class/string/regsub.c",
		"speech_tools/base_class/string/EST_strcasecmp.c",
		])
	
	my_module.add_export_path(os.path.join(tools.get_current_path(__file__), "speech_tools/include"))
	my_module.add_export_path(os.path.join(tools.get_current_path(__file__), "speech_tools/base_class/string/"))
	my_module.compile_flags('c++', "-fno-implicit-templates")
	
	return my_module


