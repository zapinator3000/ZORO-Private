#!/usr/bin/python
import os
import time
input("Press enter")
trials=15
for i in range(1,trials+1):
	print(str(i)+":")
	os.system("cp /root/GEM5/DRAMSim3_mods/dramsim3_wrapper_"+str(i)+".cc /root/GEM5/gem5_modified/src/mem/dramsim3_wrapper.cc")
#	input("...")
	os.system("./compile_gem5.sh")
	os.system("./run_gem5.sh")
#	input("...")
	os.system("cp m5out/dramsim3.json results/dramsim3_"+str(i)+".json")
	os.system("cp m5out/dramsim3.txt results/dramsim3_"+str(i)+".txt")
#	input("Done")
