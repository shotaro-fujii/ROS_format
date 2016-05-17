#!/usr/bin/env python
# coding: utf-8

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int8
from rospy_tutorials.msg import Floats

class Sub_Pub:

    msg1 = 1
    msg2 = 2
    msg3 = 3
    msg4 = 4
    #msg5 = 5

    def __init__(self):
        rospy.init_node('sub_pub')
        #self.pub1 = rospy.Publisher('topic4', String ,queue_size=10)

    def subscribe(self):
        sub1 = rospy.Subscriber('topic1', String, self.callback1)
        sub2 = rospy.Subscriber('topic2', String, self.callback2)
        sub3 = rospy.Subscriber('topic3',  Floats, self.callback3)        
        sub4 = rospy.Subscriber('topic4',  Int8, self.callback4)
        #sub5 = rospy.Subscriber('topic5',  String, self.callback4)

    def callback1(self, msg):
        #print msg.data  
        self.msg1 = msg.data      
        
    def callback2(self, msg):
        #print msg.data     
        self.msg2 = msg.data      
        #print type(self.msg2)

    def callback3(self, msg):
        #print msg.data     
        self.msg3 = msg.data

    def callback4(self, msg):
        #print msg.data     
        self.msg4 = msg.data

    #def callback5(self, msg):
        #print msg.data     
        #self.msg5 = msg.data

    def cal_publish(self):
        rate = rospy.Rate(5)
        while not rospy.is_shutdown():
            print self.msg1
            print self.msg2
            print self.msg3
            print self.msg4
            #print self.msg5
            
            #if self.msg4 == "String":
                                
            rate.sleep()

if __name__ == "__main__":


    sp = Sub_Pub()
    sp.subscribe()           
    sp.cal_publish() 

