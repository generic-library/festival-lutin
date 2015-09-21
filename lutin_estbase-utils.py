#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os

def get_desc():
	return "festival TTS engine"

def create(target):
	my_module = module.Module(__file__, 'estbase-utils', 'LIBRARY')
	
	my_module.add_module_depend(['eststring'])
	
	my_module.add_export_path(os.path.join(tools.get_current_path(__file__), "speech_tools/include"))
	
	my_module.compile_flags('c++', "-fno-implicit-templates")
	my_module.add_src_file([
		"speech_tools/utils/cmd_line.cc",
		"speech_tools/utils/util_io.cc",
		"speech_tools/utils/filetrans.cc",
		"speech_tools/utils/cmd_line_aux.cc",
		"speech_tools/utils/EST_swapping.cc",
		"speech_tools/utils/est_file.cc",
		"speech_tools/utils/EST_cutils.c",
		"speech_tools/utils/EST_error.c",
		"speech_tools/utils/walloc.c",
		"speech_tools/utils/system_specific_unix.c"
		])
	my_module.compile_flags('c++', "-DINSTANTIATE_TEMPLATES")
	my_module.compile_flags('c++', "-DFTNAME='Festival Speech Tools Library'")
	my_module.compile_flags('c++', "-DFTLIBDIRC='" + tools.get_current_path(__file__) + "/festival/lib '")
	my_module.compile_flags('c++', "-DFTVERSION='2.4'")
	my_module.compile_flags('c++', "-DFTSTATE='release'")
	my_module.compile_flags('c++', "-DFTDATE='December 2014'")
	my_module.compile_flags('c++', "-DFTSTATE='release'")
	my_module.compile_flags('c++', '-DFTOSTYPE=\\"unknown_DebianGNULinux\\"')
	
	return my_module

