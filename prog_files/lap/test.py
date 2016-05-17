#!/usr/bin/env python
import rospy
from rospy_tutorials.msg import Floats
 
rospy.init_node('talker')
pub = rospy.Publisher('topic1', Floats, queue_size=10)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    hello = [1.0, 2.0]
    pub.publish(hello)
    rate.sleep()
