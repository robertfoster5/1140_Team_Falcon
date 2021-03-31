import time
import simpy
import simpy.rt
from c_time import mil_tim

#def clock(env,mil):
	#start = time.perf_counter()
	#yield env.timeout(1)
	#end = time.perf_counter()
	#print('Duration of one simulation time unit: %.2fs' % (end - start))
	

def main(args):
	env = simpy.rt.RealtimeEnvironment(factor=1)
	tim = mil_tim(env)
	
	env.run(until=999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
	
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
