#!/usr/bin/env python

import rospy
from dynamixel_msgs.msg import JointState
from dynamixel_msgs.msg import MotorStateList
from keyboard.msg import Key
from std_msgs.msg import Float64

global positions
global button
global edit
global file
global name
positions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
file = None
button = 0
edit = 0
name = ""

# call back function for the keyboard/key topic subscribe
def keyboard_capture(data):
	global button
	global edit
	global file
	button = data.code

	#help
	if button == 104:
		print "motion saver v1.0"
		print "- n = create a new motion file"
		print "- e = edit a motion file"
		print "- c = save and exit editting a motion file"
		print "- h = help"
		
	# press on "n" to create a new motion file
	if button == 110 and edit !=1:
		name = ""
		name = raw_input("New motion name: ")
		name = "src/jimmy/motions/" + name + ".txt"
		file = open(name,"w")
		file.close()
		print "new motion file is created"
		button = 0
		
	elif button == 110 and edit == 1:
		print "you need to complete editing the previous motion file first - in order to do it press c"
	
	# press on "e" to edit a new motion file
	if button == 101 and edit !=1:
		name = ""
		name = raw_input("What motion do you want to edit?: ")
		name = "src/jimmy/motions/" + name + ".txt"
		file = open(name,"a")
		print "motion file is opened for editting"
		edit = 1
		button = 0
		
	elif button == 101 and edit == 1:
		print "you need to complete editing the previous motion file first - in order to do it press c"
										
	# press on "a" to save the servo positions in a motion file
	if button == 97 and edit == 1:
		#print data.motor_states[0].position
		new_line = ""
		for i in range(0, 20):
			new_line = new_line + str(positions[i]) + ","
				
		# ask user the delay time between motion steps/frames - add it to the end of each line
		delay = raw_input("delay(seconds):")
		new_line = new_line + str(delay)
		new_line = new_line + "\n"
		file.write(new_line)
		print "new motion is added"
		button = 0
										
	# press on "c" to exit a motion file
	if button == 99 and edit == 1:
		name = ""
		file.close()
		print "file is closed"
		edit = 0
		button = 0
										
def right_shoulder_callback(data):
	global positions
	positions[0] = data.current_pos

def left_shoulder_callback(data):
	global positions
	positions[1] = data.current_pos						
										
def right_elbow_callback(data):
	global positions
	positions[2] = data.current_pos

def left_elbow_callback(data):
	global positions
	positions[3] = data.current_pos
										
def right_hand_callback(data):
	global positions
	positions[4] = data.current_pos

def left_hand_callback(data):
	global positions
	positions[5] = data.current_pos
										
def right_hip_turn_callback(data):
	global positions
	positions[6] = data.current_pos

def left_hip_turn_callback(data):
	global positions
	positions[7] = data.current_pos

def right_hip_shake_callback(data):
	global positions
	positions[8] = data.current_pos

def left_hip_shake_callback(data):
	global positions
	positions[9] = data.current_pos
										
def right_hip_bend_callback(data):
	global positions
	positions[10] = data.current_pos

def left_hip_bend_callback(data):
	global positions
	positions[11] = data.current_pos
										
def right_knee_callback(data):
	global positions
	positions[12] = data.current_pos

def left_knee_callback(data):
	global positions
	positions[13] = data.current_pos
										
def right_ankle_callback(data):
	global positions
	positions[14] = data.current_pos

def left_ankle_callback(data):
	global positions
	positions[15] = data.current_pos
										
def right_foot_callback(data):
	global positions
	positions[16] = data.current_pos

def left_foot_callback(data):
	global positions
	positions[17] = data.current_pos
										
def neck_callback(data):
	global positions
	positions[18] = data.current_pos

def head_callback(data):
	global positions
	positions[19] = data.current_pos

def motion_control():
	rospy.init_node('motion_saver', anonymous=True)
	#rospy.Subscriber('/motor_states/pan_tilt_port', MotorStateList, motion_save)
	rospy.Subscriber('/keyboard/keydown', Key, keyboard_capture)
	
	#callback funtion calls for the robot joints states
	rospy.Subscriber('/right_shoulder_controller/state', JointState, right_shoulder_callback)		
	rospy.Subscriber('/left_shoulder_controller/state', JointState, left_shoulder_callback)	
	rospy.Subscriber('/right_elbow_controller/state', JointState, right_elbow_callback)
	rospy.Subscriber('/left_elbow_controller/state', JointState, left_elbow_callback)
	rospy.Subscriber('/right_hand_controller/state', JointState, right_hand_callback)
	rospy.Subscriber('/left_hand_controller/state', JointState, left_hand_callback)
	rospy.Subscriber('/right_hip_turn_controller/state', JointState, right_hip_turn_callback)
	rospy.Subscriber('/left_hip_turn_controller/state', JointState, left_hip_turn_callback)
	rospy.Subscriber('/right_hip_shake_controller/state', JointState, right_hip_shake_callback)
	rospy.Subscriber('/left_hip_shake_controller/state', JointState, left_hip_shake_callback)
	rospy.Subscriber('/right_hip_bend_controller/state', JointState, right_hip_bend_callback)
	rospy.Subscriber('/left_hip_bend_controller/state', JointState, left_hip_bend_callback)
	rospy.Subscriber('/right_knee_controller/state', JointState, right_knee_callback)
	rospy.Subscriber('/left_knee_controller/state', JointState, left_knee_callback)
	rospy.Subscriber('/right_ankle_controller/state', JointState, right_ankle_callback)
	rospy.Subscriber('/left_ankle_controller/state', JointState, left_ankle_callback)
	rospy.Subscriber('/right_foot_controller/state', JointState, right_foot_callback)
	rospy.Subscriber('/left_foot_controller/state', JointState, left_foot_callback)									
	rospy.Subscriber('/neck_controller/state', JointState, neck_callback)
	rospy.Subscriber('/head_controller/state', JointState, head_callback)
										
	rate = rospy.Rate(30)
	rospy.spin()
	
if __name__ == '__main__':
	try:
		motion_control()
	except rospy.ROSInterruptException:
		pass