# coding: utf-8
import my_route
#import weather
#import user_table
from time import sleep

import rospy
from std_msgs.msg import String
from std_msgs.msg import Int8
from rospy_tutorials.msg import Floats

class Excite_DB:

    msg1 = 1
    msg2 = 2
    msg3 = 3
    msg4 = 4

    def __init__(self):
        #self.__excite_data_list = []
        rospy.init_node('data_set')
        self.pub1 = rospy.Publisher('topic4', String ,queue_size=10)
        self.data_set = []


    def subscribe(self):

        sub1 = rospy.Subscriber('topic1', Floats, self.callback1)
        sub2 = rospy.Subscriber('topic2', String, self.callback2)
        sub3 = rospy.Subscriber('topic3',  Int8, self.callback3)
        sub4 = rospy.Subscriber('topic4',  String, self.callback4)
       

    def callback1(self, msg):
        #print msg.data  
        self.msg1 = msg.data      
        

    def callback2(self, msg):
        #print msg.data     
        self.msg2 = msg.data
        
    
    def callback3(self, msg):
        #print msg.data     
        self.msg3 = msg.data

    def callback4(self, msg):
        #print msg.data     
        self.msg4 = msg.data


    def add_publish(self):
        rate = rospy.Rate(5)
        while not rospy.is_shutdown():
            #print self.msg1
            #print self.msg2
            #print self.msg3
            #print self.msg4
            
            if self.msg4 == "True":
                self.data_set.append(self.msg3)
                self.data_set.extend(self.msg1)
                self.data_set.append(self.msg2)
                print self.data_set
                self.data_set = []

            rate.sleep()

if __name__ == "__main__":


    data_set = Excite_DB()
    data_set.subscribe()           
    data_set.add_publish() 

