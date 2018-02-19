#!/usr/bin/env python
import rospy
import os
import time
from std_msgs.msg import String
import std_srvs.srv 
import rosserial_arduino.srv

pub = rospy.Publisher('/play_motion', String, queue_size=1)
stop = rospy.ServiceProxy('/recognizer/stop', std_srvs.srv.Empty())
start = rospy.ServiceProxy('/recognizer/start', std_srvs.srv.Empty())
lightserv = rospy.ServiceProxy('/mouth', rosserial_arduino.srv.Test())

def callback(data):
    print data.data
    homedir = os.environ['HOME']
    filepath = homedir + "/catkin_ws/src/jimmy/voices/"
    hi_file = os.path.join(filepath, 'jimmy_hi.mp3')
    if data.data == "jimmy":
        stop()
	pub.publish("nod")

    elif data.data == "hi":
	stop()
        pub.publish("stand_hello")

    lightserv("Talk")
    os.system("mpg321 " + hi_file)
    lightserv("StopTalk")
    time.sleep(3)
    lightserv("Talk")
    os.system("mpg321 " + os.path.join(filepath, 'game_or_talk.mp3'))
    lightserv("StopTalk")
    
def init_jimmy():
    rospy.init_node('init_jimmy', anonymous=True)
    rospy.Subscriber("/recognizer/output", String, callback)
    start()
    rospy.spin()

if __name__ == '__main__':
    init_jimmy()
