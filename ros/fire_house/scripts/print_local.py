#!/usr/bin/env python  

import sys, select, termios, tty
import rospy
import math
import tf
import roslib
roslib.load_manifest("rosparam")
import rosparam
import time
import os
#import rospkg

import geometry_msgs.msg
import turtlesim.srv

import rospy 
import rospkg 
from gazebo_msgs.msg import ModelState 
#from gazebo_msgs.srv import SetModelState

from gazebo_msgs.srv import GetModelState


def getipaddrs(hostname):
    result = socket.getaddrinfo(hostname, None, 0, socket.SOCK_STREAM)
    return [x[4][0] for x in result]



class local_server:
    def __init__(self):


        self.local_x = 0
        self.local_y = 0
	#self.GetModelState = ModelState()
    	#self.state_msg.model_name = 'dog2'

	

        #print "load param success"
        #self.plocal(format(self.local_x),format(self.local_y))


        self.listener = tf.TransformListener()

    def plocal(self,X,Y):
        print ("**********************************************")
        print ("value:")
        print ("local { x %s , y %s }" % (X,Y))
        time.sleep(0.1)

    def update(self):
	self.model_coordinates = rospy.ServiceProxy( '/gazebo/get_model_state', GetModelState)
	self.state_msg = self.model_coordinates("dog2", "world")
	
        try:
            #(trans,rot) = self.listener.lookupTransform('/gazebo/odom', '/base_link', rospy.Time(0))
            #trans[0] = round(trans[0],3)
            #trans[1] = round(trans[1],3)

            self.local_x = round(self.state_msg.pose.position.x,4)
            self.local_y = round(self.state_msg.pose.position.y,4)
            print ("**********************************************")
            #print("find local  x: %f , y: %f " % (trans[0],trans[1]))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            print ("local not finded")

        time.sleep(0.1)

    def transfer(self):
	if(self.local_x>0):
       	    sx = "+"+format((int)(self.local_x*100)).zfill(4)
	else:
	    sx = format((int)(self.local_x*100)).zfill(5)
	if(self.local_y>0):
       	    sy = "+"+format((int)(self.local_y*100)).zfill(4)
	else:
	    sy = format((int)(self.local_y*100)).zfill(5)

	tran = sx+" "+sy
        
	print(tran)

	


if __name__ == '__main__':
    rospy.init_node('gazebo_listener')
    up = local_server()
    while True:
        if not rospy.is_shutdown():
            up.update()
            up.transfer()
        else:
            print "Shutting down"
            sys.exit(0)
