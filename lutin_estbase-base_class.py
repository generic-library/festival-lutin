#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os

def get_desc():
	return "festival TTS engine"

def create(target):
	my_module = module.Module(__file__, 'estbase-base_class', 'LIBRARY')
	
	my_module.add_module_depend(['eststring'])
	
	my_module.add_export_path(os.path.join(tools.get_current_path(__file__), "speech_tools/include"))
	my_module.compile_flags('c++', "-fno-implicit-templates")
	my_module.add_src_file([
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
	
	my_module.add_src_file([
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
	
	my_module.compile_flags('c++', "-DINSTANTIATE_TEMPLATES")
	
	return my_module

