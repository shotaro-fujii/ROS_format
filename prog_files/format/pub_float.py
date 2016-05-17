#!/usr/bin/env python
# coding: utf-8

import rospy
from std_msgs.msg import String


class Pub_Float:

    def __init__(self):  
        rospy.init_node('Float')
        self.pub1 = rospy.Publisher('topic2', String ,queue_size=10)
	self.pub_data = String()

    def publish(self):
        while not rospy.is_shutdown():
            rate = rospy.Rate(5)
            self.pub_data = 123.456
            self.pub1.publish(str(self.pub_data))     
            rate.sleep()


if __name__ == "__main__":

    pf = Pub_Float()
    pf.publish()
