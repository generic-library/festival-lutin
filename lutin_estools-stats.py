#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os

def get_desc():
	return "festival TTS engine"

def create(target):
	my_module = module.Module(__file__, 'estools-stats', 'LIBRARY')
	
	my_module.add_module_depend(['eststring'])
	
	my_module.add_export_path(os.path.join(tools.get_current_path(__file__), "speech_tools/include"))
	my_module.compile_flags('c++', "-fno-implicit-templates")
	my_module.compile_flags('c++', "-DINSTANTIATE_TEMPLATES")
	
	my_module.add_src_file([
		"speech_tools/stats/EST_cluster.cc",
		"speech_tools/stats/EST_multistats.cc",
		"speech_tools/stats/confusion.cc",
		"speech_tools/stats/EST_Discrete.cc",
		"speech_tools/stats/EST_DProbDist.cc",
		"speech_tools/stats/EST_ols.cc",
		"speech_tools/stats/EST_viterbi.cc",
		"speech_tools/stats/dynamic_program.cc"
		])
	
	my_module.add_src_file([
		"speech_tools/stats/wagon/dlist.cc",
		"speech_tools/stats/wagon/wagon_aux.cc",
		"speech_tools/stats/wagon/wagonint.cc",
		"speech_tools/stats/wagon/wagon.cc"
		])
	
	my_module.add_src_file([
		"speech_tools/stats/kalman_filter/EST_kalman.cc",
		])
	
	return my_module
