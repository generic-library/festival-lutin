#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os

def get_desc():
	return "festival TTS engine"

def create(target):
	myModule = module.Module(__file__, 'eststring', 'LIBRARY')
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
	myModule.compile_flags('c++', "-DCHAR_SIZE=8")
	
	
	
	
	return myModule


"""
Making in directory ./audio ...
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_ALSALINUX -I../include gen_audio.cc
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_ALSALINUX -I../include nas.cc
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_ALSALINUX -I../include esd.cc
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_ALSALINUX -I../include sun16audio.cc
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_ALSALINUX -I../include mplayer.cc
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_ALSALINUX -I../include win32audio.cc
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_ALSALINUX -I../include irixaudio.cc
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_ALSALINUX -I../include os2audio.cc
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_ALSALINUX -I../include macosxaudio.cc
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_ALSALINUX -I../include linux_sound.cc
Update library estbase
a - gen_audio.o
a - nas.o
a - esd.o
a - sun16audio.o
a - mplayer.o
a - win32audio.o
a - irixaudio.o
a - os2audio.o
a - macosxaudio.o
a - linux_sound.o
"""

"""
Making in directory ./utils ...
gcc -c -fno-implicit-templates -O3 -Wall -I../include cmd_line.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include util_io.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include filetrans.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include cmd_line_aux.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_swapping.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include -DINSTANTIATE_TEMPLATES est_file.cc
gcc -c -O3 -Wall -I../include -DESTNAME='Edinburgh Speech Tools Library' -DESTDATE='December 2014' -DESTVERSION='2.4' -DESTLIBDIRC='/home/edupin/dev/speech_tools/lib' -DESTSTATE='release' -DESTOSTYPE='unknown_DebianGNULinux' EST_cutils.c
gcc -c -O3 -Wall -I../include EST_error.c
gcc -c -O3 -Wall -I../include walloc.c
gcc -c -O3 -Wall -I../include system_specific_unix.c
Update library estbase
a - cmd_line.o
a - util_io.o
a - filetrans.o
a - cmd_line_aux.o
a - EST_swapping.o
a - est_file.o
a - EST_cutils.o
a - EST_error.o
a - walloc.o
a - system_specific_unix.o
"""


"""
Making in directory ./base_class ...
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_UList.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_Option.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_StringTrie.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_Token.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include vec_mat_aux.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_Pathname_unix.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include THash_aux.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_FMatrix.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_Complex.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_Val.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_matrix_support.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include rateconv.cc -o rateconv.o
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_IMatrix.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_SMatrix.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_DMatrix.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include vec_mat_aux_d.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_FeatureData.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_slist_aux.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_svec_aux.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_ilist_aux.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_features_aux.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_features_io.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include vec_mat_aux_i.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include -DINSTANTIATE_TEMPLATES EST_Featured.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include -DINSTANTIATE_TEMPLATES EST_Features.cc
Update library estbase
a - EST_UList.o
a - EST_Option.o
a - EST_StringTrie.o
a - EST_Token.o
a - vec_mat_aux.o
a - EST_Pathname_unix.o
a - THash_aux.o
a - EST_FMatrix.o
a - EST_Complex.o
a - EST_Val.o
a - EST_matrix_support.o
a - rateconv.o
a - EST_IMatrix.o
a - EST_SMatrix.o
a - EST_DMatrix.o
a - vec_mat_aux_d.o
a - EST_FeatureData.o
a - EST_slist_aux.o
a - EST_svec_aux.o
a - EST_ilist_aux.o
a - EST_features_aux.o
a - EST_features_io.o
a - vec_mat_aux_i.o
a - EST_Featured.o
a - EST_Features.o
"""


"""
Making in directory base_class/inst_tmpl ...
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES list_i_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES list_si_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES list_f_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES list_d_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES list_c_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES list_s_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES list_val_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES list_li_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES list_vs_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES list_vi_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES matrix_i_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES matrix_si_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES matrix_f_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES matrix_d_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES matrix_s_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES matrix_val_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES vector_i_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES vector_si_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES vector_f_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES vector_d_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES vector_c_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES vector_s_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES vector_val_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES vector_ls_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES vector_fvector_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES vector_fmatrix_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES vector_dvector_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES vector_dmatrix_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES kvl_fi_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES kvl_ii_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES kvl_sd_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES kvl_sf_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES kvl_ss_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES kvl_si_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES kvl_sv_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES kvl_rs_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES kvl_vpi_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES hash_fi_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES hash_ii_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES hash_sd_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES hash_sf_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES hash_ss_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES hash_si_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES hash_sv_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES hash_iv_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES hash_sfmp_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES hash_srp.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES tbuffer_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES deq_s_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES deq_i_t.cc
Update library estbase
a - list_i_t.o
a - list_si_t.o
a - list_f_t.o
a - list_d_t.o
a - list_c_t.o
a - list_s_t.o
a - list_val_t.o
a - list_li_t.o
a - list_vs_t.o
a - list_vi_t.o
a - matrix_i_t.o
a - matrix_si_t.o
a - matrix_f_t.o
a - matrix_d_t.o
a - matrix_s_t.o
a - matrix_val_t.o
a - vector_i_t.o
a - vector_si_t.o
a - vector_f_t.o
a - vector_d_t.o
a - vector_c_t.o
a - vector_s_t.o
a - vector_val_t.o
a - vector_ls_t.o
a - vector_fvector_t.o
a - vector_fmatrix_t.o
a - vector_dvector_t.o
a - vector_dmatrix_t.o
a - kvl_fi_t.o
a - kvl_ii_t.o
a - kvl_sd_t.o
a - kvl_sf_t.o
a - kvl_ss_t.o
a - kvl_si_t.o
a - kvl_sv_t.o
a - kvl_rs_t.o
a - kvl_vpi_t.o
a - hash_fi_t.o
a - hash_ii_t.o
a - hash_sd_t.o
a - hash_sf_t.o
a - hash_ss_t.o
a - hash_si_t.o
a - hash_sv_t.o
a - hash_iv_t.o
a - hash_sfmp_t.o
a - hash_srp.o
a - tbuffer_t.o
a - deq_s_t.o
a - deq_i_t.o
"""

"""
Making in directory ./ling_class ...
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_Item.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_Item_Content.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include item_aux.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_relation_aux.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_relation_track.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include relation_io.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_relation_compare.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include standard_feature_functions.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_Relation_mls.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_item_aux.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_item_content_aux.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_Relation.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include -DINSTANTIATE_TEMPLATES -DINCLUDE_XML_FORMATS EST_UtteranceFile.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include -DINSTANTIATE_TEMPLATES -DESTLIBDIRC='/home/edupin/dev/speech_tools/lib' genxml.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include -DINSTANTIATE_TEMPLATES -DINCLUDE_XML_FORMATS EST_utterance_aux.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include -DINSTANTIATE_TEMPLATES -DINCLUDE_XML_FORMATS ling_class_init.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include -DINSTANTIATE_TEMPLATES ling_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include -DINSTANTIATE_TEMPLATES EST_Utterance.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include -DINSTANTIATE_TEMPLATES item_feats.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include -DINSTANTIATE_TEMPLATES apml.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include -DINSTANTIATE_TEMPLATES solexml.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include -DINSTANTIATE_TEMPLATES EST_FeatureFunctionPackage.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include -DINSTANTIATE_TEMPLATES EST_FeatureFunctionContext.cc
Update library estbase
a - EST_Item.o
a - EST_Item_Content.o
a - item_aux.o
a - EST_relation_aux.o
a - EST_relation_track.o
a - relation_io.o
a - EST_relation_compare.o
a - standard_feature_functions.o
a - EST_Relation_mls.o
a - EST_item_aux.o
a - EST_item_content_aux.o
a - EST_Relation.o
a - EST_UtteranceFile.o
a - genxml.o
a - EST_utterance_aux.o
a - ling_class_init.o
a - ling_t.o
a - EST_Utterance.o
a - item_feats.o
a - apml.o
a - solexml.o
a - EST_FeatureFunctionPackage.o
a - EST_FeatureFunctionContext.o


"""