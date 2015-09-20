#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os

def get_desc():
	return "festival TTS engine"

def create(target):
	myModule = module.Module(__file__, 'eststring', 'LIBRARY')
	myModule.add_src_file([
		"speech_tools/base_class/string/EST_String.cc",
		"speech_tools/base_class/string/EST_Regex.cc",
		"speech_tools/base_class/string/EST_Chunk.cc",
		"speech_tools/base_class/string/regexp.cc",
		"speech_tools/base_class/string/regerror.c",
		"speech_tools/base_class/string/regsub.c",
		"speech_tools/base_class/string/EST_strcasecmp.c",
		])
	
	myModule.add_export_path(os.path.join(tools.get_current_path(__file__), "speech_tools/include"))
	myModule.add_export_path(os.path.join(tools.get_current_path(__file__), "speech_tools/base_class/string/"))
	myModule.compile_flags('c++', "-fno-implicit-templates")
	
	return myModule


