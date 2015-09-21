#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os

def get_desc():
	return "festival TTS engine"

def create(target):
	my_module = module.Module(__file__, 'estools', 'LIBRARY')
	"""
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
	my_module.add_export_path(os.path.join(tools.get_current_path(__file__), "speech_tools/include/rxp"))
	my_module.compile_flags('c++', "-fno-implicit-templates")
	my_module.compile_flags('c++', "-DINSTANTIATE_TEMPLATES")
	my_module.compile_flags('c', "-DSUPPORT_EDITLINE")
	
	my_module.add_src_file([
		"speech_tools/speech_class/EST_Wave.cc",
		"speech_tools/speech_class/EST_track_aux.cc",
		"speech_tools/speech_class/EST_wave_temp.cc",
		"speech_tools/speech_class/EST_wave_cuts.cc",
		"speech_tools/speech_class/ssff.cc",
		"speech_tools/speech_class/esps_io.cc",
		"speech_tools/speech_class/esps_utils.cc",
		"speech_tools/speech_class/EST_wave_io.cc",
		"speech_tools/speech_class/EST_wave_utils.cc",
		"speech_tools/speech_class/EST_TrackMap.cc",
		"speech_tools/speech_class/EST_Track.cc",
		"speech_tools/speech_class/wave_t.cc",
		"speech_tools/speech_class/track_t.cc",
		"speech_tools/speech_class/EST_wave_aux.cc",
		"speech_tools/speech_class/EST_TrackFile.cc",
		"speech_tools/speech_class/EST_WaveFile.cc"
		])
	
	my_module.add_src_file([
		"speech_tools/sigpr/EST_Window.cc",
		"speech_tools/sigpr/delta.cc",
		"speech_tools/sigpr/filter.cc",
		"speech_tools/sigpr/sigpr_frame.cc",
		"speech_tools/sigpr/sigpr_utt.cc",
		"speech_tools/sigpr/pitchmark.cc",
		"speech_tools/sigpr/spectrogram.cc",
		"speech_tools/sigpr/misc.cc",
		"speech_tools/sigpr/fft.cc"
		])
	
	my_module.add_src_file([
		"speech_tools/sigpr/pda/pcb_smoother.cc",
		"speech_tools/sigpr/pda/smooth_pda.cc",
		"speech_tools/sigpr/pda/pda.cc",
		"speech_tools/sigpr/pda/srpd1.3.cc"
		])
	
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
	
	my_module.add_src_file([
		"speech_tools/intonation/tilt/tilt_analysis.cc",
		"speech_tools/intonation/tilt/tilt_synthesis.cc",
		"speech_tools/intonation/tilt/tilt_utils.cc"
		])
	"""
	return my_module
