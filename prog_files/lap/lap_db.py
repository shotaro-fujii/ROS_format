# coding: utf-8
import my_route
#import weather
#import user_table
from time import sleep

import rospy
from std_msgs.msg import String
#from std_msgs.msg import Int8

class Excite_DB:

    #self.msg1 = 1
    #self.msg2 = 2
    msg3 = 3
    
    
    def __init__(self):
        #self.__excite_data_list = []
        rospy.init_node('data_set')
        self.pub1 = rospy.Publisher('topic4', String ,queue_size=10)
        #self.pub = String()


    def subscribe(self):

        #sub1 = rospy.Subscriber('topic1', String, self.callback1)
        #sub2 = rospy.Subscriber('topic2', String, self.callback2)
        sub3 = rospy.Subscriber('topic3',  String, self.callback3)
       

    #def callback1(self, msg):
        #print msg.data  
        #self.msg1 = msg.data      
        

    #def callback2(self, msg):
        #print "ue", msg.data     
        #self.msg2 = msg.data
        #print self.msg2
    
    def callback3(self, msg):
        #print msg.data     
        self.msg3 = msg.data

    def add_publish(self):
        #rate = rospy.Rate(10)
        #while not rospy.is_shutdown():
        print self.msg3
        #if self.msg2 == "True":
            #print self.msg1, self.msg3
            #self.pub1.publish(str(self.msg1))
            #self.pub1.publish(str(self.msg3))
            #rate.sleep()

if __name__ == "__main__":


    data_set = Excite_DB()
    data_set.subscribe()   
    while True:

        
        data_set.add_publish() 

