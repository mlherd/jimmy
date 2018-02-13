#!/usr/bin/env python

#import libraries and message types
import rospy
import time
from dynamixel_msgs.msg import JointState
from sensor_msgs.msg import JointState as js
from std_msgs.msg import Float64
import os

global joint_head_prev
joint_head_prev = 999
global head_current
head_current = 3.17
global head_goal
head_goal = 3.17

# define all the publishers
pub1 = rospy.Publisher('/neck_controller/command', Float64, queue_size = 10)
##pub2 = rospy.Publisher('/left_shoulder_controller/command', Float64)
##pub3 = rospy.Publisher('/right_elbow_controller/command', Float64)
##pub4 = rospy.Publisher('/left_elbow_controller/command', Float64)
##pub5 = rospy.Publisher('/right_hand_controller/command', Float64)
##pub6 = rospy.Publisher('/left_hand_controller/command', Float64)
##pub7 = rospy.Publisher('/right_hip_turn_controller/command', Float64)
##pub8 = rospy.Publisher('/left_hip_turn_controller/command', Float64)
##pub9 = rospy.Publisher('/right_hip_shake_controller/command', Float64)
##pub10 = rospy.Publisher('/left_hip_shake_controller/command', Float64)
##pub11 = rospy.Publisher('/right_hip_bend_controller/command', Float64)
##pub12 = rospy.Publisher('/left_hip_bend_controller/command', Float64)
##pub13 = rospy.Publisher('/right_knee_controller/command', Float64)
##pub14 = rospy.Publisher('/left_knee_controller/command', Float64)
##pub15 = rospy.Publisher('/right_ankle_controller/command', Float64)
##pub16 = rospy.Publisher('/left_ankle_controller/command', Float64)
##pub17 = rospy.Publisher('/right_foot_controller/command', Float64)
##pub18 = rospy.Publisher('/left_foot_controller/command', Float64)
##pub19 = rospy.Publisher('/neck_controller/command', Float64)
##pub20 = rospy.Publisher('/head_controller/command', Float64)

def get_head_current(pos):
	global head_current
	head_current = pos.current_pos

def get_set_postions(joint_pos):
	global head_current
	global joint_head_prev
	joint_positions = joint_pos.position
	if joint_head_prev != joint_positions[0]:
		joint_head_prev = joint_positions[0]
		head_goal = head_current + joint_positions[0]
		pub1.publish(head_goal)
	
def joint2motors():
	rospy.init_node('joint_mapper', anonymous=True)
	rospy.Subscriber('/neck_controller/state', JointState, get_head_current, queue_size = 10)
	rospy.Subscriber('/joint_states', js, get_set_postions, queue_size = 10)
	rate = rospy.Rate(20)
	rospy.spin()
	
if __name__ == '__main__':
	try:
		joint2motors()
	except rospy.ROSInterruptException:
		pass
