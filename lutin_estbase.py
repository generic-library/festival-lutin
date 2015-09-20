#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os

def get_desc():
	return "festival TTS engine"

def create(target):
	myModule = module.Module(__file__, 'estbase', 'LIBRARY')
	myModule.add_src_file([
		"speech_tools/rxp/charset.c",
		"speech_tools/rxp/dtd.c",
		"speech_tools/rxp/string16.c",
		"speech_tools/rxp/url.c",
		"speech_tools/rxp/ctype16.c",
		"speech_tools/rxp/input.c",
		"speech_tools/rxp/stdio16.c",
		"speech_tools/rxp/system.c",
		"speech_tools/rxp/xmlparser.c"
		])
	
	myModule.add_export_path(os.path.join(tools.get_current_path(__file__), "speech_tools/include"))
	myModule.add_export_path(os.path.join(tools.get_current_path(__file__), "speech_tools/include/rxp"))
	myModule.compile_flags('c', "-DCHAR_SIZE=8")
	
	
	myModule.add_src_file([
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
	myModule.compile_flags('c++', "-fno-implicit-templates")
	myModule.compile_flags('c++', "-DSUPPORT_ALSALINUX")
	
	myModule.add_src_file([
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
	myModule.compile_flags('c++', "-DINSTANTIATE_TEMPLATES")
	myModule.compile_flags('c++', "-DFTNAME='Festival Speech Tools Library'")
	myModule.compile_flags('c++', "-DFTLIBDIRC='" + tools.get_current_path(__file__) + "/festival/lib '")
	myModule.compile_flags('c++', "-DFTVERSION='2.4'")
	myModule.compile_flags('c++', "-DFTSTATE='release'")
	myModule.compile_flags('c++', "-DFTDATE='December 2014'")
	myModule.compile_flags('c++', "-DFTSTATE='release'")
	myModule.compile_flags('c++', '-DFTOSTYPE=\\"unknown_DebianGNULinux\\"')
	
	myModule.add_src_file([
		"speech_tools/base_class/EST_UList.cc",
		"speech_tools/base_class/EST_Option.cc",
		"speech_tools/base_class/EST_StringTrie.cc",
		"speech_tools/base_class/EST_Token.cc",
		"speech_tools/base_class/vec_mat_aux.cc",
		"speech_tools/base_class/EST_Pathname_unix.cc",
		"speech_tools/base_class/THash_aux.cc",
		"speech_tools/base_class/EST_FMatrix.cc",
		"speech_tools/base_class/EST_Complex.cc",
		"speech_tools/base_class/EST_Val.cc",
		"speech_tools/base_class/EST_matrix_support.cc",
		"speech_tools/base_class/rateconv.cc",
		"speech_tools/base_class/EST_IMatrix.cc",
		"speech_tools/base_class/EST_SMatrix.cc",
		"speech_tools/base_class/EST_DMatrix.cc",
		"speech_tools/base_class/vec_mat_aux_d.cc",
		"speech_tools/base_class/EST_FeatureData.cc",
		"speech_tools/base_class/EST_slist_aux.cc",
		"speech_tools/base_class/EST_svec_aux.cc",
		"speech_tools/base_class/EST_ilist_aux.cc",
		"speech_tools/base_class/EST_features_aux.cc",
		"speech_tools/base_class/EST_features_io.cc",
		"speech_tools/base_class/vec_mat_aux_i.cc",
		"speech_tools/base_class/EST_Featured.cc",
		"speech_tools/base_class/EST_Features.cc",
		])
	
	myModule.add_src_file([
		"speech_tools/base_class/inst_tmpl/list_i_t.cc",
		"speech_tools/base_class/inst_tmpl/list_si_t.cc",
		"speech_tools/base_class/inst_tmpl/list_f_t.cc",
		"speech_tools/base_class/inst_tmpl/list_d_t.cc",
		"speech_tools/base_class/inst_tmpl/list_c_t.cc",
		"speech_tools/base_class/inst_tmpl/list_s_t.cc",
		"speech_tools/base_class/inst_tmpl/list_val_t.cc",
		"speech_tools/base_class/inst_tmpl/list_li_t.cc",
		"speech_tools/base_class/inst_tmpl/list_vs_t.cc",
		"speech_tools/base_class/inst_tmpl/list_vi_t.cc",
		"speech_tools/base_class/inst_tmpl/matrix_i_t.cc",
		"speech_tools/base_class/inst_tmpl/matrix_si_t.cc",
		"speech_tools/base_class/inst_tmpl/matrix_f_t.cc",
		"speech_tools/base_class/inst_tmpl/matrix_d_t.cc",
		"speech_tools/base_class/inst_tmpl/matrix_s_t.cc",
		"speech_tools/base_class/inst_tmpl/matrix_val_t.cc",
		"speech_tools/base_class/inst_tmpl/vector_i_t.cc",
		"speech_tools/base_class/inst_tmpl/vector_si_t.cc",
		"speech_tools/base_class/inst_tmpl/vector_f_t.cc",
		"speech_tools/base_class/inst_tmpl/vector_d_t.cc",
		"speech_tools/base_class/inst_tmpl/vector_c_t.cc",
		"speech_tools/base_class/inst_tmpl/vector_s_t.cc",
		"speech_tools/base_class/inst_tmpl/vector_val_t.cc",
		"speech_tools/base_class/inst_tmpl/vector_ls_t.cc",
		"speech_tools/base_class/inst_tmpl/vector_fvector_t.cc",
		"speech_tools/base_class/inst_tmpl/vector_fmatrix_t.cc",
		"speech_tools/base_class/inst_tmpl/vector_dvector_t.cc",
		"speech_tools/base_class/inst_tmpl/vector_dmatrix_t.cc",
		"speech_tools/base_class/inst_tmpl/kvl_fi_t.cc",
		"speech_tools/base_class/inst_tmpl/kvl_ii_t.cc",
		"speech_tools/base_class/inst_tmpl/kvl_sd_t.cc",
		"speech_tools/base_class/inst_tmpl/kvl_sf_t.cc",
		"speech_tools/base_class/inst_tmpl/kvl_ss_t.cc",
		"speech_tools/base_class/inst_tmpl/kvl_si_t.cc",
		"speech_tools/base_class/inst_tmpl/kvl_sv_t.cc",
		"speech_tools/base_class/inst_tmpl/kvl_rs_t.cc",
		"speech_tools/base_class/inst_tmpl/kvl_vpi_t.cc",
		"speech_tools/base_class/inst_tmpl/hash_fi_t.cc",
		"speech_tools/base_class/inst_tmpl/hash_ii_t.cc",
		"speech_tools/base_class/inst_tmpl/hash_sd_t.cc",
		"speech_tools/base_class/inst_tmpl/hash_sf_t.cc",
		"speech_tools/base_class/inst_tmpl/hash_ss_t.cc",
		"speech_tools/base_class/inst_tmpl/hash_si_t.cc",
		"speech_tools/base_class/inst_tmpl/hash_sv_t.cc",
		"speech_tools/base_class/inst_tmpl/hash_iv_t.cc",
		"speech_tools/base_class/inst_tmpl/hash_sfmp_t.cc",
		"speech_tools/base_class/inst_tmpl/hash_srp.cc",
		"speech_tools/base_class/inst_tmpl/tbuffer_t.cc",
		"speech_tools/base_class/inst_tmpl/deq_s_t.cc",
		"speech_tools/base_class/inst_tmpl/deq_i_t.cc"
		])
	
	myModule.add_src_file([
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
		"speech_tools/ling_class/EST_FeatureFunctionContext.cc",
	
	myModule.compile_flags('c++', "-DINCLUDE_XML_FORMATS")
	
	return myModule

