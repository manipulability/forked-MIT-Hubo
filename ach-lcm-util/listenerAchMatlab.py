'''
Author: alexc89@mit.edu
ListenerAchMatlab
Used to test if hubo state is being published on lcm across the multicast by monitoring on the of variables.  In this case, the position of the joint LSP.

'''
import lcm
import hubo_ach as ha
import time
import ach

from lcmtypes import lcmt_hubo2state



def my_handler(channel, data):
    msg = lcmt_hubo2state.lcmt_hubo2state.decode(data)
    print("   positionLSP    = %s" % str(msg.LeftShoulderPitch))
    

lc = lcm.LCM("udpm://239.255.76.67:7667?ttl=2")
subscription = lc.subscribe("HuboState", my_handler)

try:
    while True:
        lc.handle()
except KeyboardInterrupt:
    pass

lc.unsubscribe(subscription)
