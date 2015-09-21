#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os

def get_desc():
	return "festival TTS engine"

def create(target):
	my_module = module.Module(__file__, 'estbase-audio', 'LIBRARY')
	
	my_module.add_module_depend(['eststring', 'estbase-base_class'])
	
	my_module.add_export_path(os.path.join(tools.get_current_path(__file__), "speech_tools/include"))
	
	my_module.add_src_file([
		"speech_tools/audio/gen_audio.cc",
		"speech_tools/audio/nas.cc",
		"speech_tools/audio/esd.cc",
		"speech_tools/audio/sun16audio.cc",
		"speech_tools/audio/mplayer.cc",
		"speech_tools/audio/win32audio.cc",
		"speech_tools/audio/irixaudio.cc",
		"speech_tools/audio/os2audio.cc",
		"speech_tools/audio/macosxaudio.cc",
		"speech_tools/audio/linux_sound.cc"
		])
	my_module.compile_flags('c++', "-fno-implicit-templates")
	my_module.compile_flags('c++', "-DSUPPORT_ALSALINUX")
	my_module.compile_flags('c++', "-DINSTANTIATE_TEMPLATES")
	return my_module

