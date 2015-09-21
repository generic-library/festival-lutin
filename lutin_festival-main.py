#!/usr/bin/python
import lutin.module as module
import lutin.tools as tools
import os

def get_desc():
	return "festival TTS engine"

def create(target):
	my_module = module.Module(__file__, 'festival-main', 'BINARY')
	
	my_module.add_module_depend(['festival'])
	
	my_module.add_src_file([
		"festival/src/main/festival_main.cc"
		])
	
	return my_module

"""
gcc -O3 -Wall     -o festival festival_main.o   -L../../src/lib -lFestival -L../../../speech_tools/lib -lestools -L../../../speech_tools/lib -lestbase -L../../../speech_tools/lib -leststring  -lncurses -lasound   -ldl -lncurses -lm  -lstdc++ 
gcc -c -fno-implicit-templates -O3 -Wall -I../../src/include -I../../../speech_tools/include festival_client.cc
gcc -O3 -Wall     -o festival_client festival_client.o   -L../../src/lib -lFestival -L../../../speech_tools/lib -lestools -L../../../speech_tools/lib -lestbase -L../../../speech_tools/lib -leststring  -lncurses -lasound   -ldl -lncurses -lm  -lstdc++ 
gcc -c -fno-implicit-templates -O3 -Wall -I../../src/include -I../../../speech_tools/include audsp.cc
gcc -O3 -Wall     -o ../../lib/etc/unknown_DebianGNULinux/audsp audsp.o   -L../../src/lib -lFestival -L../../../speech_tools/lib -lestools -L../../../speech_tools/lib -lestbase -L../../../speech_tools/lib -leststring  -lncurses -lasound   -ldl -lncurses -lm  -lstdc++ 
"""
