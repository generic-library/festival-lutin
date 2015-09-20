

$ cd ../speech_tools/
[ ALD-1354-DE : edupin ](git:master)~/dev/speech_tools
$ make
Making in directory ./siod ...
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_EDITLINE -I../include slib.cc
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_EDITLINE -I../include slib_core.cc
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_EDITLINE -I../include slib_doc.cc
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_EDITLINE -I../include slib_file.cc
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_EDITLINE -I../include slib_format.cc
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_EDITLINE -I../include slib_list.cc
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_EDITLINE -I../include slib_math.cc
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_EDITLINE -I../include slib_sys.cc
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_EDITLINE -I../include slib_server.cc
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_EDITLINE -I../include slib_str.cc
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_EDITLINE -I../include slib_xtr.cc
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_EDITLINE -I../include slib_repl.cc
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_EDITLINE -I../include slib_python.cc
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_EDITLINE -I../include io.cc
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_EDITLINE -I../include trace.cc
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_EDITLINE -I../include -DINSTANTIATE_TEMPLATES siod.cc
gcc -c -fno-implicit-templates -O3 -Wall -DSUPPORT_EDITLINE -I../include -DINSTANTIATE_TEMPLATES siod_est.cc
gcc -c -O3 -Wall -DSUPPORT_EDITLINE -I../include siodeditline.c
gcc -c -O3 -Wall -DSUPPORT_EDITLINE -I../include el_complete.c
gcc -c -O3 -Wall -DSUPPORT_EDITLINE -I../include editline.c
gcc -c -O3 -Wall -DSUPPORT_EDITLINE -I../include el_sys_unix.c
Update library estools
a - slib.o
a - slib_core.o
a - slib_doc.o
a - slib_file.o
a - slib_format.o
a - slib_list.o
a - slib_math.o
a - slib_sys.o
a - slib_server.o
a - slib_str.o
a - slib_xtr.o
a - slib_repl.o
a - slib_python.o
a - io.o
a - trace.o
a - siod.o
a - siod_est.o
a - siodeditline.o
a - el_complete.o
a - editline.o
a - el_sys_unix.o



Making in directory ./speech_class ...
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_Wave.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_track_aux.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_wave_temp.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_wave_cuts.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include ssff.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include esps_io.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include esps_utils.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_wave_io.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_wave_utils.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include -DINSTANTIATE_TEMPLATES EST_TrackMap.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include -DINSTANTIATE_TEMPLATES EST_Track.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include -DINSTANTIATE_TEMPLATES wave_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include -DINSTANTIATE_TEMPLATES track_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include -DINSTANTIATE_TEMPLATES EST_wave_aux.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include -DINSTANTIATE_TEMPLATES EST_TrackFile.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include -DINSTANTIATE_TEMPLATES EST_WaveFile.cc
look at library estools
a - EST_Wave.o
a - EST_track_aux.o
a - EST_wave_temp.o
a - EST_wave_cuts.o
a - ssff.o
a - esps_io.o
a - esps_utils.o
a - EST_wave_io.o
a - EST_wave_utils.o
a - EST_TrackMap.o
a - EST_Track.o
a - wave_t.o
a - track_t.o
a - EST_wave_aux.o
a - EST_TrackFile.o
a - EST_WaveFile.o



Making in directory ./sigpr ...
gcc -c -fno-implicit-templates -O3 -Wall -I../include -DINSTANTIATE_TEMPLATES EST_Window.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include delta.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include filter.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include sigpr_frame.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include sigpr_utt.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include pitchmark.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include spectrogram.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include misc.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include fft.cc
look at library estools
a - EST_Window.o
a - delta.o
a - filter.o
a - sigpr_frame.o
a - sigpr_utt.o
a - pitchmark.o
a - spectrogram.o
a - misc.o
a - fft.o
look at library eststring



Making in directory sigpr/pda ...
gcc -c -fno-implicit-templates -O3 -Wall -I../../include pcb_smoother.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include smooth_pda.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include pda.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include srpd1.3.cc
look at library estools
a - pcb_smoother.o
a - smooth_pda.o
a - pda.o
a - srpd1.3.o
look at library eststring




Making in directory ./stats ...
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_cluster.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_multistats.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include confusion.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_Discrete.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_DProbDist.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_ols.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include EST_viterbi.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../include -DINSTANTIATE_TEMPLATES dynamic_program.cc
look at library estools
a - EST_cluster.o
a - EST_multistats.o
a - confusion.o
a - EST_Discrete.o
a - EST_DProbDist.o
a - EST_ols.o
a - EST_viterbi.o
a - dynamic_program.o
look at library eststring



Making in directory stats/wagon ...
gcc -c -fno-implicit-templates -O3 -Wall -I../../include dlist.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include wagon_aux.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include wagonint.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES wagon.cc
Update library estools
a - dlist.o
a - wagon_aux.o
a - wagonint.o
a - wagon.o



look at library eststring
Making in directory stats/kalman_filter ...
gcc -c -fno-implicit-templates -O3 -Wall -I../../include EST_kalman.cc
Update library estools
a - EST_kalman.o




Making in directory ./grammar ...
Making in directory grammar/scfg ...
making dependencies -- EST_SCFG.cc EST_SCFG_inout.cc EST_SCFG_Chart.cc 
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES EST_SCFG.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES EST_SCFG_inout.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include EST_SCFG_Chart.cc
Update library estools
a - EST_SCFG.o
a - EST_SCFG_inout.o
a - EST_SCFG_Chart.o




Making in directory grammar/wfst ...
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES EST_WFST.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES wfst_regex.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES wfst_ops.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES wfst_transduce.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES kkcompile.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include wfst_aux.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include ltscompile.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include rgcompile.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include tlcompile.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include wfst_train.cc
Update library estools
a - EST_WFST.o
a - wfst_regex.o
a - wfst_ops.o
a - wfst_transduce.o
a - kkcompile.o
a - wfst_aux.o
a - ltscompile.o
a - rgcompile.o
a - tlcompile.o
a - wfst_train.o




Making in directory grammar/ngram ...
gcc -c -fno-implicit-templates -O3 -Wall -I../../include -DINSTANTIATE_TEMPLATES lattice_t.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include EST_Ngrammar.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include ngrammar_io.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include ngrammar_aux.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include ngrammar_utils.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include EST_lattice.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include EST_lattice_io.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include freqsmooth.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include EST_PST.cc
Update library estools
a - lattice_t.o
a - EST_Ngrammar.o
a - ngrammar_io.o
a - ngrammar_aux.o
a - ngrammar_utils.o
a - EST_lattice.o
a - EST_lattice_io.o
a - freqsmooth.o
a - EST_PST.o


Making in directory ./intonation ...
Making in directory intonation/tilt ...
gcc -c -fno-implicit-templates -O3 -Wall -I../../include tilt_analysis.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include tilt_synthesis.cc
gcc -c -fno-implicit-templates -O3 -Wall -I../../include tilt_utils.cc
Update library estools
a - tilt_analysis.o
a - tilt_synthesis.o
a - tilt_utils.o
