#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os

def get_desc():
	return "festival TTS engine"

def create(target):
	my_module = module.Module(__file__, 'estools-siod', 'LIBRARY')
	
	my_module.add_module_depend(['eststring'])
	
	my_module.add_src_file([
		"speech_tools/siod/slib.cc",
		"speech_tools/siod/slib_core.cc",
		"speech_tools/siod/slib_doc.cc",
		"speech_tools/siod/slib_file.cc",
		"speech_tools/siod/slib_format.cc",
		"speech_tools/siod/slib_list.cc",
		"speech_tools/siod/slib_math.cc",
		"speech_tools/siod/slib_sys.cc",
		"speech_tools/siod/slib_server.cc",
		"speech_tools/siod/slib_str.cc",
		"speech_tools/siod/slib_xtr.cc",
		"speech_tools/siod/slib_repl.cc",
		"speech_tools/siod/slib_python.cc",
		"speech_tools/siod/io.cc",
		"speech_tools/siod/trace.cc",
		"speech_tools/siod/siod.cc",
		"speech_tools/siod/siod_est.cc",
		"speech_tools/siod/siodeditline.c",
		"speech_tools/siod/el_complete.c",
		"speech_tools/siod/editline.c",
		"speech_tools/siod/el_sys_unix.c",
		])
	
	my_module.add_export_path(os.path.join(tools.get_current_path(__file__), "speech_tools/include"))
	my_module.compile_flags('c++', "-fno-implicit-templates")
	my_module.compile_flags('c++', "-DINSTANTIATE_TEMPLATES")
	my_module.compile_flags('c', "-DSUPPORT_EDITLINE")
	
	return my_module
