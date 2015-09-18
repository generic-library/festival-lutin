#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools

def get_desc():
	return "festival TTS engine"

def create(target):
	myModule = module.Module(__file__, 'festival', 'LIBRARY')
	myModule.add_src_file([
		# TODO: ...
		])
	myModule.compile_version_CC(1999)
	# TODO: copy in install folder ...
	myModule.add_export_path(tools.get_current_path(__file__) + "/festival/src/include")
	return myModule


