#!/usr/bin/env python

# import libraries, message types, and service types
import rospy
import os
from dynamixel_controllers.srv import TorqueEnable
from dynamixel_msgs.msg import JointState
from keyboard.msg import Key
from std_msgs.msg import Float64
from std_msgs.msg import String

# global variables used in callback functions
global positions
global button
global edit
global file
global name
global all_enabled
global left_arm_enabled
global right_arm_enabled
global head_enabled
global part
global motion_counter

# initial values for global variables
motion_counter = 0
all_enabled = 1
head_enabled = 1
left_arm_enabled = 1
right_arm_enabled = 1
positions = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
file = None
button = 0
edit = 0
name = ""
part = ""

motion_pub = rospy.Publisher('play_motion', String)

# call back function for the keyboard/key topic subscribe
# h - help menu
# e - edit motion file
# n - new motion file
# c - exit motion file
# t - torque enable/disable

def keyboard_capture(data):
	global button
	global edit
	global file
	global all_enabled
	global left_arm_enabled
	global right_arm_enabled
	global head_enabled
	global motion_counter
	
	button = data.code

	#help
	if button == 104:
		os.system('cls' if os.name == 'nt' else 'clear')
		print "motion saver v1.0 help"
		print "- n = create a new motion file"
		print "- e = edit a motion file"
		print "- c = save and exit editting a motion file"
		print "- p = play a motion file"
		print "- t = turn on/off torque all servos"
		print "- y = turn on/off torque a body part"
		print "- h = help"
		name = raw_input("press enter to go back")
	
	#press on "p" to play motions
	if button == 112 and edit !=1:
		os.system('cls' if os.name == 'nt' else 'clear')
		name = ""
		name = raw_input("What motion do you want to play?: ")
		if name == "none":
			print "going back"
		else:
			motion_pub.publish(name)
		name = raw_input("press enter to go back")
		
	# press on "n" to create a new motion file
	if button == 110 and edit !=1:
		os.system('cls' if os.name == 'nt' else 'clear')
		name = ""
		name = raw_input("New motion name: ")
		homedir = os.environ['HOME']
		name = homedir + "/catkin_ws/src/jimmy/motions/" + name + ".txt"
		file = open(name,"w+")
		file.close()
		print "new motion file is created"
		name = raw_input("press enter to go back")
		button = 0
		
	elif button == 110 and edit == 1:
		os.system('cls' if os.name == 'nt' else 'clear')
		print "you need to complete editing the previous motion file first - in order to do it press c"
		name = raw_input("press enter to go back")
	
	# press on "e" to edit a new motion file
	if button == 101 and edit !=1:
		
		os.system('cls' if os.name == 'nt' else 'clear')
		
		homedir = os.environ['HOME']
		motion_directory = homedir + "/catkin_ws/src/jimmy/motions/"
		
		print "Your motions:"
		for root, dirs, files in os.walk(motion_directory):
			for f in files:
				if f.endswith(".txt"):
					print "- " + str(os.path.join(f))
			
		name = ""
		name = raw_input("What motion do you want to edit?: ")
		if name == "none":
			print "nothing edited"
		else:
			homedir = os.environ['HOME']
			name = homedir + "/catkin_ws/src/jimmy/motions/" + name + ".txt"
			
			try:
				file = open(name,"a")
				print "motion file is opened for editting"
				print "press on 'a' to add a new motion frame"
				edit = 1
				button = 0
				
			except:
				print "motion file doens't exist"
				
	elif button == 101 and edit == 1:
		print "you need to complete editing the previous motion file first - in order to do it press c"
		name = raw_input("press enter to go back")
		
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
		motion_counter = motion_counter + 1
		print str(motion_counter) + "new motion is added"
		print "press on 'a' to add a new motion frame press c to save exit and the motion file."
		button = 0
		
	# press on "c" to exit a motion file
	if button == 99 and edit == 1:
		os.system('cls' if os.name == 'nt' else 'clear')
		name = ""
		file.close()
		print "file is closed"
		edit = 0
		button = 0
		motion_counter = 0
					
	# press on "t" to exit a motion file
	if button == 116 and edit != 1:
		os.system('cls' if os.name == 'nt' else 'clear')
		#define service calls
		service1 = rospy.ServiceProxy('/right_shoulder_controller/torque_enable', TorqueEnable)
		service2 = rospy.ServiceProxy('/left_shoulder_controller/torque_enable', TorqueEnable)
		service3 = rospy.ServiceProxy('/right_elbow_controller/torque_enable', TorqueEnable)
		service4 = rospy.ServiceProxy('/left_elbow_controller/torque_enable', TorqueEnable)
		service5 = rospy.ServiceProxy('/right_hand_controller/torque_enable', TorqueEnable)
		service6 = rospy.ServiceProxy('/left_hand_controller/torque_enable', TorqueEnable)
		service7 = rospy.ServiceProxy('/right_hip_turn_controller/torque_enable', TorqueEnable)
		service8 = rospy.ServiceProxy('/left_hip_turn_controller/torque_enable', TorqueEnable)
		service9 = rospy.ServiceProxy('/right_hip_shake_controller/torque_enable', TorqueEnable)
		service10 = rospy.ServiceProxy('/left_hip_shake_controller/torque_enable', TorqueEnable)
		service11 = rospy.ServiceProxy('/right_hip_bend_controller/torque_enable', TorqueEnable)
		service12 = rospy.ServiceProxy('/left_hip_bend_controller/torque_enable', TorqueEnable)
		service13 = rospy.ServiceProxy('/right_knee_controller/torque_enable', TorqueEnable)
		service14 = rospy.ServiceProxy('/left_knee_controller/torque_enable', TorqueEnable)
		service15 = rospy.ServiceProxy('/right_ankle_controller/torque_enable', TorqueEnable)
		service16 = rospy.ServiceProxy('/left_ankle_controller/torque_enable', TorqueEnable)
		service17 = rospy.ServiceProxy('/right_foot_controller/torque_enable', TorqueEnable)
		service18 = rospy.ServiceProxy('/left_foot_controller/torque_enable', TorqueEnable)
		service19 = rospy.ServiceProxy('/neck_controller/torque_enable', TorqueEnable)
		service20 = rospy.ServiceProxy('/head_controller/torque_enable', TorqueEnable)
		
		# enable all servos
		if all_enabled == 0:
			service1(1)
			service2(1)
			service3(1)
			service4(1)
			service5(1)
			service6(1)
			service7(1)
			service8(1)
			service9(1)
			service10(1)
			service11(1)
			service12(1)
			service13(1)
			service14(1)
			service15(1)
			service16(1)
			service17(1)
			service18(1)
			service19(1)
			service20(1)
			enabled = 1
			print "torque is enabled"
		
		# disable all servos
		elif all_enabled == 1:
			service1(0)
			service2(0)
			service3(0)
			service4(0)
			service5(0)
			service6(0)
			service7(0)
			service8(0)
			service9(0)
			service10(0)
			service11(0)
			service12(0)
			service13(0)
			service14(0)
			service15(0)
			service16(0)
			service17(0)
			service18(0)
			service19(0)
			service20(0)
			all_enabled = 0
			print "torque is disabled"
			
	if button == 121 and edit !=1:
		os.system('cls' if os.name == 'nt' else 'clear')
		#define service calls
		service1 = rospy.ServiceProxy('/right_shoulder_controller/torque_enable', TorqueEnable)
		service2 = rospy.ServiceProxy('/left_shoulder_controller/torque_enable', TorqueEnable)
		service3 = rospy.ServiceProxy('/right_elbow_controller/torque_enable', TorqueEnable)
		service4 = rospy.ServiceProxy('/left_elbow_controller/torque_enable', TorqueEnable)
		service5 = rospy.ServiceProxy('/right_hand_controller/torque_enable', TorqueEnable)
		service6 = rospy.ServiceProxy('/left_hand_controller/torque_enable', TorqueEnable)
		service19 = rospy.ServiceProxy('/neck_controller/torque_enable', TorqueEnable)
		service20 = rospy.ServiceProxy('/head_controller/torque_enable', TorqueEnable)
		
		print "body Part Torque Setting:"
		
		print "- left arm on"
		print "- left arm off"
		print "- right arm on"
		print "- right arm off"
		print "- head on"
		print "- head off"
		
		part = raw_input("type your choice:")
		
		if part == "right arm on":
		# enable right arm servos
			service1(1)
			service3(1)
			service5(1)
			right_arm_enabled = 1
			
			print "right arm is enabled"

		# disable right arm servos
		elif part == "right arm off":
			service1(0)
			service3(0)
			service5(0)
			left_arm_enabled = 0
				
			print "right arm is disabled"
		
		elif part == "left arm on":
		# enable left arm servos
			service2(1)
			service4(1)
			service6(1)
				
			print "left arm is enabled"

			# disable left arm servos
		elif part == "left arm off":
			service2(0)
			service4(0)
			service6(0)
				
			print "left arm is disabled"
				
		elif part == "head on":
			service19(1)
			service20(1)
				
			print "head is enabled"

			# disable head servos
		elif part == "head off":
			service19(0)
			service20(0)
			
			print "head is disabled"
			
		else:
			print "wrong parameter"
			
		name = raw_input("press enter to go back")
	
	if edit != 1:
		os.system('cls' if os.name == 'nt' else 'clear')
		print "motion saver v1.0 - main menu"
		print "- n = create a new motion file"
		print "- e = edit a motion file"
		print "- c = save and exit editting a motion file"
		print "- t = enable/disable all servos"
		print "- y = enable disable a body part"
		print "- h = help"
			
# callback funtions for reading joint locations
# updates the position[i] list
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

# main module for the motion saver node
# create a node and define callback funtions for topics
def motion_control():
	
	os.system('cls' if os.name == 'nt' else 'clear')
	print "motion editor v1.0 - main menu"
	print "- n = create a new motion file"
	print "- e = edit a motion file"
	print "- c = save and exit editting a motion file"
	print "- t = enable/disable all servos"
	print "- y = enable/disable a body part"
	print "- p = play a motion file"
	print "- h = help"
	
	rospy.init_node('motion_saver', anonymous=True)
	rospy.Subscriber('/keyboard/keydown', Key, keyboard_capture,queue_size=1)
	
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