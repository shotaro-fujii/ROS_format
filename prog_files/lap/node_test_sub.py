#!/usr/bin/env python
import rospy
from std_msgs.msg import String


def callback(msg):
    print msg.data
    

rospy.init_node('listener')
sub = rospy.Subscriber('topic4', String, callback)
rospy.spin()
