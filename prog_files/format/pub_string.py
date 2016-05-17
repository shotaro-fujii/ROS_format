#!/usr/bin/env python
# coding: utf-8

import rospy
from std_msgs.msg import String


class Pub_String:

    def __init__(self):  
        rospy.init_node('String')
        self.pub1 = rospy.Publisher('topic1', String ,queue_size=10)
        self.pub_data = String()	

    def publish(self):
        while not rospy.is_shutdown():
            rate = rospy.Rate(5)
            self.pub_data = "String"
            self.pub1.publish(self.pub_data)       
            rate.sleep()


if __name__ == "__main__":

    ps = Pub_String()
    ps.publish()
