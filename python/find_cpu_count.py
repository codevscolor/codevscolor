import multiprocessing
import os

print (multiprocessing.cpu_count())

print (os.cpu_count())
#print (len(os.sched_getaffinity(0)))
