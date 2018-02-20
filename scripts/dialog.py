#!/usr/bin/env python
import rospy
import os
import time
from std_msgs.msg import String
import flow

global texts
texts = [""]

project_id = "sli-hw2"
session_id = "1-1-1-1-1"

def callback(data):
	global texts
	texts[0] = data.data
	print str(flow.detect_intent_texts(project_id, session_id, texts, 'en-US'))
	
def init_jimmy():
	rospy.init_node('dialog_jimmy', anonymous=True)
	rospy.Subscriber("/text", String, callback)
	rospy.spin()
	
if __name__ == '__main__':
	init_jimmy()
