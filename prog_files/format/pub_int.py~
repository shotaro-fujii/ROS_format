#!/usr/bin/env python
# coding: utf-8

import rospy
from std_msgs.msg import Int8


class Pub_Int:

    def __init__(self):  
        rospy.init_node('Int')
        self.pub1 = rospy.Publisher('topic4', Int8 ,queue_size=10)
        self.pub_data = Int8()	

    def publish(self):
        while not rospy.is_shutdown():
            rate = rospy.Rate(5)
            self.pub_data = 99
            self.pub1.publish(self.pub_data)       
            rate.sleep()


if __name__ == "__main__":

    pi = Pub_Int()
    pi.publish()
