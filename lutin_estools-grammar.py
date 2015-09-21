#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os

def get_desc():
	return "festival TTS engine"

def create(target):
	my_module = module.Module(__file__, 'estools-grammar', 'LIBRARY')
	
	my_module.add_module_depend(['eststring'])
	
	my_module.add_export_path(os.path.join(tools.get_current_path(__file__), "speech_tools/include"))
	my_module.compile_flags('c++', "-fno-implicit-templates")
	my_module.compile_flags('c++', "-DINSTANTIATE_TEMPLATES")
	
	my_module.add_src_file([
		"speech_tools/grammar/scfg/EST_SCFG.cc",
		"speech_tools/grammar/scfg/EST_SCFG_inout.cc",
		"speech_tools/grammar/scfg/EST_SCFG_Chart.cc"
		])
	
	my_module.add_src_file([
		"speech_tools/grammar/wfst/EST_WFST.cc",
		"speech_tools/grammar/wfst/wfst_regex.cc",
		"speech_tools/grammar/wfst/wfst_ops.cc",
		"speech_tools/grammar/wfst/wfst_transduce.cc",
		"speech_tools/grammar/wfst/kkcompile.cc",
		"speech_tools/grammar/wfst/wfst_aux.cc",
		"speech_tools/grammar/wfst/ltscompile.cc",
		"speech_tools/grammar/wfst/rgcompile.cc",
		"speech_tools/grammar/wfst/tlcompile.cc",
		"speech_tools/grammar/wfst/wfst_train.cc"
		])
	
	my_module.add_src_file([
		"speech_tools/grammar/ngram/lattice_t.cc",
		"speech_tools/grammar/ngram/EST_Ngrammar.cc",
		"speech_tools/grammar/ngram/ngrammar_io.cc",
		"speech_tools/grammar/ngram/ngrammar_aux.cc",
		"speech_tools/grammar/ngram/ngrammar_utils.cc",
		"speech_tools/grammar/ngram/EST_lattice.cc",
		"speech_tools/grammar/ngram/EST_lattice_io.cc",
		"speech_tools/grammar/ngram/freqsmooth.cc",
		"speech_tools/grammar/ngram/EST_PST.cc"
		])
	
	return my_module
