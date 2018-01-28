#!/usr/bin/env python

import rospy
from dynamixel_msgs.msg import JointState
from std_msgs.msg import Float64

current_pos1 = 0
prev_pos1 = 0
goal_pos1 = 0
change_pos1 = 0

current_pos2 = 0
prev_pos2 = 0
goal_pos2 = 0
change_pos2 = 0

current_pos3 = 0
prev_pos3 = 0
goal_pos3 = 0
change_pos3 = 0

current_pos4 = 0
prev_pos4 = 0
goal_pos4 = 0
change_pos4 = 0

pub1 = rospy.Publisher('/left_bicep_controller/command', Float64)
pub2 = rospy.Publisher('/left_shoulder_controller/command', Float64)
pub3 = rospy.Publisher('/left_hand_controller/command', Float64)
pub4 = rospy.Publisher('/left_elbow_controller/command', Float64)

def transform_callback11(data):
	global current_pos1
	global prev_pos1
	global change_pos1
	
	if prev_pos1 == 0:
		prev_pos1 = data.current_pos
		
	current_pos1 = data.current_pos
	change_pos1 = 2 * (prev_pos1 - current_pos1)
	prev_pos1 = data.current_pos
	
def transform_callback12(data):
	global goal_pos1
	
	goal_pos1 = data.current_pos
	goal_pos1 = goal_pos1 + change_pos1
	pub1.publish(goal_pos1)
	
def transform_callback21(data):
	global current_pos2
	global prev_pos2
	global change_pos2
	
	if prev_pos2 == 0:
		prev_pos2 = data.current_pos
		
	current_pos2 = data.current_pos
	change_pos2 = 2 * (prev_pos2 - current_pos2)
	prev_pos2 = data.current_pos
	
def transform_callback22(data):
	global goal_pos2
	
	goal_pos2 = data.current_pos
	goal_pos2 = goal_pos2 + change_pos2
	pub2.publish(goal_pos2)
	
def transform_callback31(data):
	global current_pos3
	global prev_pos3
	global change_pos3
	
	if prev_pos3 == 0:
		prev_pos3 = data.current_pos
		
	current_pos3 = data.current_pos
	change_pos3 = 2 * (prev_pos3 - current_pos3)
	prev_pos3 = data.current_pos
	
def transform_callback32(data):
	global goal_pos3
	
	goal_pos3 = data.current_pos
	goal_pos3 = goal_pos3 + change_pos3
	
	pub3.publish(goal_pos3)

def transform_callback41(data):
	global current_pos4
	global prev_pos4
	global change_pos4
	
	if prev_pos4 == 0:
		prev_pos4 = data.current_pos
		
	current_pos4 = data.current_pos
	change_pos4 = 2 * (prev_pos4 - current_pos4)
	prev_pos4 = data.current_pos
	
def transform_callback42(data):
	global goal_pos4
	
	goal_pos4 = data.current_pos
	goal_pos4 = goal_pos4 + change_pos4
	pub4.publish(goal_pos4)
		
def dxl_control():
	rospy.init_node('dx_clone', anonymous=True)
	
	rospy.Subscriber('/right_bicep_controller/state', JointState, transform_callback11)
	rospy.Subscriber('/left_bicep_controller/state', JointState, transform_callback12)
	
	rospy.Subscriber('/right_shoulder_controller/state', JointState, transform_callback21)
	rospy.Subscriber('/left_shoulder_controller/state', JointState, transform_callback22)
	
	rospy.Subscriber('/right_hand_controller/state', JointState, transform_callback31)
	rospy.Subscriber('/left_hand_controller/state', JointState, transform_callback32)
	
	rospy.Subscriber('/right_elbow_controller/state', JointState, transform_callback41)
	rospy.Subscriber('/left_elbow_controller/state', JointState, transform_callback42)
	
	rate = rospy.Rate(30)
	rospy.spin()
	
if __name__ == '__main__':
	try:
		dxl_control()
	except rospy.ROSInterruptException:
		pass