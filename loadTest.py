from memory_profiler import memory_usage
from cpu_load_generator import load_single_core, load_all_cores, from_profile


def memory_generator(target):

    previous = memory_usage()
    print(previous)
    list1 = []
    for i in range(target*71000):
        list1.append(0)
    
    print(memory_usage())
   

def cpu_generator(target, durations, options=0, core=0):
    if options == 0:
        load_all_cores(duration_s= durations, target_load=target)
    else:
        load_single_core(core_num=core, duration_s=durations, target_load=target) 