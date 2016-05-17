# coding: utf-8
import random
#import lap_db
from time import sleep

import rospy
from std_msgs.msg import Int8
from std_msgs.msg import String

class Excited_trigger:

    def __init__(self):  
        self.__excite_level = 0
        self.__flag = [False, 0]

        rospy.init_node('trigger')
        self.pub1 = rospy.Publisher('topic4', String ,queue_size=10)
        self.pub2 = rospy.Publisher('topic3', Int8 ,queue_size=10)


	
    def send_trigger(self):
        while not rospy.is_shutdown():
            self.__excite_level = random.randint(0, 100)
        
            if self.__excite_level > 90:
                self.__flag = [True, self.__excite_level]			
            else:
                self.__flag = [False, self.__excite_level]

            rate = rospy.Rate(5)
            
            print self.__flag
            self.pub1.publish(str(self.__flag[0]))
            self.pub2.publish(self.__flag[1])
            
            rate.sleep()


if __name__ == "__main__":

    # インスタンス作成
    trigger = Excited_trigger()
     
    trigger.send_trigger()

        #sleep(1)




