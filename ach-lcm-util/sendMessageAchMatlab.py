'''
Author: alexc89@mit.edu
SendMessageAchMatlab
Used to multicast Hubo's status on LCM.  It will take the information received on ACH and convert it to LCM.  This is needed for live visualization.

'''

import lcm
import time
import ach
import hubo_ach as ha
import time
from ctypes import *

#Import LCM Messages
from lcmtypes import lcmt_hubo2state as lcmt





#Message Conversion
def convertLCM_Matlab(x):
    msg = lcmt.lcmt_hubo2state()
    msg.timestamp =  time.time()
    
    #Baselink state not included
    msg.NeckYaw = x.joint[ha.NKY].pos
    msg.NeckYawdot = x.joint[ha.NKY].vel
#
#    msg.HNP = x.joint[ha.HNP].pos
#    msg.HNPdot = x.joint[ha.HNP].vel
#
#    msg.HNR = x.joint[ha.HNR].pos
#    msg.HNRdot = x.joint[ha.HNR].vel
#
    msg.LeftShoulderPitch = x.joint[ha.LSP].pos
    msg.LeftShoulderPitchdot = x.joint[ha.LSP].vel

    msg.LeftShoulderRoll = x.joint[ha.LSR].pos
    msg.LeftShoulderRolldot = x.joint[ha.LSR].vel

    msg.LeftShoulderYaw = x.joint[ha.LSY].pos
    msg.LeftShoudlerYawdot = x.joint[ha.LSY].vel

    msg.LeftElbowPitch = x.joint[ha.LEB].pos
    msg.LeftElbowPitchdot = x.joint[ha.LEB].vel

    msg.LeftWristYaw = x.joint[ha.LWY].pos
    msg.LeftWristYawdot = x.joint[ha.LWY].vel

    msg.LeftWristPitch = x.joint[ha.LWP].pos
    msg.LeftWristPitchdot = x.joint[ha.LWP].vel

    msg.RightShoulderPitch = x.joint[ha.RSP].pos
    msg.RightShoulderPitchdot = x.joint[ha.RSP].vel

    msg.RightShoulderRoll = x.joint[ha.RSR].pos
    msg.RSRdot = x.joint[ha.RSR].vel

    msg.RightShoulderYaw = x.joint[ha.RSY].pos
    msg.RigthShoulderYawdot = x.joint[ha.RSY].vel

    msg.RightElbowPitch = x.joint[ha.REB].pos
    msg.RightElbowPitchdot = x.joint[ha.REB].vel

    msg.RightWristYaw = x.joint[ha.RWY].pos
    msg.RightWristYawdot = x.joint[ha.RWY].vel
 
    msg.RightWristPitch = x.joint[ha.RWP].pos
    msg.RightWristPitchdot = x.joint[ha.RWP].vel

    msg.LeftFinger1 = x.joint[ha.LF1].pos
    msg.LeftFinger1dot = x.joint[ha.LF1].vel

    msg.LeftFinger2 = x.joint[ha.LF2].pos
    msg.LeftFinger2dot = x.joint[ha.LF2].vel

    msg.LeftFinger3 = x.joint[ha.LF3].pos
    msg.LeftFinger3dot = x.joint[ha.LF3].vel

    msg.LeftFinger4 = x.joint[ha.LF4].pos
    msg.LeftFinger4dot = x.joint[ha.LF4].vel

    msg.LeftFinger5 = x.joint[ha.LF5].pos
    msg.LeftFinger5dot = x.joint[ha.LF5].vel

    msg.RightFinger1 = x.joint[ha.RF1].pos
    msg.RightFinger1dot = x.joint[ha.RF1].vel

    msg.RightFinger2 = x.joint[ha.RF2].pos
    msg.RightFinger2dot = x.joint[ha.RF2].vel

    msg.RightFinger3 = x.joint[ha.RF3].pos
    msg.RightFinger3dot = x.joint[ha.RF3].vel

    msg.RightFinger4 = x.joint[ha.RF4].pos
    msg.RightFinger4dot = x.joint[ha.RF4].vel

    msg.RightFinger5 = x.joint[ha.RF5].pos
    msg.RightFinger5dot = x.joint[ha.RF5].vel

    msg.TrunkYaw = x.joint[ha.WST].pos
    msg.TrunkYawdot = x.joint[ha.WST].vel


    msg.LeftHipYaw = x.joint[ha.LHY].pos
    msg.LeftHYdot = x.joint[ha.LHY].vel

    msg.LeftHipRoll = x.joint[ha.LHR].pos
    msg.LeftHipRolldot = x.joint[ha.LHR].vel

    msg.LeftHipPitch = x.joint[ha.LHP].pos
    msg.LeftHipPitchdot = x.joint[ha.LHP].vel

    msg.LeftKneePitch = x.joint[ha.LKN].pos
    msg.LeftKneePitchdot = x.joint[ha.LKN].vel

    msg.LeftAnklePitch = x.joint[ha.LAP].pos
    msg.LeftAnklePitchdot = x.joint[ha.LAP].vel

    msg.LeftAnkleRoll = x.joint[ha.LAR].pos
    msg.LeftAnkleRolldot = x.joint[ha.LAR].vel

    msg.RightHipYaw = x.joint[ha.RHY].pos
    msg.RightHipYawdot = x.joint[ha.RHY].vel

    msg.RightHipRoll = x.joint[ha.RHR].pos
    msg.RightHipRolldot = x.joint[ha.RHR].vel

    msg.RightHipPitch = x.joint[ha.RHP].pos
    msg.RightHipPitchdot = x.joint[ha.RHP].vel

    msg.RightKneePitch = x.joint[ha.RKN].pos
    msg.RightKneePitchdot = x.joint[ha.RKN].vel

    msg.RightAnklePitch = x.joint[ha.RAP].pos
    msg.RightAnklePitchdot = x.joint[ha.RAP].vel
    msg.RightAnkleRoll = x.joint[ha.RAR].pos
    msg.RightAnkleRolldot = x.joint[ha.RAR].vel

    return msg


if __name__ == "__main__":
    #Setup ACH LCM channels
    lc = lcm.LCM("udpm://239.255.76.67:7667?ttl=2")
    #Setup ACH
    c = ach.Channel(ha.HUBO_CHAN_STATE_NAME)#HuboState
    c. flush()

    while True:  #constant Transmission        
        #Grab a frame form ACH
        state = ha.HUBO_STATE()
        [status, framesize] = c.get(state, wait=True, last=False)
        if status == ach.ACH_OK or status == ach.ACH_MISSED_FRAME:
            x =1#print "ACH grab successful" #Testing Probe 1
        else:
            raise ach.AchException( c.result_string(status))
        
        
        #ACH to LCM conversion
        msg = convertLCM_Matlab(state)
        
        #Pushout an LCM message
        lc.publish("HuboState", msg.encode())
        #Loop Delay
        time.sleep(0.01)
    #ACH LCM terminate
    c.close()
