#!/usr/bin/env python
import rospy
from  std_msgs.msg import Int8

rospy.init_node('talker1')
pub = rospy.Publisher('topic3', Int8, queue_size=10)
rate = rospy.Rate(10)

while not rospy.is_shutdown():
    a = 10
    pub.publish(a)
    rate.sleep()

