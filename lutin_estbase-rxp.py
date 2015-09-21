#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os

def get_desc():
	return "festival TTS engine"

def create(target):
	my_module = module.Module(__file__, 'estbase-rxp', 'LIBRARY')
	
	my_module.add_module_depend(['eststring'])
	
	my_module.add_src_file([
		"speech_tools/rxp/charset.c",
		"speech_tools/rxp/ctype16.c",
		"speech_tools/rxp/dtd.c",
		"speech_tools/rxp/string16.c",
		"speech_tools/rxp/url.c",
		"speech_tools/rxp/ctype16.c",
		"speech_tools/rxp/input.c",
		"speech_tools/rxp/stdio16.c",
		"speech_tools/rxp/system.c",
		"speech_tools/rxp/xmlparser.c",
		"speech_tools/rxp/XML_Parser.cc"
		])
	
	my_module.add_export_path(os.path.join(tools.get_current_path(__file__), "speech_tools/include"))
	my_module.add_export_path(os.path.join(tools.get_current_path(__file__), "speech_tools/include/rxp"))
	my_module.compile_flags('c', "-DCHAR_SIZE=8")
	my_module.compile_flags('c++', "-DINSTANTIATE_TEMPLATES")
	
	return my_module

