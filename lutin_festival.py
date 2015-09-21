#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os

def get_desc():
	return "festival TTS engine"

def create(target):
	my_module = module.Module(__file__, 'festival', 'LIBRARY')
	
	#my_module.add_module_depend(['estools', 'estbase', 'eststring'])
	my_module.add_module_depend([
		'estbase-audio',
		'estbase-base_class',
		'estbase-ling_class',
		'estbase-rxp',
		'estbase-utils',
		'estools-grammar',
		'estools-intonation',
		'estools-sigpr',
		'estools-siod',
		'estools-speech_class',
		'estools-stats'
		])
	
	my_module.add_src_file([
		'festival/src/arch/festival/festival.cc',
		'festival/src/arch/festival/web.cc',
		'festival/src/arch/festival/linreg.cc',
		'festival/src/arch/festival/Phone.cc',
		'festival/src/arch/festival/wave.cc',
		'festival/src/arch/festival/tcl.cc',
		'festival/src/arch/festival/audspio.cc',
		'festival/src/arch/festival/utterance.cc',
		'festival/src/arch/festival/viterbi.cc',
		'festival/src/arch/festival/features.cc',
		'festival/src/arch/festival/wagon_interp.cc',
		'festival/src/arch/festival/wfst.cc',
		'festival/src/arch/festival/server.cc',
		'festival/src/arch/festival/client.cc',
		'festival/src/arch/festival/ngram.cc',
		'festival/src/arch/festival/ModuleDescription.cc'
		])
	
	my_module.add_src_file([
		'festival/src/modules/base/parameters.cc',
		'festival/src/modules/base/phrasify.cc',
		'festival/src/modules/base/phrinfo.cc',
		'festival/src/modules/base/postlex.cc',
		'festival/src/modules/base/word.cc',
		'festival/src/modules/base/pos.cc',
		'festival/src/modules/base/modules.cc',
		'festival/src/modules/base/ff.cc',
		'festival/src/modules/base/module_support.cc'
		])
	
	# all plugins:
	my_module.add_src_file([
		'festival/src/modules/UniSyn/us_unit.cc',
		'festival/src/modules/UniSyn/us_prosody.cc',
		'festival/src/modules/UniSyn/ps_synthesis.cc',
		'festival/src/modules/UniSyn/us_mapping.cc',
		'festival/src/modules/UniSyn/UniSyn.cc',
		'festival/src/modules/UniSyn/us_features.cc'
		])
	
	my_module.add_src_file([
		'festival/src/modules/Intonation/simple.cc',
		'festival/src/modules/Intonation/duffint.cc',
		'festival/src/modules/Intonation/int_aux.cc',
		'festival/src/modules/Intonation/gen_int.cc',
		'festival/src/modules/Intonation/int_tree.cc'
		])
	
	my_module.add_src_file([
		'festival/src/modules/UniSyn_diphone/UniSyn_diphone.cc',
		'festival/src/modules/UniSyn_diphone/us_diphone_index.cc',
		'festival/src/modules/UniSyn_diphone/us_diphone_unit.cc'
		])
	"""
	my_module.add_src_file([
		'festival/src/modules/UniSyn_phonology/UniSyn_phonology.cc',
		'festival/src/modules/UniSyn_phonology/unisyn_tilt.cc',
		'festival/src/modules/UniSyn_phonology/subword.cc',
		'festival/src/modules/UniSyn_phonology/us_duration.cc',
		'festival/src/modules/UniSyn_phonology/syllabify.cc',
		'festival/src/modules/UniSyn_phonology/mettree.cc',
		'festival/src/modules/UniSyn_phonology/us_aux.cc',
		'festival/src/modules/UniSyn_phonology/UniSyn_build.cc' # pb compiling ...
		])
	"""
	my_module.add_src_file([
		'festival/src/modules/donovan/coeffs.c',
		'festival/src/modules/donovan/donovan.cc',
		'festival/src/modules/donovan/durations.c',
		'festival/src/modules/donovan/excitation.c',
		'festival/src/modules/donovan/load_diphs.c',
		'festival/src/modules/donovan/makewav.c',
		'festival/src/modules/donovan/pitch.c',
		])
	
	my_module.add_src_file([
		'festival/src/modules/Text/text_modes.cc',
		'festival/src/modules/Text/tok_ext.cc',
		'festival/src/modules/Text/text.cc',
		'festival/src/modules/Text/token.cc',
		'festival/src/modules/Text/xxml.cc',
		'festival/src/modules/Text/token_pos.cc',
		'festival/src/modules/Text/text_aux.cc'
		])
	
	my_module.add_src_file([
		'festival/src/modules/clustergen/HTS_vocoder_me.cc', # request include : festival/src/modules/hts_engine
		'festival/src/modules/clustergen/mlsa_resynthesis.cc',
		'festival/src/modules/clustergen/simple_mlpg.cc',
		'festival/src/modules/clustergen/vc.cc',
		'festival/src/modules/clustergen/clustergen.cc'
		])
	my_module.add_export_path(os.path.join(tools.get_current_path(__file__), "festival/src/modules/hts_engine"))
	
	"""
	my_module.add_src_file([
		'festival/src/modules/diphone/di_select.cc',
		'festival/src/modules/diphone/di_pitch.cc',
		'festival/src/modules/diphone/di_io.cc',
		'festival/src/modules/diphone/oc.cc',
		'festival/src/modules/diphone/di_psola.cc',
		'festival/src/modules/diphone/di_reslpc.cc',
		'festival/src/modules/diphone/diphone.cc'
		])
	"""
	
	my_module.add_src_file([
		'festival/src/modules/Duration/duration.cc',
		'festival/src/modules/Duration/dur_aux.cc',
		'festival/src/modules/Duration/Klatt.cc'
		])
	
	my_module.add_src_file([
		'festival/src/modules/hts_engine/fest2hts_engine.cc',
		'festival/src/modules/hts_engine/HTS_audio.c',
		'festival/src/modules/hts_engine/HTS_engine.c',
		'festival/src/modules/hts_engine/HTS_engine.c',
		'festival/src/modules/hts_engine/HTS_gstream.c',
		'festival/src/modules/hts_engine/HTS_label.c',
		'festival/src/modules/hts_engine/HTS_misc.c',
		'festival/src/modules/hts_engine/HTS_model.c',
		'festival/src/modules/hts_engine/HTS_pstream.c',
		'festival/src/modules/hts_engine/HTS_sstream.c',
		#'festival/src/modules/hts_engine/HTS_vocoder.c'
		])
	
	my_module.add_src_file([
		'festival/src/modules/clunits/cldb.cc',
		'festival/src/modules/clunits/clunits.cc',
		'festival/src/modules/clunits/acost.cc',
		'festival/src/modules/clunits/cljoin.cc' # request finclude estival/src/modules/UniSyn
		])
	my_module.add_export_path(os.path.join(tools.get_current_path(__file__), "festival/src/modules/UniSyn"))
	
	my_module.add_src_file([
		'festival/src/modules/rxp/ttsxml.cc' # request include : speech_tools/include/rxp
		])
	my_module.add_export_path(os.path.join(tools.get_current_path(__file__), "speech_tools/include/rxp"))
	my_module.compile_flags('c++', "-DCHAR_SIZE=8")
	
	my_module.add_src_file([
		'festival/src/modules/Lexicon/complex.cc',
		'festival/src/modules/Lexicon/lts.cc',
		'festival/src/modules/Lexicon/lexicon.cc',
		'festival/src/modules/Lexicon/lex_ff.cc',
		'festival/src/modules/Lexicon/lex_aux.cc',
		'festival/src/modules/Lexicon/lts_rules.cc'
		])
	
	my_module.add_src_file([
		'festival/src/modules/parser/pparser.cc'
		])
	
	my_module.add_src_file([
		'festival/src/modules/MultiSyn/EST_JoinCost.cc',
		'festival/src/modules/MultiSyn/DiphoneUnitVoice.cc',
		'festival/src/modules/MultiSyn/inst_tmpl/list_itemp_t.cc',
		'festival/src/modules/MultiSyn/inst_tmpl/hash_itemp_tcdatap_t.cc',
		'festival/src/modules/MultiSyn/inst_tmpl/list_voicemodulep_t.cc',
		'festival/src/modules/MultiSyn/inst_tmpl/list_scorepair_t.cc',
		'festival/src/modules/MultiSyn/inst_tmpl/hash_s_itemlistp_t.cc',
		'festival/src/modules/MultiSyn/inst_tmpl/list_strlist_t.cc',
		'festival/src/modules/MultiSyn/inst_tmpl/list_uttp_t.cc',
		'festival/src/modules/MultiSyn/inst_tmpl/vector_jccp_t.cc',
		'festival/src/modules/MultiSyn/DiphoneBackoff.cc',
		'festival/src/modules/MultiSyn/EST_DiphoneCoverage.cc',
		'festival/src/modules/MultiSyn/EST_TargetCost.cc',
		'festival/src/modules/MultiSyn/EST_JoinCostCache.cc',
		'festival/src/modules/MultiSyn/DiphoneVoiceModule.cc',
		'festival/src/modules/MultiSyn/VoiceModuleBase.cc',
		'festival/src/modules/MultiSyn/VoiceBase.cc',
		'festival/src/modules/MultiSyn/UnitSelection.cc',
		'festival/src/modules/MultiSyn/EST_FlatTargetCost.cc',
		'festival/src/modules/MultiSyn/TargetCostRescoring.cc'
		])
	my_module.add_export_path(os.path.join(tools.get_current_path(__file__), "festival/src/modules/MultiSyn"))
	my_module.add_export_path(os.path.join(tools.get_current_path(__file__), "festival/src/modules/MultiSyn/inst_tmpl"))
	
	# load all modules
	my_module.add_src_file([
		'init_modules.cc'
		])
	my_module.add_export_path(os.path.join(tools.get_current_path(__file__), "festival/src/modules"))
	
	my_module.compile_flags('c++', "-fno-implicit-templates")
	my_module.compile_flags('c++', "-DINSTANTIATE_TEMPLATES")
	my_module.compile_flags('c++', "-DFTNAME='Festival Speech Synthesis System'")
	my_module.compile_flags('c++', "-DFTLIBDIRC='" + tools.get_current_path(__file__) + "/festival/lib '")
	my_module.compile_flags('c++', "-DFTVERSION='2.4'")
	my_module.compile_flags('c++', "-DFTSTATE='release'")
	my_module.compile_flags('c++', "-DFTDATE='December 2014'")
	my_module.compile_flags('c++', "-DFTSTATE='release'")
	my_module.compile_flags('c++', '-DFTOSTYPE=\\"unknown_DebianGNULinux\\"')
	my_module.compile_version_CC(1999)
	# TODO: copy in install folder ...
	my_module.add_export_path(os.path.join(tools.get_current_path(__file__), "festival/src/include"))
	my_module.add_export_path(os.path.join(tools.get_current_path(__file__), "speech_tools/include"))
	#my_module.add_export_path(tools.get_current_path(__file__) + "/festival/src/include")
	
	my_module.compile_version_XX(2003)
	my_module.add_export_flag('link', "-lncurses")
	my_module.add_export_flag('link', "-lasound")
	my_module.add_export_flag('link', "-ldl")
	my_module.add_export_flag('link', "-lm")
	my_module.add_export_flag('link', "-lstdc++")
	return my_module


