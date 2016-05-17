# coding: utf-8

import rospy
from rospy_tutorials.msg import Floats
from std_msgs.msg import String

class Excited_route:

    route_list = []

    def __init__(self, number):
        self.__number = number
        self.__route_list = Excited_route.route_list * self.__number * 3
        self.__route_list = Excited_route.route_list
	
    def set_route(self, gps_data):	
        self.__route_list.extend(gps_data) 
        if len(self.__route_list) - (3*self.__number) >=1:
            del self.__route_list[:(len(self.__route_list) - (3*self.__number))]
            #print self.__route_list
        
            rospy.init_node('route')
            pub1 = rospy.Publisher('topic1', Floats ,queue_size=10)
            pub2 = rospy.Publisher('topic2', String ,queue_size=10)
            #print ([self.__route_list[0], self.__route_list[1]])
            pub1.publish([self.__route_list[0], self.__route_list[1]])
            pub2.publish(self.__route_list[2])
     

