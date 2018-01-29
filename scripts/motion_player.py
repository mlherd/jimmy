#!/usr/bin/env python

import rospy
import time
from dynamixel_msgs.msg import JointState
from std_msgs.msg import Float64
from std_msgs.msg import String
import os

global in_action
in_action = 0

pub1 = rospy.Publisher('/right_shoulder_controller/command', Float64)
pub2 = rospy.Publisher('/left_shoulder_controller/command', Float64)
pub3 = rospy.Publisher('/right_elbow_controller/command', Float64)
pub4 = rospy.Publisher('/left_elbow_controller/command', Float64)
pub5 = rospy.Publisher('/right_hand_controller/command', Float64)
pub6 = rospy.Publisher('/left_hand_controller/command', Float64)
pub7 = rospy.Publisher('/right_hip_turn_controller/command', Float64)
pub8 = rospy.Publisher('/left_hip_turn_controller/command', Float64)
pub9 = rospy.Publisher('/right_hip_shake_controller/command', Float64)
pub10 = rospy.Publisher('/left_hip_shake_controller/command', Float64)
pub11 = rospy.Publisher('/right_hip_bend_controller/command', Float64)
pub12 = rospy.Publisher('/left_hip_bend_controller/command', Float64)
pub13 = rospy.Publisher('/right_knee_controller/command', Float64)
pub14 = rospy.Publisher('/left_knee_controller/command', Float64)
pub15 = rospy.Publisher('/right_ankle_controller/command', Float64)
pub16 = rospy.Publisher('/left_ankle_controller/command', Float64)
pub17 = rospy.Publisher('/right_foot_controller/command', Float64)
pub18 = rospy.Publisher('/left_foot_controller/command', Float64)
pub19 = rospy.Publisher('/neck_controller/command', Float64)
pub20 = rospy.Publisher('/head_controller/command', Float64)

def motion_play(data):
	global in_action
	if in_action == 0:
		in_action = 1
		
		homedir = os.environ['HOME']
		filepath = homedir + "/catkin_ws/src/jimmy/motions/" + data.data + ".txt"  
		
		try:
			with open(filepath) as f:
				content = f.readlines()
				# you may also want to remove whitespace characters like `\n` at the end of each line
				content = [x.strip('\n') for x in content]

				print "playing " + data.data + " motion"
				for i in range (0, len(content)):
					joint_positions = content[i].split(",")
					delay = joint_positions[20]
					del joint_positions[20]

					pub1.publish(float(joint_positions[0]))
					pub2.publish(float(joint_positions[1]))
					pub3.publish(float(joint_positions[2]))
					pub4.publish(float(joint_positions[3]))
					pub5.publish(float(joint_positions[4]))
					pub6.publish(float(joint_positions[5]))
					pub7.publish(float(joint_positions[6]))
					pub8.publish(float(joint_positions[7]))
					pub9.publish(float(joint_positions[8]))
					pub10.publish(float(joint_positions[9]))
					pub11.publish(float(joint_positions[10]))
					pub12.publish(float(joint_positions[11]))
					pub13.publish(float(joint_positions[12]))
					pub14.publish(float(joint_positions[13]))
					pub15.publish(float(joint_positions[14]))
					pub16.publish(float(joint_positions[15]))
					pub17.publish(float(joint_positions[16]))
					pub18.publish(float(joint_positions[17]))
					pub19.publish(float(joint_positions[18]))
					pub20.publish(float(joint_positions[19]))

					#delay between motions
					rospy.sleep(float(delay))
				in_action = 0
				print "motion is done"
		except:
			in_action = 0
			print "motion file doens't exist"
	else:
		print "The robot can't play this motion because it is playing another motion. Wait until the motion is done."
			
# call back function for the keyboard/key topic subscribe
def keyboard_capture(data):
	global button
	button = data.code

def motion_control():
	rospy.init_node('motion_player', anonymous=True)
	rospy.Subscriber('/play_motion', String, motion_play)
	rate = rospy.Rate(20)
	rospy.spin()
	
if __name__ == '__main__':
	try:
		motion_control()
	except rospy.ROSInterruptException:
		pass