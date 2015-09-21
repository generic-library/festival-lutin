#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os

def get_desc():
	return "festival TTS engine"

def create(target):
	my_module = module.Module(__file__, 'estbase-ling_class', 'LIBRARY')
	
	my_module.add_module_depend(['eststring', 'estbase-base_class', 'estools-stats', 'estbase-rxp'])
	
	my_module.add_export_path(os.path.join(tools.get_current_path(__file__), "speech_tools/include"))
	my_module.compile_flags('c++', "-fno-implicit-templates")
	
	my_module.add_src_file([
		"speech_tools/ling_class/EST_Item.cc",
		"speech_tools/ling_class/EST_Item_Content.cc",
		"speech_tools/ling_class/item_aux.cc",
		"speech_tools/ling_class/EST_relation_aux.cc",
		"speech_tools/ling_class/EST_relation_track.cc",
		"speech_tools/ling_class/relation_io.cc",
		"speech_tools/ling_class/EST_relation_compare.cc",
		"speech_tools/ling_class/standard_feature_functions.cc",
		"speech_tools/ling_class/EST_Relation_mls.cc",
		"speech_tools/ling_class/EST_item_aux.cc",
		"speech_tools/ling_class/EST_item_content_aux.cc",
		"speech_tools/ling_class/EST_Relation.cc",
		"speech_tools/ling_class/EST_UtteranceFile.cc",
		"speech_tools/ling_class/genxml.cc",
		"speech_tools/ling_class/EST_utterance_aux.cc",
		"speech_tools/ling_class/ling_class_init.cc",
		"speech_tools/ling_class/ling_t.cc",
		"speech_tools/ling_class/EST_Utterance.cc",
		"speech_tools/ling_class/item_feats.cc",
		"speech_tools/ling_class/apml.cc",
		"speech_tools/ling_class/solexml.cc",
		"speech_tools/ling_class/EST_FeatureFunctionPackage.cc",
		"speech_tools/ling_class/EST_FeatureFunctionContext.cc"
		])
	
	my_module.compile_flags('c++', "-DINCLUDE_XML_FORMATS")
	my_module.compile_flags('c++', '-DESTLIBDIR=\\"~/festival_data\\"')
	my_module.compile_flags('c++', "-DINSTANTIATE_TEMPLATES")
	
	return my_module

